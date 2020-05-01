from app import db, Country, Hotel

db.drop_all()
db.create_all()

countries = []
countries.append(Country(
    name='UAE', 
    description='The United Arab Emirates, sometimes simply called the Emirates, is a country in Western Asia at the northeast end of the Arabian Peninsula on the Persian Gulf, bordering Oman to the east and Saudi Arabia to the south and west, as well as sharing maritime borders with Qatar to the west and Iran to the north.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQMRaO--iQCHqOx5hH4gIz2b1TkGrCgD2g4s08mQ3xtfxWSglxz&usqp=CAU'
))
countries.append(Country(
    name='Egypt', 
    description='Egypt, a country linking northeast Africa with the Middle East, dates to the time of the pharaohs. Millennia-old monuments sit along the fertile Nile River Valley, including Giza\'s colossal Pyramids and Great Sphinx as well as Luxor\'s hieroglyph-lined Karnak Temple and Valley of the Kings tombs.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRCbTPkFPwpkJHAeEwtua7gqN4lY0cMsbFAir4-JAIg1CmERlCj&usqp=CAU'
))
countries.append(Country(
    name='Turkey',
    description='Turkey is a nation straddling eastern Europe and western Asia with cultural connections to ancient Greek, Persian, Roman, Byzantine and Ottoman empires. Cosmopolitan Istanbul, on the Bosphorus Strait, is home to the iconic Hagia Sophia, with its soaring dome and Christian mosaics, the massive 17th-century Blue Mosque and the circa-1460 Topkapı Palace, former home of sultans. Ankara is Turkey’s modern capital.',
    photo='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcStflr06npgZNAHchDx58j_0eu04GJQnrZm0cwHf8YqHjqwfsJy&usqp=CAU'
))

hotels = []
hotels.append(Hotel(
    name='Al Khoory Executive Hotel', 
    country_id=1, 
    stars=3,
    description='Set in the residential Al Bada\'a neighbourhood, this chic hotel is 6 km from the Burj Khalifa skyscraper, and 6 km from The Dubai Mall shopping and recreation centre.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/446/44618414.jpg',
    booking_page='https://www.booking.com/hotel/ae/corp-executive-al-khoory.en-gb.html?aid=356938;label=metagha-link-localuniversalKZ-hotel-428990_dev-desktop_los-1_bw-1_dow-Saturday_defdate-1_room-0_lang-en_curr-KZT_gstadt-2_rateid-0_aud-102524574_cid-_gacid-6641364928_mcid-10;sid=efe0d923850e8571bdb60e00f4fdb7ae;all_sr_blocks=42899001_88789688_0_42_0;checkin=2020-05-02;checkout=2020-05-03;dest_id=-782831;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=42899001_88789688_0_42_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=42899001_88789688_0_42_0__10800;srepoch=1588336528;srpvid=0d9f58876b7800e6;type=total;ucfs=1&#hotelTmpl'
))
hotels.append(Hotel(
    name='Ibis Al Barsha',
    country_id=1,
    stars=3,
    description='Near the centre of the city, this modern hotel is a 12-minute walk from the nearest bus stop, 4 km from Ski Dubai and 6 km from the 280-metre-high Burj Al Arab.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/454/45414490.jpg',
    booking_page='https://www.booking.com/hotel/ae/ibis-al-barsha.en-gb.html?aid=356938;label=metagha-link-localuniversalKZ-hotel-48016_dev-desktop_los-1_bw-17_dow-Monday_defdate-1_room-0_lang-en_curr-KZT_gstadt-2_rateid-0_aud-102524574_cid-_gacid-6641364928_mcid-10;sid=efe0d923850e8571bdb60e00f4fdb7ae;all_sr_blocks=4801601_94270347_2_42_0;checkin=2020-05-18;checkout=2020-05-19;dest_id=-782831;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=4801601_94270347_2_42_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=4801601_94270347_2_42_0__10710;srepoch=1588347838;srpvid=f8d76e9ed6c50066;type=total;ucfs=1&#hotelTmpl'
))
hotels.append(Hotel(
    name='Hyatt Place Al Rigga',
    country_id=1,
    stars=4,
    description='Your Dubai adventure starts at our conveniently located hotel in Al Rigga Street. Situated right beside the Muraqqabat Mosque and near the historic Deira Clock.',
    photo='https://r-cf.bstatic.com/images/hotel/max1024x768/209/209989756.jpg',
    booking_page='https://www.booking.com/hotel/ae/hyatt-place-dubai-al-rigga.en-gb.html?aid=356980;label=gog235jc-1DCAsoAkIaaHlhdHQtcGxhY2UtZHViYWktYWwtcmlnZ2FIM1gDaIABiAEBmAEJuAEZyAEP2AED6AEBiAIBqAIDuAKYiLH1BcACAQ;sid=efe0d923850e8571bdb60e00f4fdb7ae;dist=0&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&'
))
hotels.append(Hotel(
    name='Novotel Sharm El Sheikh',
    country_id=2,
    stars=5,
    description='Along Naama Bay on the Red Sea, this modern hotel is 3 km from Space Sham nightclub and 11 km from Sharm El Sheikh International Airport.',
    photo='https://r-cf.bstatic.com/images/hotel/max1024x768/135/13525148.jpg',
    booking_page='https://www.booking.com/hotel/eg/novotel-sharm-el-sheikh.en-gb.html?aid=356980;label=gog235jc-1DCAsoQ0IXbm92b3RlbC1zaGFybS1lbC1zaGVpa2hIM1gDaIABiAEBmAEJuAEZyAEP2AED6AEBiAIBqAIDuALtiLH1BcACAQ;sid=efe0d923850e8571bdb60e00f4fdb7ae;dist=0&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&'
))
hotels.append(Hotel(
    name='Dreams Beach',
    country_id=2,
    stars=5,
    description='Set along the coast of the Red Sea, this relaxed resort is 7 km from water park Cleo and 17 km from Sharm El Sheikh International Airport.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/159/15953631.jpg',
    booking_page='https://www.booking.com/hotel/eg/dreams-beach-resort.en-gb.html?aid=311984;label=dreams-beach-resort-49nrv0w8H_2fnkGQ6sUA8gS354672583377%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-285284111406%3Akwd-294867758%3Alp9063099%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YTQUGSsRwx9_3qo3uPTHyoo;sid=efe0d923850e8571bdb60e00f4fdb7ae;all_sr_blocks=32769501_116261202_0_1_0;checkin=2020-05-18;checkout=2020-05-19;dest_id=-302053;dest_type=city;dist=0;from_beach_non_key_ufi_sr=1;group_adults=2;group_children=0;hapos=1;highlighted_blocks=32769501_116261202_0_1_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=32769501_116261202_0_1_0__11157;srepoch=1588348141;srpvid=9f9b6f35029f0067;type=total;ucfs=1&#hotelTmpl'
))
hotels.append(Hotel(
    name='Sharm Grand Plaza',
    country_id=2,
    stars=5,
    description='Laid-back property offering direct beach access, dining & bars, plus an outdoor pool & a spa.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/134/134721758.jpg',
    booking_page='https://www.booking.com/hotel/eg/sharm-grand-plaza-resort.ru.html'
))
hotels.append(Hotel(
    name='Sarnic Premier Hotel & SPA',
    country_id=3,
    stars=5,
    description='Hotel Sarnıç Premier is a 5-minute walk from the Hagia Sophia Museum, Topkapi Palace, and the Basilica Cistern. Free parking is available at a location nearby.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/377/37724379.jpg',
    booking_page='https://www.booking.com/hotel/tr/sarnic-premier.ru.html?aid=318615;label=New_English_EN_ALL-GBIECAUS_5226333385-zrfE0CU6K_HWeoloJw%2APrQS217244291991%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg;sid=efe0d923850e8571bdb60e00f4fdb7ae;all_sr_blocks=29645106_185933098_2_41_0;checkin=2020-05-18;checkout=2020-05-19;dest_id=-755070;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=29645106_185933098_2_41_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=29645106_185933098_2_41_0__7224;srepoch=1588348951;srpvid=a92070ca531600aa;type=total;ucfs=1&#hotelTmpl'
))
hotels.append(Hotel(
    name='Best Western Antea Palace Hotel & Spa',
    country_id=3,
    stars=5,
    description='A 15-minute walk from Basilica Cistern, this polished hotel in a stone building is 1 km from both the Grand Bazaar and Kumkapı train station.',
    photo='https://q-cf.bstatic.com/images/hotel/max1024x768/157/157386198.jpg',
    booking_page='https://www.booking.com/hotel/tr/best-western-anteapalace.ru.html?aid=356980;label=gog235jc-1DCAso5AFCGGJlc3Qtd2VzdGVybi1hbnRlYXBhbGFjZUgzWANogAGIAQGYASG4ARnIAQ_YAQPoAQGIAgGoAgO4AsuRsfUFwAIB;sid=efe0d923850e8571bdb60e00f4fdb7ae;dist=0&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&'
))
hotels.append(Hotel(
    name='Otantik Guesthouse',
    country_id=3,
    stars=2,
    description='Guests at the bed and breakfast can enjoy a continental breakfast. A car rental service is available at Otantik Guesthouse. Basilica Cistern is a 20-minute walk from the hotel.',
    photo='https://r-cf.bstatic.com/images/hotel/max1024x768/228/228234876.jpg',
    booking_page='https://www.booking.com/hotel/tr/otantik-guesthouse.en-gb.html?aid=311984;label=otantik-guesthouse-P%2AkPMAlXwaV8t6GFcjzHcQS261014928423%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-285284111406%3Akwd-142160930486%3Alp9063099%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXwxhKG0pUU-mcMVT-JwQpc;sid=efe0d923850e8571bdb60e00f4fdb7ae;all_sr_blocks=167306806_124514907_2_1_0;checkin=2020-05-18;checkout=2020-05-19;dest_id=-755070;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=167306806_124514907_2_1_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=167306806_124514907_2_1_0__3614;srepoch=1588349243;srpvid=f78a715c99040017;type=total;ucfs=1&#hotelTmpl'
))

for country in countries:
    db.session.add(country)

for hotel in hotels:
    db.session.add(hotel)


db.session.commit()