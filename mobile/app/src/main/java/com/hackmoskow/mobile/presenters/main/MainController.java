package com.hackmoskow.mobile.presenters.main;

import com.hackmoskow.mobile.domain.executor.Executor;
import com.hackmoskow.mobile.domain.executor.ThreadExecutor;
import com.hackmoskow.mobile.domain.models.Places;
import com.hackmoskow.mobile.domain.models.UserData;
import com.hackmoskow.mobile.domain.repository.PlacesRepository;
import com.hackmoskow.mobile.domain.repository.UserProfileRepository;
import com.hackmoskow.mobile.domain.services.positionsender.PositionSenderService;
import com.hackmoskow.mobile.domain.services.positionsender.PositionSenderServiceCallback;
import com.hackmoskow.mobile.domain.threading.MainThread;
import com.hackmoskow.mobile.domain.threading.MainThreadImpl;
import com.hackmoskow.mobile.ui.main.BasicMapActivity;
import com.here.android.mpa.common.GeoCoordinate;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class MainController implements PositionSenderServiceCallback {

    private PositionSenderService positionSenderService;
    private BasicMapActivity view;
    private Executor executor;
    private MainThread mainThread;
    private List<GeoCoordinate> coordinates;
    private Date lastCoordinatesAdd;
    private UserProfileRepository userProfileRepository;
    private PlacesRepository placesRepository;
    private List<Places> places;
    volatile private int countOfPaused = 0;

    public MainController(BasicMapActivity view) {
        this.positionSenderService = new PositionSenderService(view.getContentResolver());
        this.executor = ThreadExecutor.getInstance();
        this.mainThread = MainThreadImpl.getInstance();
        this.view = view;
        this.coordinates = new ArrayList<>();
        this.userProfileRepository = new UserProfileRepository("userData.txt", view);
        this.placesRepository = new PlacesRepository(view.getContentResolver());
        this.places = new ArrayList<>();

        checkUserData();
    }

    private void checkUserData() {
        executor.execute(() -> {
            UserData userData = userProfileRepository.getUserData();
            if (userData == null) {
                mainThread.post(() -> view.showUserDataAlert());
            }
        });
    }

    public void positionChanged(GeoCoordinate coordinate) {
        executor.execute(() -> {
            if (lastCoordinatesAdd == null || coordinates.size() == 0) {
                coordinates.add(coordinate);
                System.out.println("Add first!!!");
                lastCoordinatesAdd = new Date();
                return;
            }

            System.out.println(lastCoordinatesAdd.getTime() - new Date().getTime());
            if (new Date().getTime() - lastCoordinatesAdd.getTime() > 60000) {

                GeoCoordinate lastCoordinate = getCoordinate();
                if (Math.abs(coordinate.getLatitude() - lastCoordinate.getLatitude()) > 0.001 ||
                        Math.abs(coordinate.getLongitude() - lastCoordinate.getLongitude()) > 0.001) {
                    if (coordinates.size() > 5) {
                        System.out.println("Send location!!!");
                        positionSenderService.sendLocation(lastCoordinate.getLatitude(), lastCoordinate.getLongitude(), coordinates.size());
                    } else {
                        coordinates.clear();
                        coordinates.add(coordinate);
                        System.out.println("Add FIRST!!!");
                        lastCoordinatesAdd = new Date();
                    }
                } else {
                    coordinates.add(coordinate);
                    System.out.println("Add one more!!!");
                    lastCoordinatesAdd = new Date();
                }
            }
        });
    }

    public void readyForGetPlaces(GeoCoordinate coordinate) {
        executor.execute(() -> {
            List<Places> places = placesRepository.getPlaces(coordinate.getLatitude(), coordinate.getLongitude());
            this.places.clear();
            this.places.addAll(places);
            mainThread.post(() -> view.showNearestPlaces(places));
        });
    }

    public void placePressed(double latitude, double longitude) {
        executor.execute(() -> {
            for (Places place : places) {
                if (place.getCoordinate().getLongitude() == longitude &&
                        place.getCoordinate().getLatitude() == latitude) {
                    mainThread.post(() -> view.showPlaceInfo(place));
                    return;
                }
            }
        });
    }

    public void mapPressed() {
        executor.execute(() -> {
            System.out.println("PRESSED");
            countOfPaused++;

            view.setPaused(true);
            try {
                Thread.sleep(5000);
            } catch (Exception ignored) {

            } finally {
                countOfPaused--;
                System.out.println("UNPRESSED");
                if (countOfPaused == 0) {
                    view.setPaused(false);
                }
            }
        });
    }

    @Override
    public void onLostConnection() {
        mainThread.post(() -> view.showLostConnection());
    }

    private GeoCoordinate getCoordinate() {
        double midleLatitude = 0;
        double midleLongitude = 0;

        for (GeoCoordinate coord : coordinates) {
            midleLatitude += coord.getLatitude();
            midleLongitude += coord.getLongitude();
        }
        midleLatitude /= coordinates.size();
        midleLongitude /= coordinates.size();

        return new GeoCoordinate(midleLatitude, midleLongitude);
    }
}
