import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (26, 35)
L = {
 "id": "en7", "no": 7, "t": "4.1 Our Festivals", "m": [12], "ty": "Text & Activities", "th": "Our Celebrations",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 4: Our Celebrations (pages 90–99)",
 "sum": "Children talk about a Sankranthi picture and read short texts about festivals: Dussehra (ten days; the last day Vijayadasami – good wins over evil), Diwali (festival of lights – diyas, fireworks, sweets), Christmas (birth of Jesus Christ – decorated trees, gifts, carols), Sankranthi (harvest festival – kites, sweets, family gatherings; thanks nature) and Ramzan (holy month for Muslims – fasting, prayer, helping the poor – Zakat). They learn the names of the 12 months, action words (verbs), syllables (moth-er, fes-ti-val) and the sounds oo, oi, ou.",
 "te": "పండుగల గురించి చదవడం – దసరా (పది రోజులు, విజయదశమి, చెడుపై మంచి గెలుపు), దీపావళి (వెలుగుల పండుగ), క్రిస్మస్ (యేసుక్రీస్తు జన్మదినం), సంక్రాంతి (పంటల పండుగ – గాలిపటాలు), రంజాన్ (ఉపవాసం, ప్రార్థన, జకాత్). 12 నెలల పేర్లు, క్రియా పదాలు (action words), అక్షర విభజన (syllables), oo, oi, ou శబ్దాలు.",
 "pts": [
  "1. Dussehra is celebrated for ten days; the last day is Vijayadasami – good always wins over evil.",
  "2. Diwali is the festival of lights – diyas, fireworks and sweets; victory of good over evil.",
  "3. Christmas celebrates the birth of Jesus Christ – decorated trees, gifts, carols; 25th December.",
  "4. Sankranthi is a harvest festival – kites, sweets, family gatherings; thanks nature (January).",
  "5. Ramzan – holy festival of Muslims: fasting, prayer (Namaz), helping the poor (Zakat); teaches kindness and self-control.",
  "6. Holi is the festival of colours. Vinayaka Chavithi – Lord Ganesha’s festival.",
  "7. Months: January, February, March, April, May, June, July, August, September, October, November, December.",
  "8. Action words (verbs) show actions: play, bathe, do, read, come, wear, eat, grow, clean, pray, draw, sing.",
  "9. Syllables: moth-er, fa-ther, bro-ther, hap-py, fes-ti-val (clap for each part).",
  "10. Sounds: oo – tooth, roof, moon, loom, bloom, pool, cool; oi – oil, boil, soil, spoil; ou – group, route, mount, count, pound, bound."],
 "w": [["festival", "పండుగ"], ["celebrate", "జరుపుకో"], ["harvest", "పంట కోత"], ["fireworks", "బాణసంచా"], ["sweets", "మిఠాయిలు"], ["evil", "చెడు"], ["gift", "కానుక"], ["carols", "క్రిస్మస్ పాటలు"], ["fast", "ఉపవాసం"], ["pray", "ప్రార్థించు"], ["poor", "పేదలు"], ["kindness", "దయ"], ["month", "నెల"], ["diya", "దీపం (ప్రమిద)"]],
 "gr": {"t": "Action words (verbs) • Syllables", "p": [
  "Action words tell what someone does: Father reads the newspaper. We eat rice.",
  "Divide words into syllables and clap: hap-py (2), fes-ti-val (3).",
  "Months begin with capital letters: January, February…"]},
 "qa": [
  ["How many days is Dussehra celebrated?", "Ten days."],
  ["What is Diwali called?", "The festival of lights."],
  ["What does Christmas celebrate?", "The birth of Jesus Christ."],
  ["When do we fly kites?", "On Sankranthi."],
  ["What is Zakat?", "Helping the poor during Ramzan."],
  ["Which is the first month of the year?", "January."]
 ],
 "act": "Make a festival chart with pictures and names. Practise the dialogue ‘Which festival is this? – This is …’. Say the 12 months in order around the month wheel. Clap syllables of family words. Underline action words in sentences.",
 "kn": "India celebrates many festivals of different religions – we respect all and celebrate together (unity in diversity).",
 "qz": [
  ["Which festival comes on 25th December?", "Christmas", "Diwali", "Ramzan", "Sankranthi"],
  ["Which is the ‘Festival of colours’?", "Holi", "Diwali", "Christmas", "Ramzan"],
  ["We fly kites during…", "Sankranthi", "Diwali", "Christmas", "Ramzan"],
  ["Diwali is the festival of…", "lights", "kites", "colours", "harvest"],
  ["The last day of Dussehra is…", "Vijayadasami", "Bhogi", "Ugadi", "Kanuma"],
  ["Sankranthi is a … festival.", "harvest", "light", "colour", "water"],
  ["During Ramzan, Muslims…", "fast and pray", "fly kites", "burn crackers", "decorate trees"],
  ["Christmas celebrates the birth of…", "Jesus Christ", "Lord Rama", "Lord Ganesha", "Gandhiji"],
  ["Muslims offer ___ on Ramzan.", "Namaz", "carols", "kites", "crackers"],
  ["On Diwali we burn…", "crackers", "kites", "gifts", "trees"],
  ["We celebrate Sankranthi in…", "January", "December", "October", "June"],
  ["First month of the year?", "January", "March", "December", "June"],
  ["Month after March?", "April", "May", "February", "June"],
  ["Last month of the year?", "December", "November", "January", "October"],
  ["Action word in ‘Father reads the newspaper daily’?", "reads", "Father", "newspaper", "daily"],
  ["Action word in ‘Plants grow in the soil’?", "grow", "Plants", "soil", "in"],
  ["We ___ rangoli on Sankranti.", "draw", "pray", "sing", "eat"],
  ["How many syllables in ‘festival’?", "3", "1", "2", "4"],
  ["Which word has the ‘oi’ sound?", "boil", "moon", "count", "roof"],
  ["Which word has the long ‘oo’ sound?", "moon", "oil", "count", "soil"]
 ],
 "wb": {"ws": [], "mis": ["Writing month names with small letters (january) – use capital letters.", "Mixing ‘Festival of lights’ (Diwali) and ‘Festival of colours’ (Holi)."], "qz": []},
 "tg": []
}
SEC = [
 (26, "Let us Interact (page 90)", [
  "1. Things: kites, sugarcane, rangoli (muggu), pots with pongal, gobbemmalu, children, family (look at the picture).",
  "2. Sankranthi is being celebrated.",
  "3. Yes. We draw rangoli, fly kites, wear new clothes, make sweets and visit relatives (own answer).",
  "4. Diwali, Dussehra, Ugadi, Vinayaka Chavithi, Ramzan, Christmas."]),
 (27, "Text – Our Festivals (page 91)", [
  "Read about Dussehra, Diwali, Christmas, Sankranthi and Ramzan; listen and read on your own."]),
 (28, "New words • Let us Think • Let us Speak (page 92)", [
  "New words: Sankranthi, Ramzan, Festivals, Diwali, Dussehra, Christmas.",
  "1. Festival names in the text: Dussehra (Vijayadasami), Diwali, Christmas, Sankranthi, Ramzan.",
  "2. On Diwali I light diyas, wear new clothes, eat sweets and burn crackers safely with elders.",
  "3. We fly kites on Sankranthi.",
  "4. On a festival day I wake up early, take a bath, wear new clothes, pray, eat sweets and play with family.",
  "5. The birth of Jesus Christ is celebrated on Christmas.",
  "Let us Speak: ‘Which festival is this?’ – ‘This is Sankranthi.’ (practise in pairs)."]),
 (29, "Speak with pictures • Let us Learn A (page 93)", [
  "Practise the dialogue with each picture: Which festival is this? – This is Vinayaka Chavithi / Ramzan / Christmas / Diwali / Dussehra.",
  "A. Read aloud: Sankranthi, Vinayaka chavithi, Ramzan, Christmas, Diwali, Dussehra."]),
 (30, "Months • Action words (page 94)", [
  "B. Months in order: January, February, March, April, May, June, July, August, September, October, November, December.",
  "C. Action words: 1. reads 2. came 3. wears 4. eat 5. grow."]),
 (31, "Let us Write A, B (page 95)", [
  "A. 1. Sankranthi is the festival of harvest. 2. Muslims offer Namaz on Ramzan. 3. Christmas falls on 25th December. 4. On Diwali we burn crackers. 5. We celebrate Sankranthi in January.",
  "B. 1. January 2. February 3. March 4. April 5. May 6. June 7. July 8. August 9. September 10. October 11. November 12. December."]),
 (32, "Let us Write C • Syllables (page 96)", [
  "C. 1. Ramu and Geetha pray to God on the festival day. 2. Anitha and Mamatha draw rangoli on Sankranti. 3. They clean the house. 4. We eat sweets. 5. They sing songs.",
  "Syllables: moth-er, fa-ther, bro-ther, hap-py, fes-ti-val – clap for each syllable."]),
 (33, "Phonics – oo, oi, ou (page 97)", [
  "B. tooth, roof, moon; oil, boil; group, route, wound.",
  "C. oo – loom, bloom, pool, cool; oi – oil, boil, soil, spoil; ou – mount, count, pound, bound. Say aloud and repeat."]),
 (34, "Let us Do (page 98)", [
  "Colour and write: kite → Sankranthi; Christmas tree → Christmas; boy praying (crescent moon) → Ramzan; rangoli/muggu → Sankranthi (or Diwali). (Look at the pictures.)"]),
 (35, "Let us Practise – Our Festivals (page 99)", [
  "1. B) Christmas.",
  "2. A) Holi.",
  "3. B) Sankranthi.",
  "4. Write the festival name under each picture (e.g., Diwali / Christmas / Ramzan – check with the pictures).",
  "5. January, February, March.",
  "6. We draw rangoli on Sankranti."]),
 (35, ET, edom("Role play, colouring pictures, clapping syllables", "festival names, months of the year, action words, fill in the blanks", "story reading, syllable drill, phonic drill (oo, oi, ou)", "role play, colouring festival pictures, learning about our festivals")),
]
