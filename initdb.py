from app import db, Country, Hotel

db.drop_all()
db.create_all()

countries = []
countries.append(Country(
    name='UAE', 
    discription='The United Arab Emirates, sometimes simply called the Emirates, is a country in Western Asia at the northeast end of the Arabian Peninsula on the Persian Gulf, bordering Oman to the east and Saudi Arabia to the south and west, as well as sharing maritime borders with Qatar to the west and Iran to the north.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQMRaO--iQCHqOx5hH4gIz2b1TkGrCgD2g4s08mQ3xtfxWSglxz&usqp=CAU'
countries.append(Country(
    name='Egypt', 
    discription='Egypt, a country linking northeast Africa with the Middle East, dates to the time of the pharaohs. Millennia-old monuments sit along the fertile Nile River Valley, including Giza's colossal Pyramids and Great Sphinx as well as Luxor's hieroglyph-lined Karnak Temple and Valley of the Kings tombs.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRCbTPkFPwpkJHAeEwtua7gqN4lY0cMsbFAir4-JAIg1CmERlCj&usqp=CAU'
))
countries.append(Country(
    name='Turkey',
    discription='Turkey is a nation straddling eastern Europe and western Asia with cultural connections to ancient Greek, Persian, Roman, Byzantine and Ottoman empires. Cosmopolitan Istanbul, on the Bosphorus Strait, is home to the iconic Hagia Sophia, with its soaring dome and Christian mosaics, the massive 17th-century Blue Mosque and the circa-1460 Topkapı Palace, former home of sultans. Ankara is Turkey’s modern capital.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcStflr06npgZNAHchDx58j_0eu04GJQnrZm0cwHf8YqHjqwfsJy&usqp=CAU'
))

hotels = []
hotels.append(Hotel(
    name='Al Khoory Executive Hotel'
    country_id=1
    stars=3
    discription='Set in the residential Al Bada\'a neighbourhood, this chic hotel is 6 km from the Burj Khalifa skyscraper, and 6 km from The Dubai Mall shopping and recreation centre.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=20
))
hotels.append(Hotel(
    name='Ibis Al Barsha'
    country_id=1
    stars=3
    discription='Near the centre of the city, this modern hotel is a 12-minute walk from the nearest bus stop, 4 km from Ski Dubai and 6 km from the 280-metre-high Burj Al Arab.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=30
))
hotels.append(Hotel(
    name='Hyatt Place Al Rigga'
    country_id=1
    stars=4
    discription='Your Dubai adventure starts at our conveniently located hotel in Al Rigga Street. Situated right beside the Muraqqabat Mosque and near the historic Deira Clock.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=50
))
hotels.append(Hotel(
    name='Novotel Sharm El Sheikh'
    country_id=2
    stars=5
    discription='Along Naama Bay on the Red Sea, this modern hotel is 3 km from Space Sham nightclub and 11 km from Sharm El Sheikh International Airport.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=40
))
hotels.append(Hotel(
    name='Dreams Beach'
    country_id=2
    stars=5
    discription='Set along the coast of the Red Sea, this relaxed resort is 7 km from water park Cleo and 17 km from Sharm El Sheikh International Airport.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=50
))
hotels.append(Hotel(
    name='Sharm Plaza'
    country_id=2
    stars=5
    discription='Laid-back property offering direct beach access, dining & bars, plus an outdoor pool & a spa.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=60
))
hotels.append(Hotel(
    name='Sarnic Premier Hotel & SPA'
    country_id=3
    stars=5
    discription='Hotel Sarnıç Premier is a 5-minute walk from the Hagia Sophia Museum, Topkapi Palace, and the Basilica Cistern. Free parking is available at a location nearby.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=40
))
hotels.append(Hotel(
    name='Best Western Antea Palace Hotel & Spa'
    country_id=3 
    stars=5
    discription='A 15-minute walk from Basilica Cistern, this polished hotel in a stone building is 1 km from both the Grand Bazaar and Kumkapı train station.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=70
))
hotels.append(Hotel(
    name='Otantik Guesthouse'
    country_id=3
    stars=3
    discription='Guests at the bed and breakfast can enjoy a continental breakfast. A car rental service is available at Otantik Guesthouse. Basilica Cistern is a 20-minute walk from the hotel.'
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWM5hxc1uNTeqqIVKKd-_IH8H0bt8Zicsl5JL7wdXE7cD6xcaB&usqp=CAU'
    cost=25
))

for country in countries:
    db.session.add(country)

for hotel in hotels:
    db.session.add(hotel)


db.session.commit()