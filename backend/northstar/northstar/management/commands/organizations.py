'''from here import HERE

coord = [
    {'lat': 55.7522, 'long': 37.6156},
    {'lat': 55.800028, 'long': 37.557448},
    {'lat': 55.700028, 'long': 37.557448},
    {'lat': 55.600028, 'long': 37.557448},
    {'lat': 55.800028, 'long': 38.557448},
    {'lat': 55.800028, 'long': 36.557448},
]
places_list = []
for c in coord:
    places_list.append(HERE.get_place_by_location(c))

new_places = []
for item in places_list:
    for it in item:
        new_places.append(it)
print(new_places)'''
new_places = [{'location': {'long': 37.61234, 'lat': 55.7535}, 'distance': 250, 'title': 'Coffee House',
               'category': 'restaurant'},
              {'location': {'long': 37.61234, 'lat': 55.7535}, 'distance': 250, 'title': 'Cofix',
               'category': 'restaurant'},
              {'location': {'long': 37.61234, 'lat': 55.7535}, 'distance': 250, 'title': 'Zamyaso',
               'category': 'restaurant'},
              {'location': {'long': 37.61127, 'lat': 55.75279}, 'distance': 279, 'title': 'Eat & Talk',
               'category': 'bar-pub'},
              {'location': {'long': 37.61009, 'lat': 55.75065}, 'distance': 385, 'title': 'Korchma Taras Bulba',
               'category': 'restaurant'},
              {'location': {'long': 37.61484, 'lat': 55.75576}, 'distance': 399, 'title': 'Chacha Room',
               'category': 'restaurant'},
              {'location': {'long': 37.61159, 'lat': 55.75497}, 'distance': 397, 'title': 'Cut',
               'category': 'restaurant'},
              {'location': {'long': 37.62077, 'lat': 55.75433}, 'distance': 401, 'title': 'Coffee House',
               'category': 'coffee-tea'},
              {'location': {'long': 37.60988, 'lat': 55.75389}, 'distance': 404, 'title': 'Fish Chain',
               'category': 'restaurant'},
              {'location': {'long': 37.615523, 'lat': 55.755891}, 'distance': 410, 'title': 'Menza',
               'category': 'restaurant'},
              {'location': {'long': 37.60986, 'lat': 55.7502}, 'distance': 422, 'title': 'Cafe 1892',
               'category': 'restaurant'},
              {'location': {'long': 37.6162, 'lat': 55.75615}, 'distance': 441, 'title': 'KODO',
               'category': 'restaurant'},
              {'location': {'long': 37.61543, 'lat': 55.75621}, 'distance': 446, 'title': 'Osteria Mario',
               'category': 'restaurant'},
              {'location': {'long': 37.61973, 'lat': 55.75551}, 'distance': 450, 'title': 'Drova',
               'category': 'restaurant'},
              {'location': {'long': 37.619663, 'lat': 55.755619}, 'distance': 457, 'title': 'Laduree Restaurant',
               'category': 'restaurant'},
              {'location': {'long': 37.62153, 'lat': 55.75468}, 'distance': 462, 'title': 'Coffeemania',
               'category': 'restaurant'},
              {'location': {'long': 37.62153, 'lat': 55.75468}, 'distance': 462, 'title': 'Bosco Cafe',
               'category': 'restaurant'},
              {'location': {'long': 37.61899, 'lat': 55.756}, 'distance': 473, 'title': 'Vassa & Co',
               'category': 'clothing-accessories-shop'},
              {'location': {'long': 37.60754, 'lat': 55.75125}, 'distance': 515, 'title': 'RULE taproom',
               'category': 'restaurant'},
              {'location': {'long': 37.614174, 'lat': 55.75661}, 'distance': 498, 'title': 'Bar Alexandrovsky',
               'category': 'restaurant'},
              {'location': {'long': 37.55893, 'lat': 55.799445}, 'distance': 113, 'title': 'Mnogo Lososya',
               'category': 'restaurant'},
              {'location': {'long': 37.56018, 'lat': 55.79987}, 'distance': 172, 'title': 'Bufet Cafe',
               'category': 'restaurant'},
              {'location': {'long': 37.5593, 'lat': 55.80398}, 'distance': 454, 'title': 'Pizza na Drovakh',
               'category': 'restaurant'},
              {'location': {'long': 37.547039, 'lat': 55.793678}, 'distance': 960, 'title': 'Heritage Restaurant',
               'category': 'restaurant'},
              {'location': {'long': 37.5435, 'lat': 55.79432}, 'distance': 1078, 'title': 'Sikvaruli',
               'category': 'restaurant'},
              {'location': {'long': 37.569135, 'lat': 55.792412}, 'distance': 1118, 'title': 'Izba na Maslovke',
               'category': 'restaurant'},
              {'location': {'long': 37.57568, 'lat': 55.79994}, 'distance': 1140, 'title': 'Khinkalnaya City',
               'category': 'restaurant'},
              {'location': {'long': 37.56914, 'lat': 55.79218}, 'distance': 1138, 'title': 'Pizza Presto',
               'category': 'restaurant'},
              {'location': {'long': 37.54433, 'lat': 55.7918}, 'distance': 1229, 'title': 'Ibis Moscow Dynamo Hotel',
               'category': 'hotel'},
              {'location': {'long': 37.559548, 'lat': 55.788825}, 'distance': 1253, 'title': 'Cosmic Latte',
               'category': 'restaurant'},
              {'location': {'long': 37.56698, 'lat': 55.78798}, 'distance': 1466, 'title': 'Larionov',
               'category': 'restaurant'},
              {'location': {'long': 37.56633, 'lat': 55.78721}, 'distance': 1530, 'title': 'Oriental Cocktail Bar',
               'category': 'restaurant'},
              {'location': {'long': 37.581342, 'lat': 55.796514}, 'distance': 1544, 'title': 'Factoria Beer&Grill',
               'category': 'restaurant'},
              {'location': {'long': 37.58206, 'lat': 55.80437}, 'distance': 1612, 'title': 'Tkven-Genatsvalet',
               'category': 'restaurant'},
              {'location': {'long': 37.58146, 'lat': 55.80581}, 'distance': 1633, 'title': 'AyDaBaran',
               'category': 'restaurant'},
              {'location': {'long': 37.56212, 'lat': 55.78539}, 'distance': 1654, 'title': 'Restaurant Parisienne',
               'category': 'restaurant'},
              {'location': {'long': 37.56598, 'lat': 55.81402}, 'distance': 1645, 'title': 'Pivarius',
               'category': 'restaurant'},
              {'location': {'long': 37.58392, 'lat': 55.79947}, 'distance': 1656, 'title': 'Beer Restaurant Bruder',
               'category': 'restaurant'},
              {'location': {'long': 37.55782, 'lat': 55.785035}, 'distance': 1667, 'title': 'Karaoke Club Sing',
               'category': 'restaurant'},
              {'location': {'long': 37.58399, 'lat': 55.79719}, 'distance': 1689, 'title': 'Hizhina',
               'category': 'restaurant'},
              {'location': {'long': 37.55778, 'lat': 55.69435}, 'distance': 632, 'title': "Brawler's Pub",
               'category': 'restaurant'},
              {'location': {'long': 37.550777, 'lat': 55.704484}, 'distance': 648, 'title': 'Coffee House',
               'category': 'restaurant'},
              {'location': {'long': 37.56394, 'lat': 55.70629}, 'distance': 806, 'title': 'Korston',
               'category': 'hotel'},
              {'location': {'long': 37.56402, 'lat': 55.70603}, 'distance': 784, 'title': 'Extra Lounge',
               'category': 'restaurant'},
              {'location': {'long': 37.56409, 'lat': 55.70604}, 'distance': 787, 'title': 'EVOO',
               'category': 'restaurant'},
              {'location': {'long': 37.56559, 'lat': 55.70561}, 'distance': 803, 'title': 'JU-JU Lounge & Bar',
               'category': 'restaurant'}, {'location': {'long': 37.54432, 'lat': 55.69635}, 'distance': 919,
                                           'title': 'Moscow Children’S Musical Theatre',
                                           'category': 'theatre-music-culture'},
              {'location': {'long': 37.57166, 'lat': 55.70466}, 'distance': 1029, 'title': 'Darbar',
               'category': 'restaurant'},
              {'location': {'long': 37.57229, 'lat': 55.70512}, 'distance': 1089, 'title': 'Darbars',
               'category': 'restaurant'},
              {'location': {'long': 37.54491, 'lat': 55.70788}, 'distance': 1174, 'title': 'Restaurant Tramplin',
               'category': 'restaurant'},
              {'location': {'long': 37.54184, 'lat': 55.70789}, 'distance': 1312, 'title': 'Coffee and the City',
               'category': 'coffee-tea'},
              {'location': {'long': 37.57838, 'lat': 55.7023}, 'distance': 1336, 'title': 'Petrushka',
               'category': 'restaurant'},
              {'location': {'long': 37.54678, 'lat': 55.71137}, 'distance': 1427, 'title': 'Prawns',
               'category': 'restaurant'},
              {'location': {'long': 37.58069, 'lat': 55.70182}, 'distance': 1470, 'title': 'Syncope Сoffee',
               'category': 'restaurant'},
              {'location': {'long': 37.58044, 'lat': 55.70303}, 'distance': 1479, 'title': 'Angelo',
               'category': 'restaurant'},
              {'location': {'long': 37.54303, 'lat': 55.68891}, 'distance': 1531, 'title': 'Bekers',
               'category': 'restaurant'},
              {'location': {'long': 37.576049, 'lat': 55.690756}, 'distance': 1556, 'title': 'Wine Buffet',
               'category': 'restaurant'},
              {'location': {'long': 37.57572, 'lat': 55.68977}, 'distance': 1616, 'title': 'Lustra Bar',
               'category': 'restaurant'},
              {'location': {'long': 37.571551, 'lat': 55.68774}, 'distance': 1627, 'title': 'Billy McDaniel',
               'category': 'restaurant'},
              {'location': {'long': 37.572527, 'lat': 55.687822}, 'distance': 1654, 'title': 'Pravda Coffee',
               'category': 'restaurant'},
              {'location': {'long': 37.55516, 'lat': 55.59838}, 'distance': 233, 'title': 'Karaoke Bar Mule',
               'category': 'restaurant'},
              {'location': {'long': 37.537022, 'lat': 55.610185}, 'distance': 1709, 'title': 'Territoria Yasenevo',
               'category': 'restaurant'},
              {'location': {'long': 37.53875, 'lat': 55.61372}, 'distance': 1923, 'title': 'Coffee Yest!',
               'category': 'restaurant'},
              {'location': {'long': 37.52561, 'lat': 55.59794}, 'distance': 2014, 'title': 'Yapono Italyano',
               'category': 'restaurant'},
              {'location': {'long': 37.52561, 'lat': 55.59794}, 'distance': 2014, 'title': 'Shakers',
               'category': 'restaurant'},
              {'location': {'long': 37.572342, 'lat': 55.580041}, 'distance': 2411, 'title': 'New Moscow',
               'category': 'restaurant'},
              {'location': {'long': 37.51191, 'lat': 55.59657}, 'distance': 2887, 'title': 'Artiko',
               'category': 'restaurant'},
              {'location': {'long': 37.60307, 'lat': 55.59596}, 'distance': 2902, 'title': 'Sun Sushi',
               'category': 'restaurant'},
              {'location': {'long': 37.60638, 'lat': 55.5958}, 'distance': 3110, 'title': 'Shtirbeerlits',
               'category': 'restaurant'},
              {'location': {'long': 37.60487, 'lat': 55.6127}, 'distance': 3295, 'title': 'Beans&Berries',
               'category': 'restaurant'},
              {'location': {'long': 37.60669, 'lat': 55.61077}, 'distance': 3316, 'title': 'Svarnya',
               'category': 'restaurant'},
              {'location': {'long': 37.60669, 'lat': 55.61077}, 'distance': 3316, 'title': 'Sultan Restaurant',
               'category': 'restaurant'},
              {'location': {'long': 37.60697, 'lat': 55.6121}, 'distance': 3388, 'title': 'Cutlet',
               'category': 'restaurant'},
              {'location': {'long': 37.60888, 'lat': 55.61127}, 'distance': 3464, 'title': 'Chaihona No 1',
               'category': 'restaurant'},
              {'location': {'long': 37.612894, 'lat': 55.592902}, 'distance': 3572, 'title': 'Bakery Tartin',
               'category': 'restaurant'},
              {'location': {'long': 37.506677, 'lat': 55.617203}, 'distance': 3717, 'title': 'Chocolate',
               'category': 'restaurant'}, {'location': {'long': 37.50922, 'lat': 55.61949}, 'distance': 3723,
                                           'title': 'Aleksandr Seleznev - Confectionery', 'category': 'restaurant'},
              {'location': {'long': 37.50738, 'lat': 55.61823}, 'distance': 3740, 'title': 'Coffee House',
               'category': 'coffee-tea'},
              {'location': {'long': 37.605622, 'lat': 55.621964}, 'distance': 3886, 'title': 'Cafe Chocolate',
               'category': 'restaurant'},
              {'location': {'long': 37.60336, 'lat': 55.62508}, 'distance': 4009, 'title': 'Chaihona No 1',
               'category': 'restaurant'},
              {'location': {'long': 38.46511, 'lat': 55.79781}, 'distance': 5777, 'title': 'Beer Club Tolsty Medved',
               'category': 'restaurant'},
              {'location': {'long': 38.65585, 'lat': 55.77981}, 'distance': 6550, 'title': 'Fabrika Obedov',
               'category': 'restaurant'},
              {'location': {'long': 38.655801, 'lat': 55.776743}, 'distance': 6672, 'title': 'Aristokrat',
               'category': 'hotel'},
              {'location': {'long': 38.44297, 'lat': 55.778}, 'distance': 7565, 'title': 'Fabrika Obedov',
               'category': 'restaurant'},
              {'location': {'long': 38.444272, 'lat': 55.770561}, 'distance': 7798, 'title': 'Yason',
               'category': 'restaurant'},
              {'location': {'long': 38.448199, 'lat': 55.765409}, 'distance': 7841, 'title': 'Cafe Antresole',
               'category': 'restaurant'},
              {'location': {'long': 38.42663, 'lat': 55.8131}, 'distance': 8303, 'title': 'Apelsin Hotel',
               'category': 'hotel'},
              {'location': {'long': 38.44765, 'lat': 55.85281}, 'distance': 9026, 'title': 'Pandora',
               'category': 'restaurant'}, {'location': {'long': 38.446185, 'lat': 55.856389}, 'distance': 9358,
                                           'title': 'Culinary Buffet Fabrika Obedov', 'category': 'restaurant'},
              {'location': {'long': 38.44152, 'lat': 55.85404}, 'distance': 9407, 'title': 'Baskin Robbins',
               'category': 'restaurant'},
              {'location': {'long': 38.65241, 'lat': 55.77954}, 'distance': 6359, 'title': 'Cafe Citi Fresh',
               'category': 'restaurant'},
              {'location': {'long': 38.44341, 'lat': 55.79054}, 'distance': 7206, 'title': 'Pechka',
               'category': 'restaurant'},
              {'location': {'long': 38.4352, 'lat': 55.77677}, 'distance': 8069, 'title': 'Quest-Cafe 4 Komnaty',
               'category': 'restaurant'},
              {'location': {'long': 38.49112, 'lat': 55.79951}, 'distance': 4146, 'title': 'Restaurant-Club AERODROM',
               'category': 'restaurant'},
              {'location': {'long': 38.61889, 'lat': 55.78323}, 'distance': 4271, 'title': 'Pekin',
               'category': 'restaurant'},
              {'location': {'long': 38.61889, 'lat': 55.78323}, 'distance': 4271, 'title': 'Vintage',
               'category': 'dance-night-club'},
              {'location': {'long': 38.61951, 'lat': 55.78277}, 'distance': 4328, 'title': 'Bierloga',
               'category': 'restaurant'},
              {'location': {'long': 38.48685, 'lat': 55.79999}, 'distance': 4412, 'title': 'Maestro',
               'category': 'restaurant'},
              {'location': {'long': 38.48639, 'lat': 55.80037}, 'distance': 4441, 'title': 'Metelitsa',
               'category': 'dance-night-club'},
              {'location': {'long': 38.47492, 'lat': 55.80763}, 'distance': 5226, 'title': 'Zamok',
               'category': 'restaurant'},
              {'location': {'long': 36.6451, 'lat': 55.83284}, 'distance': 6580, 'title': 'Satang Food Aps',
               'category': 'restaurant'},
              {'location': {'long': 36.51109, 'lat': 55.85331}, 'distance': 6594, 'title': 'Kafe',
               'category': 'restaurant'},
              {'location': {'long': 36.62443, 'lat': 55.85195}, 'distance': 7130, 'title': 'Pirogovskiy Dvorik',
               'category': 'restaurant'}]
'''
new_places = [{'location': {'long': 55.799445, 'lat': 37.55893}, 'distance': 113, 'title': 'Mnogo Lososya',
               'category': 'restaurant'},
              {'location': {'long': 55.79987, 'lat': 37.56018}, 'distance': 172, 'title': 'Bufet Cafe',
               'category': 'restaurant'},
              {'location': {'long': 55.80398, 'lat': 37.5593}, 'distance': 454, 'title': 'Pizza na Drovakh',
               'category': 'restaurant'},
              {'location': {'long': 55.793678, 'lat': 37.547039}, 'distance': 960, 'title': 'Heritage Restaurant',
               'category': 'restaurant'},
              {'location': {'long': 55.79432, 'lat': 37.5435}, 'distance': 1078, 'title': 'Sikvaruli',
               'category': 'restaurant'},
              {'location': {'long': 55.792412, 'lat': 37.569135}, 'distance': 1118, 'title': 'Izba na Maslovke',
               'category': 'restaurant'},
              {'location': {'long': 55.79994, 'lat': 37.57568}, 'distance': 1140, 'title': 'Khinkalnaya City',
               'category': 'restaurant'},
              {'location': {'long': 55.79218, 'lat': 37.56914}, 'distance': 1138, 'title': 'Pizza Presto',
               'category': 'restaurant'},
              {'location': {'long': 55.7918, 'lat': 37.54433}, 'distance': 1229, 'title': 'Ibis Moscow Dynamo Hotel',
               'category': 'hotel'},
              {'location': {'long': 55.788825, 'lat': 37.559548}, 'distance': 1253, 'title': 'Cosmic Latte',
               'category': 'restaurant'},
              {'location': {'long': 55.78798, 'lat': 37.56698}, 'distance': 1466, 'title': 'Larionov',
               'category': 'restaurant'},
              {'location': {'long': 55.78721, 'lat': 37.56633}, 'distance': 1530, 'title': 'Oriental Cocktail Bar',
               'category': 'restaurant'},
              {'location': {'long': 55.796514, 'lat': 37.581342}, 'distance': 1544, 'title': 'Factoria Beer&Grill',
               'category': 'restaurant'},
              {'location': {'long': 55.80437, 'lat': 37.58206}, 'distance': 1612, 'title': 'Tkven-Genatsvalet',
               'category': 'restaurant'},
              {'location': {'long': 55.80581, 'lat': 37.58146}, 'distance': 1633, 'title': 'AyDaBaran',
               'category': 'restaurant'},
              {'location': {'long': 55.78539, 'lat': 37.56212}, 'distance': 1654, 'title': 'Restaurant Parisienne',
               'category': 'restaurant'},
              {'location': {'long': 55.81402, 'lat': 37.56598}, 'distance': 1645, 'title': 'Pivarius',
               'category': 'restaurant'},
              {'location': {'long': 55.79947, 'lat': 37.58392}, 'distance': 1656, 'title': 'Beer Restaurant Bruder',
               'category': 'restaurant'},
              {'location': {'long': 55.785035, 'lat': 37.55782}, 'distance': 1667, 'title': 'Karaoke Club Sing',
               'category': 'restaurant'},
              {'location': {'long': 55.79719, 'lat': 37.58399}, 'distance': 1689, 'title': 'Hizhina',
               'category': 'restaurant'},
              {'location': {'long': 55.69435, 'lat': 37.55778}, 'distance': 632, 'title': "Brawler's Pub",
               'category': 'restaurant'},
              {'location': {'long': 55.704484, 'lat': 37.550777}, 'distance': 648, 'title': 'Coffee House',
               'category': 'restaurant'},
              {'location': {'long': 55.70629, 'lat': 37.56394}, 'distance': 806, 'title': 'Korston',
               'category': 'hotel'},
              {'location': {'long': 55.70603, 'lat': 37.56402}, 'distance': 784, 'title': 'Extra Lounge',
               'category': 'restaurant'},
              {'location': {'long': 55.70604, 'lat': 37.56409}, 'distance': 787, 'title': 'EVOO',
               'category': 'restaurant'},
              {'location': {'long': 55.70561, 'lat': 37.56559}, 'distance': 803, 'title': 'JU-JU Lounge & Bar',
               'category': 'restaurant'}, {'location': {'long': 55.69635, 'lat': 37.54432}, 'distance': 919,
                                           'title': 'Moscow Children’S Musical Theatre',
                                           'category': 'theatre-music-culture'},
              {'location': {'long': 55.70466, 'lat': 37.57166}, 'distance': 1029, 'title': 'Darbar',
               'category': 'restaurant'},
              {'location': {'long': 55.70512, 'lat': 37.57229}, 'distance': 1089, 'title': 'Darbars',
               'category': 'restaurant'},
              {'location': {'long': 55.70788, 'lat': 37.54491}, 'distance': 1174, 'title': 'Restaurant Tramplin',
               'category': 'restaurant'},
              {'location': {'long': 55.70789, 'lat': 37.54184}, 'distance': 1312, 'title': 'Coffee and the City',
               'category': 'coffee-tea'},
              {'location': {'long': 55.7023, 'lat': 37.57838}, 'distance': 1336, 'title': 'Petrushka',
               'category': 'restaurant'},
              {'location': {'long': 55.71137, 'lat': 37.54678}, 'distance': 1427, 'title': 'Prawns',
               'category': 'restaurant'},
              {'location': {'long': 55.70182, 'lat': 37.58069}, 'distance': 1470, 'title': 'Syncope Сoffee',
               'category': 'restaurant'},
              {'location': {'long': 55.70303, 'lat': 37.58044}, 'distance': 1479, 'title': 'Angelo',
               'category': 'restaurant'},
              {'location': {'long': 55.68891, 'lat': 37.54303}, 'distance': 1531, 'title': 'Bekers',
               'category': 'restaurant'},
              {'location': {'long': 55.690756, 'lat': 37.576049}, 'distance': 1556, 'title': 'Wine Buffet',
               'category': 'restaurant'},
              {'location': {'long': 55.68977, 'lat': 37.57572}, 'distance': 1616, 'title': 'Lustra Bar',
               'category': 'restaurant'},
              {'location': {'long': 55.68774, 'lat': 37.571551}, 'distance': 1627, 'title': 'Billy McDaniel',
               'category': 'restaurant'},
              {'location': {'long': 55.687822, 'lat': 37.572527}, 'distance': 1654, 'title': 'Pravda Coffee',
               'category': 'restaurant'},
              {'location': {'long': 55.59838, 'lat': 37.55516}, 'distance': 233, 'title': 'Karaoke Bar Mule',
               'category': 'restaurant'},
              {'location': {'long': 55.610185, 'lat': 37.537022}, 'distance': 1709, 'title': 'Territoria Yasenevo',
               'category': 'restaurant'},
              {'location': {'long': 55.61372, 'lat': 37.53875}, 'distance': 1923, 'title': 'Coffee Yest!',
               'category': 'restaurant'},
              {'location': {'long': 55.59794, 'lat': 37.52561}, 'distance': 2014, 'title': 'Yapono Italyano',
               'category': 'restaurant'},
              {'location': {'long': 55.59794, 'lat': 37.52561}, 'distance': 2014, 'title': 'Shakers',
               'category': 'restaurant'},
              {'location': {'long': 55.580041, 'lat': 37.572342}, 'distance': 2411, 'title': 'New Moscow',
               'category': 'restaurant'},
              {'location': {'long': 55.59657, 'lat': 37.51191}, 'distance': 2887, 'title': 'Artiko',
               'category': 'restaurant'},
              {'location': {'long': 55.59596, 'lat': 37.60307}, 'distance': 2902, 'title': 'Sun Sushi',
               'category': 'restaurant'},
              {'location': {'long': 55.5958, 'lat': 37.60638}, 'distance': 3110, 'title': 'Shtirbeerlits',
               'category': 'restaurant'},
              {'location': {'long': 55.6127, 'lat': 37.60487}, 'distance': 3295, 'title': 'Beans&Berries',
               'category': 'restaurant'},
              {'location': {'long': 55.61077, 'lat': 37.60669}, 'distance': 3316, 'title': 'Svarnya',
               'category': 'restaurant'},
              {'location': {'long': 55.61077, 'lat': 37.60669}, 'distance': 3316, 'title': 'Sultan Restaurant',
               'category': 'restaurant'},
              {'location': {'long': 55.6121, 'lat': 37.60697}, 'distance': 3388, 'title': 'Cutlet',
               'category': 'restaurant'},
              {'location': {'long': 55.61127, 'lat': 37.60888}, 'distance': 3464, 'title': 'Chaihona No 1',
               'category': 'restaurant'},
              {'location': {'long': 55.592902, 'lat': 37.612894}, 'distance': 3572, 'title': 'Bakery Tartin',
               'category': 'restaurant'},
              {'location': {'long': 55.617203, 'lat': 37.506677}, 'distance': 3717, 'title': 'Chocolate',
               'category': 'restaurant'}, {'location': {'long': 55.61949, 'lat': 37.50922}, 'distance': 3723,
                                           'title': 'Aleksandr Seleznev - Confectionery', 'category': 'restaurant'},
              {'location': {'long': 55.61823, 'lat': 37.50738}, 'distance': 3740, 'title': 'Coffee House',
               'category': 'coffee-tea'},
              {'location': {'long': 55.621964, 'lat': 37.605622}, 'distance': 3886, 'title': 'Cafe Chocolate',
               'category': 'restaurant'},
              {'location': {'long': 55.62508, 'lat': 37.60336}, 'distance': 4009, 'title': 'Chaihona No 1',
               'category': 'restaurant'},
              {'location': {'long': 55.79781, 'lat': 38.46511}, 'distance': 5777, 'title': 'Beer Club Tolsty Medved',
               'category': 'restaurant'},
              {'location': {'long': 55.77981, 'lat': 38.65585}, 'distance': 6550, 'title': 'Fabrika Obedov',
               'category': 'restaurant'},
              {'location': {'long': 55.776743, 'lat': 38.655801}, 'distance': 6672, 'title': 'Aristokrat',
               'category': 'hotel'},
              {'location': {'long': 55.778, 'lat': 38.44297}, 'distance': 7565, 'title': 'Fabrika Obedov',
               'category': 'restaurant'},
              {'location': {'long': 55.770561, 'lat': 38.444272}, 'distance': 7798, 'title': 'Yason',
               'category': 'restaurant'},
              {'location': {'long': 55.765409, 'lat': 38.448199}, 'distance': 7841, 'title': 'Cafe Antresole',
               'category': 'restaurant'},
              {'location': {'long': 55.8131, 'lat': 38.42663}, 'distance': 8303, 'title': 'Apelsin Hotel',
               'category': 'hotel'},
              {'location': {'long': 55.85281, 'lat': 38.44765}, 'distance': 9026, 'title': 'Pandora',
               'category': 'restaurant'}, {'location': {'long': 55.856389, 'lat': 38.446185}, 'distance': 9358,
                                           'title': 'Culinary Buffet Fabrika Obedov', 'category': 'restaurant'},
              {'location': {'long': 55.85404, 'lat': 38.44152}, 'distance': 9407, 'title': 'Baskin Robbins',
               'category': 'restaurant'},
              {'location': {'long': 55.77954, 'lat': 38.65241}, 'distance': 6359, 'title': 'Cafe Citi Fresh',
               'category': 'restaurant'},
              {'location': {'long': 55.79054, 'lat': 38.44341}, 'distance': 7206, 'title': 'Pechka',
               'category': 'restaurant'},
              {'location': {'long': 55.77677, 'lat': 38.4352}, 'distance': 8069, 'title': 'Quest-Cafe 4 Komnaty',
               'category': 'restaurant'},
              {'location': {'long': 55.79951, 'lat': 38.49112}, 'distance': 4146, 'title': 'Restaurant-Club AERODROM',
               'category': 'restaurant'},
              {'location': {'long': 55.78323, 'lat': 38.61889}, 'distance': 4271, 'title': 'Pekin',
               'category': 'restaurant'},
              {'location': {'long': 55.78323, 'lat': 38.61889}, 'distance': 4271, 'title': 'Vintage',
               'category': 'dance-night-club'},
              {'location': {'long': 55.78277, 'lat': 38.61951}, 'distance': 4328, 'title': 'Bierloga',
               'category': 'restaurant'},
              {'location': {'long': 55.79999, 'lat': 38.48685}, 'distance': 4412, 'title': 'Maestro',
               'category': 'restaurant'},
              {'location': {'long': 55.80037, 'lat': 38.48639}, 'distance': 4441, 'title': 'Metelitsa',
               'category': 'dance-night-club'},
              {'location': {'long': 55.80763, 'lat': 38.47492}, 'distance': 5226, 'title': 'Zamok',
               'category': 'restaurant'},
              {'location': {'long': 55.83284, 'lat': 36.6451}, 'distance': 6580, 'title': 'Satang Food Aps',
               'category': 'restaurant'},
              {'location': {'long': 55.85331, 'lat': 36.51109}, 'distance': 6594, 'title': 'Kafe',
               'category': 'restaurant'},
              {'location': {'long': 55.85195, 'lat': 36.62443}, 'distance': 7130, 'title': 'Pirogovskiy Dvorik',
               'category': 'restaurant'}]'''