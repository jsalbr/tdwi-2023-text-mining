# Dictionary with Cars and Brands
# based on https://github.com/matthlavacka/car-list

"""
with open("car-list.json", "r") as file:
    cars = json.loads(file.read())

cars2 = {}

synonyms = { 'Mercedes-Benz': 'Mercedes',
             'Volkswagen': 'VW' }

for brand_models in cars:
    brand = normalize(brand_models['brand'])
    models = [normalize(m) for m in brand_models['models']]
    # models.extend([brand+' '+model for model in models])
    cars2[brand] = models

    if brand in synonyms:
        models = brand_models['models']
        brand = synonyms[brand]
        # models.extend([brand+' '+model for model in models])
        cars2[brand] = models
cars = cars2

brands = []
models = []

for brand, brand_models in cars.items():
    brands.append(brand.lower())
    for model in brand_models:
        models.append(model.lower())

models = sorted(models)
brands = sorted(brands)
"""

cars = {
    'Alfa Romeo': ['145', '146', '147', '155', '156', '156 Sportwagon', '159', '159 Sportwagon', '164', '166', '4C', 'Brera', 'GTV', 'MiTo', 'Crosswagon', 'Spider', 'GT', 'Giulietta', 'Giulia'],
    'Audi': ['100', '100 Avant', '80', '80 Avant', '80 Cabrio', '90', 'A1', 'A2', 'A3', 'A3 Cabriolet', 'A3 Limuzina', 'A3 Sportback', 'A4', 'A4 Allroad', 'A4 Avant', 'A4 Cabriolet', 'A5', 'A5 Cabriolet', 'A5 Sportback', 'A6', 'A6 Allroad', 'A6 Avant', 'A7', 'A8', 'A8 Long', 'Q3', 'Q5', 'Q7', 'R8', 'RS4 Cabriolet', 'RS4/RS4 Avant', 'RS5', 'RS6 Avant', 'RS7', 'S3/S3 Sportback', 'S4 Cabriolet', 'S4/S4 Avant', 'S5/S5 Cabriolet', 'S6/RS6', 'S7', 'S8', 'SQ5', 'TT Coupe', 'TT Roadster', 'TTS'],
    'BMW': ['i3', 'i8', 'M3', 'M4', 'M5', 'M6', 'Rad 1', 'Rad 1 Cabrio', 'Rad 1 Coupe', 'Rad 2', 'Rad 2 Active Tourer', 'Rad 2 Coupe', 'Rad 2 Gran Tourer', 'Rad 3', 'Rad 3 Cabrio', 'Rad 3 Compact', 'Rad 3 Coupe', 'Rad 3 GT', 'Rad 3 Touring', 'Rad 4', 'Rad 4 Cabrio', 'Rad 4 Gran Coupe', 'Rad 5', 'Rad 5 GT', 'Rad 5 Touring', 'Rad 6', 'Rad 6 Cabrio', 'Rad 6 Coupe', 'Rad 6 Gran Coupe', 'Rad 7', 'Rad 8 Coupe', 'X1', 'X3', 'X4', 'X5', 'X6', 'Z3', 'Z3 Coupe', 'Z3 Roadster', 'Z4', 'Z4 Roadster'],
    'Chevrolet': ['Alero', 'Aveo', 'Camaro', 'Captiva', 'Corvette', 'Cruze', 'Cruze SW', 'Epica', 'Equinox', 'Evanda', 'HHR', 'Kalos', 'Lacetti', 'Lacetti SW', 'Lumina', 'Malibu', 'Matiz', 'Monte Carlo', 'Nubira', 'Orlando', 'Spark', 'Suburban', 'Tacuma', 'Tahoe', 'Trax'],
    'Chrysler': ['300 C', '300 C Touring', '300 M', 'Crossfire', 'Grand Voyager', 'LHS', 'Neon', 'Pacifica', 'Plymouth', 'PT Cruiser', 'Sebring', 'Sebring Convertible', 'Stratus', 'Stratus Cabrio', 'Town & Country', 'Voyager'],
    'Citroen': ['Berlingo', 'C-Crosser', 'C-Elissee', 'C-Zero', 'C1', 'C2', 'C3', 'C3 Picasso', 'C4', 'C4 Aircross', 'C4 Cactus', 'C4 Coupe', 'C4 Grand Picasso', 'C4 Sedan', 'C5', 'C5 Break', 'C5 Tourer', 'C6', 'C8', 'DS3', 'DS4', 'DS5', 'Evasion', 'Jumper', 'Jumpy', 'Saxo', 'Nemo', 'Xantia', 'Xsara'],
    'Dacia': ['Dokker', 'Duster', 'Lodgy', 'Logan', 'Logan MCV', 'Logan Van', 'Sandero', 'Solenza'],
    'Daewoo': ['Espero', 'Kalos', 'Lacetti', 'Lanos', 'Leganza', 'Lublin', 'Matiz', 'Nexia', 'Nubira', 'Nubira kombi', 'Racer', 'Tacuma', 'Tico'],
    'Dodge': ['Avenger', 'Caliber', 'Challenger', 'Charger', 'Grand Caravan', 'Journey', 'Magnum', 'Nitro', 'RAM', 'Stealth', 'Viper'],
    'Fiat': ['1100', '126', '500', '500L', '500X', '850', 'Barchetta', 'Brava', 'Cinquecento', 'Coupe', 'Croma', 'Doblo', 'Doblo Cargo', 'Doblo Cargo Combi', 'Ducato', 'Ducato Van', 'Ducato Kombi', 'Ducato Podvozok', 'Florino', 'Florino Combi', 'Freemont', 'Grande Punto', 'Idea', 'Linea', 'Marea', 'Marea Weekend', 'Multipla', 'Palio Weekend', 'Panda', 'Panda Van', 'Punto', 'Punto Cabriolet', 'Punto Evo', 'Punto Van', 'Qubo', 'Scudo', 'Scudo Van', 'Scudo Kombi', 'Sedici', 'Seicento', 'Stilo', 'Stilo Multiwagon', 'Strada', 'Talento', 'Tipo', 'Ulysse', 'Uno', 'X1/9'],
    'Ford': ['Aerostar', 'B-Max', 'C-Max', 'Cortina', 'Cougar', 'Edge', 'Escort', 'Escort Cabrio', 'Escort kombi', 'Explorer', 'F-150', 'F-250', 'Fiesta', 'Focus', 'Focus C-Max', 'Focus CC', 'Focus kombi', 'Fusion', 'Galaxy', 'Grand C-Max', 'Ka', 'Kuga', 'Maverick', 'Mondeo', 'Mondeo Combi', 'Mustang', 'Orion', 'Puma', 'Ranger', 'S-Max', 'Sierra', 'Street Ka', 'Tourneo Connect', 'Tourneo Custom', 'Transit', 'Transit', 'Transit Bus', 'Transit Connect LWB', 'Transit Courier', 'Transit Custom', 'Transit kombi', 'Transit Tourneo', 'Transit Valnik', 'Transit Van', 'Transit Van 350', 'Windstar'],
    'Honda': ['Accord', 'Accord Coupe', 'Accord Tourer', 'City', 'Civic', 'Civic Aerodeck', 'Civic Coupe', 'Civic Tourer', 'Civic Type R', 'CR-V', 'CR-X', 'CR-Z', 'FR-V', 'HR-V', 'Insight', 'Integra', 'Jazz', 'Legend', 'Prelude'],
    'Hummer': ['H2', 'H3'],
    'Hyundai': ['Accent', 'Atos', 'Atos Prime', 'Coupe', 'Elantra', 'Galloper', 'Genesis', 'Getz', 'Grandeur', 'H 350', 'H1', 'H1 Bus', 'H1 Van', 'H200', 'i10', 'i20', 'i30', 'i30 CW', 'i40', 'i40 CW', 'ix20', 'ix35', 'ix55', 'Lantra', 'Matrix', 'Santa Fe', 'Sonata', 'Terracan', 'Trajet', 'Tucson', 'Veloster'],
    'Infiniti': ['EX', 'FX', 'G', 'G Coupe', 'M', 'Q', 'QX'],
    'Jaguar': ['Daimler', 'F-Pace', 'F-Type', 'S-Type', 'Sovereign', 'X-Type', 'X-type Estate', 'XE', 'XF', 'XJ', 'XJ12', 'XJ6', 'XJ8', 'XJ8', 'XJR', 'XK', 'XK8 Convertible', 'XKR', 'XKR Convertible'],
    'Jeep': ['Cherokee', 'Commander', 'Compass', 'Grand Cherokee', 'Patriot', 'Renegade', 'Wrangler'],
    'Kia': ['Avella', 'Besta', 'Carens', 'Carnival', "Cee'd", "Cee'd SW", 'Cerato', 'K 2500', 'Magentis', 'Opirus', 'Optima', 'Picanto', 'Pregio', 'Pride', "Pro Cee'd", 'Rio', 'Rio Combi', 'Rio sedan', 'Sephia', 'Shuma', 'Sorento', 'Soul', 'Sportage', 'Venga'],
    'Land Rover': ['109', 'Defender', 'Discovery', 'Discovery Sport', 'Freelander', 'Range Rover', 'Range Rover Evoque', 'Range Rover Sport'],
    'Lexus': ['CT', 'GS', 'GS 300', 'GX', 'IS', 'IS 200', 'IS 250 C', 'IS-F', 'LS', 'LX', 'NX', 'RC F', 'RX', 'RX 300', 'RX 400h', 'RX 450h', 'SC 430'],
    'MINI': ['Cooper', 'Cooper Cabrio', 'Cooper Clubman', 'Cooper D', 'Cooper D Clubman', 'Cooper S', 'Cooper S Cabrio', 'Cooper S Clubman', 'Countryman', 'Mini One', 'One D'],
    'Mazda': ['121', '2', '3', '323', '323 Combi', '323 Coupe', '323 F', '5', '6', '6 Combi', '626', '626 Combi', 'B-Fighter', 'B2500', 'BT', 'CX-3', 'CX-5', 'CX-7', 'CX-9', 'Demio', 'MPV', 'MX-3', 'MX-5', 'MX-6', 'Premacy', 'RX-7', 'RX-8', 'Xedox 6'],
    'Mercedes': ['100 D', '115', '124', '126', '190', '190 D', '190 E', '200 - 300', '200 D', '200 E', '210 Van', '210 kombi', '310 Van', '310 kombi', '230 - 300 CE Coupé', '260 - 560 SE', '260 - 560 SEL', '500 - 600 SEC Coupé', 'Trieda A', 'A', 'A L', 'AMG GT', 'Trieda B', 'Trieda C', 'C', 'C Sportcoupé', 'C T', 'Citan', 'CL', 'CL', 'CLA', 'CLC', 'CLK Cabrio', 'CLK Coupé', 'CLS', 'Trieda E', 'E', 'E Cabrio', 'E Coupé', 'E T', 'Trieda G', 'G Cabrio', 'GL', 'GLA', 'GLC', 'GLE', 'GLK', 'Trieda M', 'MB 100', 'Trieda R', 'Trieda S', 'S', 'S Coupé', 'SL', 'SLC', 'SLK', 'SLR', 'Sprinter'],
    'Mercedes-Benz': ['100 D', '115', '124', '126', '190', '190 D', '190 E', '200 - 300', '200 D', '200 E', '210 Van', '210 kombi', '310 Van', '310 kombi', '230 - 300 CE Coupe', '260 - 560 SE', '260 - 560 SEL', '500 - 600 SEC Coupe', 'Trieda A', 'A', 'A L', 'AMG GT', 'Trieda B', 'Trieda C', 'C', 'C Sportcoupe', 'C T', 'Citan', 'CL', 'CL', 'CLA', 'CLC', 'CLK Cabrio', 'CLK Coupe', 'CLS', 'Trieda E', 'E', 'E Cabrio', 'E Coupe', 'E T', 'Trieda G', 'G Cabrio', 'GL', 'GLA', 'GLC', 'GLE', 'GLK', 'Trieda M', 'MB 100', 'Trieda R', 'Trieda S', 'S', 'S Coupe', 'SL', 'SLC', 'SLK', 'SLR', 'Sprinter'],
    'Mitsubishi': ['3000 GT', 'ASX', 'Carisma', 'Colt', 'Colt CC', 'Eclipse', 'Fuso canter', 'Galant', 'Galant Combi', 'Grandis', 'L200', 'L200 Pick up', 'L200 Pick up Allrad', 'L300', 'Lancer', 'Lancer Combi', 'Lancer Evo', 'Lancer Sportback', 'Outlander', 'Pajero', 'Pajeto Pinin', 'Pajero Pinin Wagon', 'Pajero Sport', 'Pajero Wagon', 'Space Star'],
    'Nissan': ['100 NX', '200 SX', '350 Z', '350 Z Roadster', '370 Z', 'Almera', 'Almera Tino', 'Cabstar E - T', 'Cabstar TL2 Valnik', 'e-NV200', 'GT-R', 'Insterstar', 'Juke', 'King Cab', 'Leaf', 'Maxima', 'Maxima QX', 'Micra', 'Murano', 'Navara', 'Note', 'NP300 Pickup', 'NV200', 'NV400', 'Pathfinder', 'Patrol', 'Patrol GR', 'Pickup', 'Pixo', 'Primastar', 'Primastar Combi', 'Primera', 'Primera Combi', 'Pulsar', 'Qashqai', 'Serena', 'Sunny', 'Terrano', 'Tiida', 'Trade', 'Vanette Cargo', 'X-Trail'],
    'Opel': ['Agila', 'Ampera', 'Antara', 'Astra', 'Astra cabrio', 'Astra caravan', 'Astra coupe', 'Calibra', 'Campo', 'Cascada', 'Corsa', 'Frontera', 'Insignia', 'Insignia kombi', 'Kadett', 'Meriva', 'Mokka', 'Movano', 'Omega', 'Signum', 'Vectra', 'Vectra Caravan', 'Vivaro', 'Vivaro Kombi', 'Zafira'],
    'Peugeot': ['1007', '107', '106', '108', '2008', '205', '205 Cabrio', '206', '206 CC', '206 SW', '207', '207 CC', '207 SW', '306', '307', '307 CC', '307 SW', '308', '308 CC', '308 SW', '309', '4007', '4008', '405', '406', '407', '407 SW', '5008', '508', '508 SW', '605', '806', '607', '807', 'Bipper', 'RCZ'],
    'Porsche': ['911 Carrera', '911 Carrera Cabrio', '911 Targa', '911 Turbo', '924', '944', '997', 'Boxster', 'Cayenne', 'Cayman', 'Macan', 'Panamera'],
    'Renault': ['Captur', 'Clio', 'Clio Grandtour', 'Espace', 'Express', 'Fluence', 'Grand Espace', 'Grand Modus', 'Grand Scenic', 'Kadjar', 'Kangoo', 'Kangoo Express', 'Koleos', 'Laguna', 'Laguna Grandtour', 'Latitude', 'Mascott', 'Megane', 'Megane CC', 'Megane Combi', 'Megane Grandtour', 'Megane Coupe', 'Megane Scenic', 'Scenic', 'Talisman', 'Talisman Grandtour', 'Thalia', 'Twingo', 'Wind', 'Zoe'],
    'Rover': ['200', '214', '218', '25', '400', '414', '416', '620', '75'],
    'Saab': ['9-3', '9-3 Cabriolet', '9-3 Coupe', '9-3 SportCombi', '9-5', '9-5 SportCombi', '900', '900 C', '900 C Turbo', '9000'],
    'Seat': ['Alhambra', 'Altea', 'Altea XL', 'Arosa', 'Cordoba', 'Cordoba Vario', 'Exeo', 'Ibiza', 'Ibiza ST', 'Exeo ST', 'Leon', 'Leon ST', 'Inca', 'Mii', 'Toledo'],
    'Skoda': ['Favorit', 'Felicia', 'Citigo', 'Fabia', 'Fabia Combi', 'Fabia Sedan', 'Felicia Combi', 'Octavia', 'Octavia Combi', 'Roomster', 'Yeti', 'Rapid', 'Rapid Spaceback', 'Superb', 'Superb Combi'],
    'Smart': ['Cabrio', 'City-Coupe', 'Compact Pulse', 'Forfour', 'Fortwo cabrio', 'Fortwo coupe', 'Roadster'],
    'Subaru': ['BRZ', 'Forester', 'Impreza', 'Impreza Wagon', 'Justy', 'Legacy', 'Legacy Wagon', 'Legacy Outback', 'Levorg', 'Outback', 'SVX', 'Tribeca', 'Tribeca B9', 'XV'],
    'Suzuki': ['Alto', 'Baleno', 'Baleno kombi', 'Grand Vitara', 'Grand Vitara XL-7', 'Ignis', 'Jimny', 'Kizashi', 'Liana', 'Samurai', 'Splash', 'Swift', 'SX4', 'SX4 Sedan', 'Vitara', 'Wagon R+'],
    'Tesla': ['Model S', 'Model X', 'Model Y', 'Model 3'],
    'Toyota': ['4-Runner', 'Auris', 'Avensis', 'Avensis Combi', 'Avensis Van Verso', 'Aygo', 'Camry', 'Carina', 'Celica', 'Corolla', 'Corolla Combi', 'Corolla sedan', 'Corolla Verso', 'FJ Cruiser', 'GT86', 'Hiace', 'Hiace Van', 'Highlander', 'Hilux', 'Land Cruiser', 'MR2', 'Paseo', 'Picnic', 'Prius', 'RAV4', 'Sequoia', 'Starlet', 'Supra', 'Tundra', 'Urban Cruiser', 'Verso', 'Yaris', 'Yaris Verso'],
    'VW': ['Amarok', 'Beetle', 'Bora', 'Bora Variant', 'Caddy', 'Caddy Van', 'Life', 'California', 'Caravelle', 'CC', 'Crafter', 'Crafter Van', 'Crafter Kombi', 'CrossTouran', 'Eos', 'Fox', 'Golf', 'Golf Cabrio', 'Golf Plus', 'Golf Sportvan', 'Golf Variant', 'Jetta', 'LT', 'Lupo', 'Multivan', 'New Beetle', 'New Beetle Cabrio', 'Passat', 'Passat Alltrack', 'Passat CC', 'Passat Variant', 'Passat Variant Van', 'Phaeton', 'Polo', 'Polo Van', 'Polo Variant', 'Scirocco', 'Sharan', 'T4', 'T4 Caravelle', 'T4 Multivan', 'T5', 'T5 Caravelle', 'T5 Multivan', 'T5 Transporter Shuttle', 'Tiguan', 'Touareg', 'Touran'],
    'Volkswagen': ['Amarok', 'Beetle', 'Bora', 'Bora Variant', 'Caddy', 'Caddy Van', 'Life', 'California', 'Caravelle', 'CC', 'Crafter', 'Crafter Van', 'Crafter Kombi', 'CrossTouran', 'Eos', 'Fox', 'Golf', 'Golf Cabrio', 'Golf Plus', 'Golf Sportvan', 'Golf Variant', 'Jetta', 'LT', 'Lupo', 'Multivan', 'New Beetle', 'New Beetle Cabrio', 'Passat', 'Passat Alltrack', 'Passat CC', 'Passat Variant', 'Passat Variant Van', 'Phaeton', 'Polo', 'Polo Van', 'Polo Variant', 'Scirocco', 'Sharan', 'T4', 'T4 Caravelle', 'T4 Multivan', 'T5', 'T5 Caravelle', 'T5 Multivan', 'T5 Transporter Shuttle', 'Tiguan', 'Touareg', 'Touran'],
    'Volvo': ['240', '340', '360', '460', '850', '850 kombi', 'C30', 'C70', 'C70 Cabrio', 'C70 Coupe', 'S40', 'S60', 'S70', 'S80', 'S90', 'V40', 'V50', 'V60', 'V70', 'V90', 'XC60', 'XC70', 'XC90']
}

brands = ['alfa romeo', 'audi', 'bmw', 'chevrolet', 'chrysler', 'citroen', 'dacia', 'daewoo', 'dodge', 'fiat', 'ford', 'honda', 'hummer', 'hyundai', 'infiniti', 'jaguar', 'jeep', 'kia', 'land rover', 'lexus', 'mazda', 'mercedes', 'mercedes-benz', 'mini', 'mitsubishi', 'nissan', 'opel', 'peugeot', 'porsche', 'renault', 'rover', 'saab', 'seat', 'skoda', 'smart', 'subaru', 'suzuki', 'tesla', 'toyota', 'volkswagen', 'volvo', 'vw']

models = [
    '100', '100 avant', '100 d', '100 d', '100 nx', '1007', '106', '107', '108', '109', '1100',
    '115', '115', '121', '124', '124', '126', '126', '126', '145', '146', '147', '155', '156',
    '156 sportwagon', '159', '159 sportwagon', '164', '166', '190', '190', '190 d', '190 d',
    '190 e', '190 e', '2', '200', '200 - 300', '200 - 300', '200 d', '200 d', '200 e', '200 e',
    '200 sx', '2008', '205', '205 cabrio', '206', '206 cc', '206 sw', '207', '207 cc', '207 sw',
    '210 kombi', '210 kombi', '210 van', '210 van', '214', '218', '230 - 300 ce coupe',
    '230 - 300 ce coupé', '240', '25', '260 - 560 se', '260 - 560 se', '260 - 560 sel',
    '260 - 560 sel', '3', '300 c', '300 c touring', '300 m', '3000 gt', '306', '307', '307 cc',
    '307 sw', '308', '308 cc', '308 sw', '309', '310 kombi', '310 kombi', '310 van', '310 van',
    '323', '323 combi', '323 coupe', '323 f', '340', '350 z', '350 z roadster', '360', '370 z',
    '4-runner', '400', '4007', '4008', '405', '406', '407', '407 sw', '414', '416', '460', '4c',
    '5', '500', '500 - 600 sec coupe', '500 - 600 sec coupé', '5008', '500l', '500x', '508',
    '508 sw', '6', '6 combi', '605', '607', '620', '626', '626 combi', '75', '80', '80 avant',
    '80 cabrio', '806', '807', '850', '850', '850 kombi', '9-3', '9-3 cabriolet', '9-3 coupe',
    '9-3 sportcombi', '9-5', '9-5 sportcombi', '90', '900', '900 c', '900 c turbo', '9000',
    '911 carrera', '911 carrera cabrio', '911 targa', '911 turbo', '924', '944', '997', 'a', 'a',
    'a l', 'a l', 'a1', 'a2', 'a3', 'a3 cabriolet', 'a3 limuzina', 'a3 sportback', 'a4',
    'a4 allroad', 'a4 avant', 'a4 cabriolet', 'a5', 'a5 cabriolet', 'a5 sportback', 'a6',
    'a6 allroad', 'a6 avant', 'a7', 'a8', 'a8 long', 'accent', 'accord', 'accord coupe',
    'accord tourer', 'aerostar', 'agila', 'alero', 'alhambra', 'almera', 'almera tino', 'altea',
    'altea xl', 'alto', 'amarok', 'amarok', 'amg gt', 'amg gt', 'ampera', 'antara', 'arosa',
    'astra', 'astra cabrio', 'astra caravan', 'astra coupe', 'asx', 'atos', 'atos prime', 'auris',
    'avella', 'avenger', 'avensis', 'avensis combi', 'avensis van verso', 'aveo', 'aygo',
    'b-fighter', 'b-max', 'b2500', 'baleno', 'baleno kombi', 'barchetta', 'beetle', 'beetle',
    'berlingo', 'besta', 'bipper', 'bora', 'bora', 'bora variant', 'bora variant', 'boxster',
    'brava', 'brera', 'brz', 'bt', 'c', 'c', 'c sportcoupe', 'c sportcoupé', 'c t', 'c t',
    'c-crosser', 'c-elissee', 'c-max', 'c-zero', 'c1', 'c2', 'c3', 'c3 picasso', 'c30', 'c4',
    'c4 aircross', 'c4 cactus', 'c4 coupe', 'c4 grand picasso', 'c4 sedan', 'c5', 'c5 break',
    'c5 tourer', 'c6', 'c70', 'c70 cabrio', 'c70 coupe', 'c8', 'cabrio', 'cabstar e - t',
    'cabstar tl2 valnik', 'caddy', 'caddy', 'caddy van', 'caddy van', 'caliber', 'calibra',
    'california', 'california', 'camaro', 'campo', 'camry', 'captiva', 'captur', 'caravelle',
    'caravelle', 'carens', 'carina', 'carisma', 'carnival', 'cascada', 'cayenne', 'cayman', 'cc',
    'cc', "cee'd", "cee'd sw", 'celica', 'cerato', 'challenger', 'charger', 'cherokee',
    'cinquecento', 'citan', 'citan', 'citigo', 'city', 'city-coupe', 'civic', 'civic aerodeck',
    'civic coupe', 'civic tourer', 'civic type r', 'cl', 'cl', 'cl', 'cl', 'cla', 'cla', 'clc',
    'clc', 'clio', 'clio grandtour', 'clk cabrio', 'clk cabrio', 'clk coupe', 'clk coupé', 'cls',
    'cls', 'colt', 'colt cc', 'commander', 'compact pulse', 'compass', 'cooper', 'cooper cabrio',
    'cooper clubman', 'cooper d', 'cooper d clubman', 'cooper s', 'cooper s cabrio',
    'cooper s clubman', 'cordoba', 'cordoba vario', 'corolla', 'corolla combi', 'corolla sedan',
    'corolla verso', 'corsa', 'cortina', 'corvette', 'cougar', 'countryman', 'coupe', 'coupe',
    'cr-v', 'cr-x', 'cr-z', 'crafter', 'crafter', 'crafter kombi', 'crafter kombi', 'crafter van',
    'crafter van', 'croma', 'crossfire', 'crosstouran', 'crosstouran', 'crosswagon', 'cruze',
    'cruze sw', 'ct', 'cx-3', 'cx-5', 'cx-7', 'cx-9', 'daimler', 'defender', 'demio', 'discovery',
    'discovery sport', 'doblo', 'doblo cargo', 'doblo cargo combi', 'dokker', 'ds3', 'ds4', 'ds5',
    'ducato', 'ducato kombi', 'ducato podvozok', 'ducato van', 'duster', 'e', 'e', 'e cabrio',
    'e cabrio', 'e coupe', 'e coupé', 'e t', 'e t', 'e-nv200', 'eclipse', 'edge', 'elantra', 'eos',
    'eos', 'epica', 'equinox', 'escort', 'escort cabrio', 'escort kombi', 'espace', 'espero',
    'evanda', 'evasion', 'ex', 'exeo', 'exeo st', 'explorer', 'express', 'f-150', 'f-250', 'f-pace',
    'f-type', 'fabia', 'fabia combi', 'fabia sedan', 'favorit', 'felicia', 'felicia combi',
    'fiesta', 'fj cruiser', 'florino', 'florino combi', 'fluence', 'focus', 'focus c-max',
    'focus cc', 'focus kombi', 'forester', 'forfour', 'fortwo cabrio', 'fortwo coupe', 'fox', 'fox',
    'fr-v', 'freelander', 'freemont', 'frontera', 'fusion', 'fuso canter', 'fx', 'g', 'g cabrio',
    'g cabrio', 'g coupe', 'galant', 'galant combi', 'galaxy', 'galloper', 'genesis', 'getz',
    'giulia', 'giulietta', 'gl', 'gl', 'gla', 'gla', 'glc', 'glc', 'gle', 'gle', 'glk', 'glk',
    'golf', 'golf', 'golf cabrio', 'golf cabrio', 'golf plus', 'golf plus', 'golf sportvan',
    'golf sportvan', 'golf variant', 'golf variant', 'grand c-max', 'grand caravan',
    'grand cherokee', 'grand espace', 'grand modus', 'grand scenic', 'grand vitara',
    'grand vitara xl-7', 'grand voyager', 'grande punto', 'grandeur', 'grandis', 'gs', 'gs 300',
    'gt', 'gt-r', 'gt86', 'gtv', 'gx', 'h 350', 'h1', 'h1 bus', 'h1 van', 'h2', 'h200', 'h3', 'hhr',
    'hiace', 'hiace van', 'highlander', 'hilux', 'hr-v', 'i10', 'i20', 'i3', 'i30', 'i30 cw', 'i40',
    'i40 cw', 'i8', 'ibiza', 'ibiza st', 'idea', 'ignis', 'impreza', 'impreza wagon', 'inca',
    'insight', 'insignia', 'insignia kombi', 'insterstar', 'integra', 'is', 'is 200', 'is 250 c',
    'is-f', 'ix20', 'ix35', 'ix55', 'jazz', 'jetta', 'jetta', 'jimny', 'journey', 'juke', 'jumper',
    'jumpy', 'justy', 'k 2500', 'ka', 'kadett', 'kadjar', 'kalos', 'kalos', 'kangoo',
    'kangoo express', 'king cab', 'kizashi', 'koleos', 'kuga', 'l200', 'l200 pick up',
    'l200 pick up allrad', 'l300', 'lacetti', 'lacetti', 'lacetti sw', 'laguna', 'laguna grandtour',
    'lancer', 'lancer combi', 'lancer evo', 'lancer sportback', 'land cruiser', 'lanos', 'lantra',
    'latitude', 'leaf', 'legacy', 'legacy outback', 'legacy wagon', 'leganza', 'legend', 'leon',
    'leon st', 'levorg', 'lhs', 'liana', 'life', 'life', 'linea', 'lodgy', 'logan', 'logan mcv',
    'logan van', 'ls', 'lt', 'lt', 'lublin', 'lumina', 'lupo', 'lupo', 'lx', 'm', 'm3', 'm4', 'm5',
    'm6', 'macan', 'magentis', 'magnum', 'malibu', 'marea', 'marea weekend', 'mascott', 'matiz',
    'matiz', 'matrix', 'maverick', 'maxima', 'maxima qx', 'mb 100', 'mb 100', 'megane', 'megane cc',
    'megane combi', 'megane coupe', 'megane grandtour', 'megane scenic', 'meriva', 'micra', 'mii',
    'mini one', 'mito', 'model 3', 'model s', 'model x', 'model y', 'mokka', 'mondeo',
    'mondeo combi', 'monte carlo', 'movano', 'mpv', 'mr2', 'multipla', 'multivan', 'multivan',
    'murano', 'mustang', 'mx-3', 'mx-5', 'mx-6', 'navara', 'nemo', 'neon', 'new beetle',
    'new beetle', 'new beetle cabrio', 'new beetle cabrio', 'nexia', 'nitro', 'note',
    'np300 pickup', 'nubira', 'nubira', 'nubira kombi', 'nv200', 'nv400', 'nx', 'octavia',
    'octavia combi', 'omega', 'one d', 'opirus', 'optima', 'orion', 'orlando', 'outback',
    'outlander', 'pacifica', 'pajero', 'pajero pinin wagon', 'pajero sport', 'pajero wagon',
    'pajeto pinin', 'palio weekend', 'panamera', 'panda', 'panda van', 'paseo', 'passat', 'passat',
    'passat alltrack', 'passat alltrack', 'passat cc', 'passat cc', 'passat variant',
    'passat variant', 'passat variant van', 'passat variant van', 'pathfinder', 'patriot', 'patrol',
    'patrol gr', 'phaeton', 'phaeton', 'picanto', 'pickup', 'picnic', 'pixo', 'plymouth', 'polo',
    'polo', 'polo van', 'polo van', 'polo variant', 'polo variant', 'pregio', 'prelude', 'premacy',
    'pride', 'primastar', 'primastar combi', 'primera', 'primera combi', 'prius', "pro cee'd",
    'pt cruiser', 'pulsar', 'puma', 'punto', 'punto cabriolet', 'punto evo', 'punto van', 'q', 'q3',
    'q5', 'q7', 'qashqai', 'qubo', 'qx', 'r8', 'racer', 'rad 1', 'rad 1 cabrio', 'rad 1 coupe',
    'rad 2', 'rad 2 active tourer', 'rad 2 coupe', 'rad 2 gran tourer', 'rad 3', 'rad 3 cabrio',
    'rad 3 compact', 'rad 3 coupe', 'rad 3 gt', 'rad 3 touring', 'rad 4', 'rad 4 cabrio',
    'rad 4 gran coupe', 'rad 5', 'rad 5 gt', 'rad 5 touring', 'rad 6', 'rad 6 cabrio',
    'rad 6 coupe', 'rad 6 gran coupe', 'rad 7', 'rad 8 coupe', 'ram', 'range rover',
    'range rover evoque', 'range rover sport', 'ranger', 'rapid', 'rapid spaceback', 'rav4', 'rc f',
    'rcz', 'renegade', 'rio', 'rio combi', 'rio sedan', 'roadster', 'roomster', 'rs4 cabriolet',
    'rs4/rs4 avant', 'rs5', 'rs6 avant', 'rs7', 'rx', 'rx 300', 'rx 400h', 'rx 450h', 'rx-7',
    'rx-8', 's', 's', 's coupe', 's coupé', 's-max', 's-type', 's3/s3 sportback', 's4 cabriolet',
    's4/s4 avant', 's40', 's5/s5 cabriolet', 's6/rs6', 's60', 's7', 's70', 's8', 's80', 's90',
    'samurai', 'sandero', 'santa fe', 'saxo', 'sc 430', 'scenic', 'scirocco', 'scirocco', 'scudo',
    'scudo kombi', 'scudo van', 'sebring', 'sebring convertible', 'sedici', 'seicento', 'sephia',
    'sequoia', 'serena', 'sharan', 'sharan', 'shuma', 'sierra', 'signum', 'sl', 'sl', 'slc', 'slc',
    'slk', 'slk', 'slr', 'slr', 'solenza', 'sonata', 'sorento', 'soul', 'sovereign', 'space star',
    'spark', 'spider', 'splash', 'sportage', 'sprinter', 'sprinter', 'sq5', 'starlet', 'stealth',
    'stilo', 'stilo multiwagon', 'strada', 'stratus', 'stratus cabrio', 'street ka', 'suburban',
    'sunny', 'superb', 'superb combi', 'supra', 'svx', 'swift', 'sx4', 'sx4 sedan', 't4', 't4',
    't4 caravelle', 't4 caravelle', 't4 multivan', 't4 multivan', 't5', 't5', 't5 caravelle',
    't5 caravelle', 't5 multivan', 't5 multivan', 't5 transporter shuttle',
    't5 transporter shuttle', 'tacuma', 'tacuma', 'tahoe', 'talento', 'talisman',
    'talisman grandtour', 'terracan', 'terrano', 'thalia', 'tico', 'tiguan', 'tiguan', 'tiida',
    'tipo', 'toledo', 'touareg', 'touareg', 'touran', 'touran', 'tourneo connect', 'tourneo custom',
    'town & country', 'trade', 'trajet', 'transit', 'transit', 'transit bus', 'transit connect lwb',
    'transit courier', 'transit custom', 'transit kombi', 'transit tourneo', 'transit valnik',
    'transit van', 'transit van 350', 'trax', 'tribeca', 'tribeca b9', 'trieda a', 'trieda a',
    'trieda b', 'trieda b', 'trieda c', 'trieda c', 'trieda e', 'trieda e', 'trieda g', 'trieda g',
    'trieda m', 'trieda m', 'trieda r', 'trieda r', 'trieda s', 'trieda s', 'tt coupe',
    'tt roadster', 'tts', 'tucson', 'tundra', 'twingo', 'ulysse', 'uno', 'urban cruiser', 'v40',
    'v50', 'v60', 'v70', 'v90', 'vanette cargo', 'vectra', 'vectra caravan', 'veloster', 'venga',
    'verso', 'viper', 'vitara', 'vivaro', 'vivaro kombi', 'voyager', 'wagon r+', 'wind', 'windstar',
    'wrangler', 'x-trail', 'x-type', 'x-type estate', 'x1', 'x1/9', 'x3', 'x4', 'x5', 'x6',
    'xantia', 'xc60', 'xc70', 'xc90', 'xe', 'xedox 6', 'xf', 'xj', 'xj12', 'xj6', 'xj8', 'xj8',
    'xjr', 'xk', 'xk8 convertible', 'xkr', 'xkr convertible', 'xsara', 'xv', 'yaris', 'yaris verso',
    'yeti', 'z3', 'z3 coupe', 'z3 roadster', 'z4', 'z4 roadster', 'zafira', 'zoe']
    