import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (36, 43)
L = {
 "id": "en8", "no": 8, "t": "4.2 Ravi’s Birthday", "m": [12], "ty": "Story & Activities", "th": "Our Celebrations",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 4: Our Celebrations (pages 100–107)",
 "sum": "Story “Ravi’s Birthday”: Ravi celebrated his birthday at home with his family. He wore a new dress and looked very happy. His parents decorated the house with balloons and colour papers and arranged sweets and fruits. His friends came with balloons and birthday hats and gave him a greeting card and gifts (books, pens, toys, a crayon box). Everyone sang “Happy birthday to you!”. Ravi distributed sweets and fruits; his parents blessed him; Ravi felt happy. Children learn to greet on special days, birthday words, joining sentences with ‘and’, syllables and the sounds wh and th.",
 "te": "“రవి పుట్టినరోజు” కథ – కొత్త బట్టలు, బెలూన్లతో ఇంటి అలంకరణ, స్నేహితులు గ్రీటింగ్ కార్డు, కానుకలు ఇచ్చారు, ‘Happy birthday’ పాట, రవి మిఠాయిలు పంచాడు, తల్లిదండ్రులు ఆశీర్వదించారు. ప్రత్యేక రోజుల్లో శుభాకాంక్షలు, పుట్టినరోజు పదాలు, ‘and’ తో వాక్యాలు కలపడం, syllables, wh, th శబ్దాలు.",
 "pts": [
  "1. Ravi celebrated his birthday at home with his family; he wore a new dress and looked very happy.",
  "2. His parents decorated the house with balloons and colour papers and arranged sweets and fruits.",
  "3. Friends came with balloons and birthday hats; they gave a greeting card and gifts – books, pens, toys and a crayon box.",
  "4. Everyone sang “Happy birthday to you… dear Ravi!”",
  "5. Ravi distributed sweets and fruits to his friends; his parents blessed him; Ravi felt happy.",
  "6. Sight words: was, with, they, his.",
  "7. Greetings: Happy birthday! Happy New Year! Happy Teachers’ Day! Happy Independence Day! Happy Republic Day! – Reply: Thank you!",
  "8. Birthday things: birthday hat, balloon, gift, sweets, chocolate, greeting card, candle, bouquet, fruits, decoration, biscuits, cake.",
  "9. ‘and’ joins two names/things: Ravi likes sweets and cakes. He plays cricket and chess.",
  "10. Syllables: birth-day, can-dle, bal-loon, choc-o-late. Sounds: wh – whale, wheel, whistle, where, which; th – thumb, three, thorn, thunder."],
 "w": [["birthday", "పుట్టినరోజు"], ["celebrate", "జరుపుకో"], ["decorate", "అలంకరించు"], ["balloon", "బెలూన్"], ["greeting card", "శుభాకాంక్షల కార్డు"], ["gift", "కానుక"], ["distribute", "పంచు"], ["bless", "ఆశీర్వదించు"], ["candle", "కొవ్వొత్తి"], ["bouquet", "పూలగుత్తి"], ["crayon box", "రంగు క్రేయాన్ల పెట్టె"], ["felt", "అనిపించింది"]],
 "gr": {"t": "Joining with ‘and’", "p": [
  "Ravi likes sweets. Ravi likes cakes. → Ravi likes sweets and cakes.",
  "John speaks Telugu. John speaks English. → John speaks Telugu and English.",
  "Use ‘and’ to join two persons/things/places: Ravi and his parents went to the market."]},
 "qa": [
  ["Where did Ravi celebrate his birthday?", "At home with his family."],
  ["Who decorated the house?", "His parents."],
  ["What did his friends give him?", "A greeting card and gifts – books, pens, toys and a crayon box."],
  ["What song did they sing?", "Happy birthday to you!"],
  ["What did Ravi distribute?", "Sweets and fruits."],
  ["How did Ravi feel?", "Happy."]
 ],
 "act": "Role-play a birthday party and greet ‘Happy birthday to you!’ – ‘Thank you!’. Make a birthday calendar of classmates (name, date, month). Clap syllables of birthday words. Join two sentences with ‘and’.",
 "kn": "On our birthday we can plant a sapling or share with the needy – a good way to celebrate.",
 "qz": [
  ["Whose birthday was it?", "Ravi’s", "Rani’s", "Ramu’s", "Raju’s"],
  ["Where did Ravi celebrate his birthday?", "At home", "At school", "In a hotel", "In a park"],
  ["What did Ravi wear?", "A new dress", "An old shirt", "A uniform", "A raincoat"],
  ["Who decorated the house?", "His parents", "His teacher", "His friends", "His grandfather"],
  ["They decorated with balloons and…", "colour papers", "leaves", "stones", "sand"],
  ["Friends came with balloons and…", "birthday hats", "kites", "bats", "umbrellas"],
  ["Which was NOT a gift?", "a bicycle", "books", "pens", "a crayon box"],
  ["Ravi distributed…", "sweets and fruits", "books and pens", "toys", "balloons"],
  ["Who blessed Ravi?", "His parents", "His friends", "His teacher", "The shopkeeper"],
  ["How did Ravi feel?", "happy", "sad", "angry", "heavy"],
  ["Correct spelling?", "candle", "candel", "canlde", "cnadle"],
  ["‘He plays cricket. He plays chess.’ joined:", "He plays cricket and chess.", "He plays cricket he chess.", "He plays cricket or chess.", "He cricket plays chess."],
  ["We greet on a birthday by saying…", "Happy birthday to you!", "Good night!", "Get well soon!", "Sorry!"],
  ["Reply to a greeting:", "Thank you!", "Go away!", "No!", "Why?"],
  ["Which word starts with ‘th’?", "three", "whale", "wheel", "where"],
  ["Which word starts with ‘wh’?", "whistle", "thumb", "thorn", "three"],
  ["Syllables in ‘chocolate’?", "3", "1", "2", "4"],
  ["We light ___ on a birthday cake.", "candles", "crackers", "lamps", "torches"],
  ["‘Arun eats fruits. Arun eats vegetables.’ joined:", "Arun eats fruits and vegetables.", "Arun eats fruits Arun vegetables.", "Arun and eats fruits.", "Arun fruits and eats."],
  ["Sight word in the story?", "with", "zebra", "quiz", "jump"]
 ],
 "wb": {"ws": [], "mis": ["Repeating the subject after ‘and’ (He plays cricket and he plays chess is long – say He plays cricket and chess).", "Spelling ‘candel’ – correct ‘candle’."], "qz": []},
 "tg": []
}
SEC = [
 (36, "Let us Interact (page 100)", [
  "1. I see a birthday party – a cake with candles, balloons, birthday hats, gifts, children and parents (look at the picture).",
  "2. My birthday is on ______ (own answer – date and month).",
  "3. On my birthday we buy a new dress, cake, chocolates, sweets and balloons (own answer)."]),
 (37, "Story – Ravi’s Birthday (page 101)", [
  "Read the story; sing the song ‘Happy birthday to you’. Sight words: was, with, they, his."]),
 (38, "Let us Think • New words • Greetings (page 102)", [
  "1. Ravi wore a new dress because it was his birthday.",
  "2. I say ‘Happy birthday to you!’, give a greeting card/gift and shake hands.",
  "3. My parents and grandparents (elders) bless me.",
  "4. Ravi felt very happy.",
  "New words: birthday, new, sweets, balloons, greeting card, decorate, blessed, felt.",
  "Greetings: Happy Teachers’ Day! Happy New Year! Happy Independence Day! Happy Republic Day! – Thank you!"]),
 (39, "Let us Learn A, B (page 103)", [
  "A. birthday hat, balloon, gift, sweets, chocolate, greeting card, candle, bouquet, fruits, decoration, biscuits.",
  "B. ‘and’ joins: Ravi and his parents went to the market. Ravi bought a cake and chocolates. Ravi likes sweets and cakes. He plays cricket and chess."]),
 (40, "Let us Write A, B (page 104)", [
  "A. Circle: 1. birthday cake 2. balloon 3. sweets 4. birthday hat 5. gift 6. candle 7. birthday card 8. fruits.",
  "B. 1. John speaks Telugu and English. 2. Arun eats fruits and vegetables. 3. Akhila sings rhymes and songs. 4. Nabi reads the stories and the comics."]),
 (41, "Let us Practise A, B (page 105)", [
  "A. Syllables: birth-day, can-dle, bal-loon, choc-o-late – clap for each part.",
  "B. wh – whale, wheel, whistle; th – thumb, three, thorn."]),
 (42, "Phonics C • Birthday Calendar (page 106)", [
  "C. wh – where, which; th – three, thunder (say aloud).",
  "Birthday calendar: write S.No., name, date of birth, month for family members/classmates (own answers; do not share in public)."]),
 (43, "Let us Practise – Ravi’s Birthday (page 107)", [
  "1. C) candle.",
  "2. C) happy.",
  "3. B) He plays cricket and chess.",
  "4. I greet my friend saying ‘Happy birthday to you! Many happy returns of the day!’",
  "5. Birthday cake, balloons, candles (also gifts, birthday hats).",
  "6. ‘th’ words: three, thorn (also thunder, thick)."]),
 (43, ET, edom("Role play, clapping syllables", "picture reading, birthday items, preparing a birthday calendar", "story reading, use of ‘and’, phonic drill (wh, th)", "role play, birthday song, greetings")),
]
