import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (55, 63)
L = {
 "id": "en10", "no": 10, "t": "5.2 Our Helpers", "m": [1], "ty": "Rhyme & Activities", "th": "Our Community and People",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 5: Our Community and People (pages 119–127)",
 "sum": "Rhyme “Bang and a bang!” – a cobbler down the street mends shoes for little feet the whole day long to make them strong, with a bang, bang, bang. Children learn about community helpers: the potter makes pots, the barber trims hair, the washerman washes clothes, the cobbler mends shoes, the carpenter makes furniture, the tailor stitches clothes, the fisherwoman catches fish. They use the pronouns he/she, make profession words with -er and -man (driver, teacher, farmer, milkman, postman, fireman), make small words from ‘washerwoman’, clap syllables and practise the blends gl and sl.",
 "te": "“Bang and a bang!” రైమ్ – వీధిలో చెప్పులు కుట్టే వ్యక్తి (చెప్పుల మేస్త్రి) రోజంతా పిల్లల బూట్లు బాగుచేస్తాడు. మనకు సహాయం చేసేవారు – కుమ్మరి, మంగలి, చాకలి, చెప్పులు కుట్టేవారు, వడ్రంగి, దర్జీ, జాలరి. He/She సర్వనామాలు, -er, -man తో వృత్తి పేర్లు, ‘washerwoman’ నుండి పదాలు, syllables, gl, sl శబ్దాలు.",
 "pts": [
  "1. Rhyme: A cobbler down the street mends shoes for little feet the whole day long, to make them strong – with a bang, and a bang, bang, bang.",
  "2. He makes pots – he is a potter. He trims hair – he is a barber. He washes clothes – he is a washerman.",
  "3. She mends shoes – she is a cobbler. He makes furniture – he is a carpenter. She stitches clothes – she is a tailor. She catches fish – she is a fisherwoman.",
  "4. ‘He’ for a man/boy, ‘she’ for a woman/girl (pronouns): Ramaiah trims hair. He is a barber. Sitamma catches fish. She is a fisherwoman.",
  "5. -er words: driver, teacher, farmer, painter, potter, weaver, barber.",
  "6. -man words: milkman, postman, fireman, fisherman, washerman, watchman.",
  "7. Words from ‘washerwoman’: wash, she, her, woman, wear, show, hear, when, how, an, on, was, as, so, are, we, new.",
  "8. Syllables: pot-ter, bar-ber, cob-bler, tai-lor, tea-cher, car-pen-ter.",
  "9. Blends: gl – glue, globe, glass, glove, glad, glide; sl – slide, slate, sleep, slice, slow, slipper, slope.",
  "10. All helpers are important – we should respect them and say ‘thank you’."],
 "w": [["helper", "సహాయకుడు"], ["cobbler", "చెప్పులు కుట్టే వ్యక్తి"], ["mend", "బాగుచేయు"], ["potter", "కుమ్మరి"], ["barber", "మంగలి"], ["washerman", "చాకలి"], ["carpenter", "వడ్రంగి"], ["tailor", "దర్జీ"], ["fisherwoman", "జాలరి స్త్రీ"], ["furniture", "కుర్చీలు, బల్లలు"], ["stitch", "కుట్టు"], ["profession", "వృత్తి"], ["whole day", "రోజంతా"]],
 "gr": {"t": "Pronouns he/she • -er/-man words", "p": [
  "Ramu makes pots. He is a potter. Sarala stitches clothes. She is a tailor.",
  "drive → driver, teach → teacher, farm → farmer.",
  "milk → milkman, post → postman, fire → fireman, watch → watchman."]},
 "qa": [
  ["Who is mending shoes in the rhyme?", "The cobbler."],
  ["What does a potter make?", "Pots."],
  ["Who trims hair?", "The barber."],
  ["Who makes furniture?", "The carpenter."],
  ["Who stitches clothes?", "The tailor."],
  ["Which pronoun is used for a woman?", "She."]
 ],
 "act": "Recite the rhyme with hammering actions. Play the flashcard ball game – ‘He is a potter. He makes pots.’ Act out a profession and let others guess. Make words from ‘washerwoman’. Thank a helper in your village.",
 "kn": "Every job is important. Farmers give food, doctors heal, teachers teach, cleaners keep our streets clean.",
 "qz": [
  ["Who mends shoes in the rhyme?", "The cobbler", "The potter", "The tailor", "The barber"],
  ["The cobbler mends shoes for…", "little feet", "big hands", "old books", "new pots"],
  ["The cobbler mends shoes…", "the whole day long", "only at night", "once a year", "never"],
  ["Akbar makes pots. ___ is a potter.", "He", "She", "They", "It"],
  ["Raju trims hair in a shop. He is a…", "barber", "potter", "carpenter", "tailor"],
  ["A man making a table/chair is a…", "carpenter", "tailor", "potter", "barber"],
  ["She stitches clothes. She is a…", "tailor", "cobbler", "potter", "fisherwoman"],
  ["She catches fish. She is a…", "fisherwoman", "tailor", "barber", "washerwoman"],
  ["He washes clothes. He is a…", "washerman", "milkman", "postman", "fireman"],
  ["Missing letters: c_bbl_r", "cobbler", "cabbler", "cobblar", "cubbler"],
  ["farm + er =", "farmer", "farmman", "farmor", "farmar"],
  ["watch + man =", "watchman", "watcher", "watchar", "watchmen"],
  ["Who brings letters?", "postman", "fireman", "milkman", "watchman"],
  ["Match: Potter –", "makes pots", "catches fish", "stitches clothes", "trims hair"],
  ["Match: Tailor –", "stitches clothes", "makes pots", "catches fish", "mends shoes"],
  ["Letters 1,2,3,4 of ‘washerwoman’ =", "wash", "she", "her", "woman"],
  ["Syllables in ‘carpenter’?", "3", "1", "2", "4"],
  ["Which word begins with ‘gl’?", "globe", "slide", "slate", "sleep"],
  ["Which word begins with ‘sl’?", "slipper", "glass", "glue", "glove"],
  ["Sarala stitches clothes. ___ is a tailor.", "She", "He", "It", "They"]
 ],
 "wb": {"ws": [], "mis": ["Using ‘He’ for a woman or ‘She’ for a man.", "Spelling ‘tailar’ / ‘carpanter’ – correct: tailor, carpenter."], "qz": []},
 "tg": []
}
SEC = [
 (55, "Let us Interact (page 119)", [
  "1. I see many helpers working (look at the picture).",
  "2. They are a potter, barber, washerman, cobbler, carpenter, tailor, fisherwoman, farmer, doctor, postman (as in the picture).",
  "3. They are making pots, cutting hair, washing clothes, mending shoes, making furniture, stitching clothes, catching fish.",
  "4. They help us by giving services – clothes, shoes, food, furniture, health, letters.",
  "5. Yes, there are many such helpers in my village (own answer)."]),
 (56, "Rhyme – Bang and a bang! • Let us Think (page 120)", [
  "Recite with hammering actions.",
  "1. The man in the picture is a cobbler.",
  "2. The cobbler is mending shoes.",
  "3. I go to the cobbler down the street to repair my shoes.",
  "4. Yes, I wear shoes regularly to school (own answer).",
  "New words: cobbler, street, mending, bang, whole."]),
 (57, "Helpers and their work (page 121)", [
  "He makes pots – potter; he trims hair – barber; he washes clothes – washerman; she mends shoes – cobbler; he makes furniture – carpenter; she stitches clothes – tailor; she catches fish – fisherwoman."]),
 (58, "Let us Learn A–C (page 122)", [
  "A. tailor, carpenter, potter.",
  "B. This is Ramaiah. He trims hair. He is a barber. This is Sitamma. She catches fish. She is a fisherwoman. (he/she are pronouns)",
  "C. 1. He 2. She 3. She 4. He 5. He."]),
 (59, "Let us Speak • Let us Write A, B (page 123)", [
  "Let us Speak: He is a potter. He makes pots. (Speak about the helper on your flashcard.)",
  "A. potter, tailor, carpenter, Cobbler, fisherwoman, Barber.",
  "B. -er: 1. driver 2. teacher 3. farmer 4. painter 5. potter 6. weaver 7. barber.",
  "-man: 1. milkman 2. postman 3. fireman 4. fisherman 5. washerman 6. watchman."]),
 (60, "Let us Write C, D (page 124)", [
  "C. 1,2,3,4 = wash; 3,4,5 = she; 4,5,6 = her; 7,8,9,10,11 = woman; 1,5,2,6 = wear; 3,4,8,1 = show; 4,2,6,5 = hare; 4,5,2,6 = hear; 1,4,5,11 = when.",
  "4,8,7 = how; 10,11 = an; 8,11 = on; 1,2,3 = was; 2,3 = as; 3,8 = so; 2,6,5 = are; 1,5 = we; 11,5,1 = new.",
  "D. Somaiah is making pots. He is a potter. Rajini is washing clothes. She is a washerwoman. Ganapathi is trimming hair. He is a barber. Rani is mending shoes. She is a cobbler. Kamala is stitching clothes. She is a tailor."]),
 (61, "Let us Practise A, B (page 125)", [
  "A. pot-ter, bar-ber, cob-bler, tai-lor, tea-cher, car-pen-ter.",
  "B. gl – glue, globe, glass; sl – slide, slate, sleep."]),
 (62, "Phonics • Language game (page 126)", [
  "gl – glove, globe, glad, glide; sl – slice, slow, slipper, slope.",
  "Game: pick a profession card, act it out without speaking; others guess (e.g., potter – shaping pots on a wheel)."]),
 (63, "Let us Practise – Our Helpers (page 127)", [
  "1. B) He.",
  "2. C) He is a carpenter. (picture – check)",
  "3. B) Barber.",
  "4. cobbler.",
  "5. 1) farmer 2) watchman.",
  "6. i) Potter – c) makes pot; ii) Fisherwoman – a) catches fish; iii) Tailor – b) stitches clothes."]),
 (63, ET, edom("Reciting the rhyme with actions, role play, language game", "identify professions, fill in the blanks, matching, making words", "rhyme, pronouns he/she, phonic drill (gl, sl)", "reciting in rhythm, role play, respecting helpers")),
]
