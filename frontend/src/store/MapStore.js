import {action, computed, observable, reaction} from "mobx";
import {rest} from './RestStore'
class MapStore {
    @observable _isHeatMap = false;
    @observable _isMarkersMap = false;
    @observable _eventMarkers = [];
    @action toggleHeatMap(){
        this._isHeatMap = !this._isHeatMap;
    }
    @action activateMarkersMap() {
        this._isMarkersMap = true;
    }
    @action deactivateMarkersMap() {
        this._isMarkersMap = false;
    }
    @computed get isMarkersMap() {
        return this._isMarkersMap
    }
    @computed get isHeatMap(){
        return this._isHeatMap
    }
    @action addEventMarker(latlng){
        // this.
    }
    @computed get eventsMarkers() {
        return this._eventMarkers
    }
    @action setEventMarkers(markers) {
        this._eventMarkers = markers;
    }
    @action addEventMarker(marker) {
        this._eventMarkers.push(marker);
    }
    @action editLastEventMarker(marker) {
        this._eventMarkers.splice(
            this._eventMarkers.length - 1,
            1,
            marker)
    }
    reactAddressPoints = reaction(() => rest.addressPoints,
        (adresspoints) => {
            this.setEventMarkers(adresspoints.map(({lat, long}) => [lat,long]))
        })
    @computed get addressPoints() {
        return rest.organisationsEvents.map(
            ({lat, long}) => [lat, long, Math.random()*1000]
        )
    }
}
export const mapStore = new MapStore();
