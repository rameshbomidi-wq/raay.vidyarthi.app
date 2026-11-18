import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (64, 72)
L = {
 "id": "en11", "no": 11, "t": "6.1 Our Fair", "m": [2], "ty": "Text & Activities", "th": "Things and Vehicles",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 6: Things and Vehicles (pages 128–136)",
 "sum": "Text “Our Fair”: Yesterday there was a fair in Rangapuram. People came from far away places. There were many shops and stalls selling sweets, clothes and toys. Children bought toys and rode on the merry-go-round; some went on the giant wheel and shouted with joy or fear. There were camel, elephant and horse rides. People had a good time and returned home after sunset. Children learn fair words, ‘was’ (singular) and ‘were’ (plural) for the past, singular–plural (car–cars), alphabetical order, syllables and the end sounds ll, ss, tt.",
 "te": "“మా జాతర (సంత)” – నిన్న రంగాపురంలో జాతర జరిగింది; దూర ప్రాంతాల నుండి ప్రజలు వచ్చారు; మిఠాయిలు, బట్టలు, బొమ్మల దుకాణాలు; రంగులరాట్నం, జెయింట్ వీల్, ఒంటె–ఏనుగు–గుర్రపు సవారీలు; సూర్యాస్తమయం తర్వాత ఇంటికి. was/were, ఏకవచనం–బహువచనం, ఆంగ్ల అక్షర క్రమం (alphabetical order), syllables, ll, ss, tt శబ్దాలు.",
 "pts": [
  "1. Yesterday there was a fair in Rangapuram; people came from far away places.",
  "2. There were many shops and stalls – sweets, clothes and toys; people were buying and selling.",
  "3. Children bought toys and went on the merry-go-round.",
  "4. Some children went on the giant wheel – some shouted with joy, others with fear.",
  "5. There were camel rides, elephant rides and horse rides; people returned home after sunset.",
  "6. Sight words: from, there, some, were.",
  "7. ‘was’ for one (singular), ‘were’ for many (plural) – for the past: There was a fair. There were many shops. He was happy. They were villagers.",
  "8. Singular – plural: This is a car. These are cars. This is a tree. These are trees. This is a cup. These are cups.",
  "9. Alphabetical order: look at the first letter and arrange A to Z (apple, boost, cake, egg…).",
  "10. Syllables: chil-dren, buy-ing, sell-ing, yes-ter-day. End sounds: ll – ball, bell, doll, well, call, tall; ss – dress, grass, mess, bless, guess, chess; tt – letter, button, kettle, bitter, better."],
 "w": [["fair", "జాతర / సంత"], ["yesterday", "నిన్న"], ["far away", "దూరంగా"], ["stall", "అంగడి"], ["buying", "కొంటూ"], ["selling", "అమ్ముతూ"], ["bought", "కొన్నారు"], ["merry-go-round", "రంగులరాట్నం"], ["giant wheel", "పెద్ద రాట్నం"], ["shouted", "అరిచారు"], ["joy", "ఆనందం"], ["fear", "భయం"], ["ride", "సవారీ"], ["sunset", "సూర్యాస్తమయం"], ["return", "తిరిగి రావు"]],
 "gr": {"t": "was / were • Alphabetical order", "p": [
  "was – one person/thing: The weather was cold. My uncle was talking.",
  "were – many: Children were buying toys. People were coming.",
  "Alphabetical order: and, buy, children, elephant, fair, good…"]},
 "qa": [
  ["Where was the fair held?", "In Rangapuram."],
  ["What were the shops selling?", "Sweets, clothes and toys."],
  ["What rides were there?", "Merry-go-round, giant wheel, camel, elephant and horse rides."],
  ["When did people return home?", "After sunset."],
  ["Use was/were: Children ___ buying toys.", "were"],
  ["Use was/were: The weather ___ cold.", "was"]
 ],
 "act": "Role-play the dialogue ‘Where did you go yesterday? – I went to a fair…’. Make a word web around ‘Fair’. Arrange classmates’ names in alphabetical order. Play the ‘Find the word’ board game in two teams.",
 "kn": "At a fair, stay with your parents, hold their hand, and remember your parents’ phone number.",
 "qz": [
  ["Where was the fair?", "Rangapuram", "Rampur", "Guntur", "Nellore"],
  ["When was the fair?", "Yesterday", "Tomorrow", "Today", "Next week"],
  ["Shops sold sweets, clothes and…", "toys", "cars", "houses", "books only"],
  ["Children went for a ride on the…", "merry-go-round", "bus", "boat", "train"],
  ["On the giant wheel some children shouted with joy and others with…", "fear", "food", "money", "sleep"],
  ["Which animal ride was NOT at the fair?", "Tiger ride", "Camel ride", "Elephant ride", "Horse ride"],
  ["People returned home after…", "sunset", "sunrise", "lunch", "breakfast"],
  ["Animal rides at a fair:", "Camel and Horse", "Dog and Cat", "Snake and Rat", "Fish and Frog"],
  ["Many trees – we say…", "These are trees.", "These are tree.", "This are trees.", "This is trees."],
  ["Word ending with ‘ss’ sound?", "chess", "call", "bitter", "ball"],
  ["Children ___ buying toys.", "were", "was", "is", "am"],
  ["The weather ___ cold yesterday.", "was", "were", "are", "am"],
  ["There ___ a big giant wheel.", "was", "were", "are", "have"],
  ["Alphabetical order of people, good, children:", "children, good, people", "good, people, children", "people, children, good", "children, people, good"],
  ["First in alphabetical order:", "and", "buy", "fair", "many"],
  ["Plural of ‘car’?", "cars", "cares", "car", "caries"],
  ["Syllables in ‘yesterday’?", "3", "1", "2", "4"],
  ["Word ending with ‘ll’?", "bell", "dress", "letter", "grass"],
  ["Word with ‘tt’?", "kettle", "doll", "mess", "tall"],
  ["Sight word:", "were", "zebra", "quiet", "jump"]
 ],
 "wb": {"ws": [], "mis": ["Using ‘was’ with plural (Children was) – correct: Children were.", "Alphabetical order by second letter instead of first."], "qz": []},
 "tg": []
}
SEC = [
 (64, "Let us Interact (page 128)", [
  "1. I see a fair – shops, stalls, giant wheel, merry-go-round, balloons, toys, people (look at the picture).",
  "2. I like the giant wheel, balloons and toys (own answer).",
  "3. Yes, I visited a fair/jatara in our village with my parents (own answer).",
  "4. I like to buy toys, balloons, bangles and sweets in a fair."]),
 (65, "Text – Our Fair (page 129)", [
  "Read the text; sight words: from, there, some, were."]),
 (66, "Let us Think • New words • Let us Speak (page 130)", [
  "1. The fair was held in Rangapuram.",
  "2. Rides: merry-go-round, giant wheel, camel ride, elephant ride, horse ride.",
  "3. I want a horse ride / camel ride / elephant ride (own answer).",
  "4. Shops selling sweets, clothes and toys.",
  "5. I buy toys, balloons and sweets at the fair.",
  "New words: yesterday, fair, far away, many, stalls, people, buying, selling, bought, giant wheel, shouted, ride, return, sunset.",
  "Let us Speak: practise the dialogue in pairs – Where did you go yesterday? I went to a fair with my parents…"]),
 (67, "Let us Learn A–C – was/were (page 131)", [
  "A. merry-go-round, toys, horse ride, camel ride (fair words).",
  "B. was – singular, were – plural (past).",
  "C. 1. There was a big giant wheel. 2. People were coming from nearby villages. 3. Children were buying toys. 4. My uncle was talking with the shopkeeper."]),
 (68, "Alphabetical order • Let us Write A (page 132)", [
  "Example order: APPLE, BOOST, CAKE, EGG, FROOTI, GUAVA, MILK.",
  "A. Words for ‘Fair’: shops, stalls, toys, sweets, balloons, giant wheel, merry-go-round, horse ride (any eight)."]),
 (69, "Let us Write B, C (page 133)", [
  "B. This is a car. These are cars. This is a tree. These are trees. This is a cup. These are cups.",
  "C. 1. and 2. buy 3. children 4. elephant 5. fair 6. good 7. many 8. people 9. shops 10. stalls 11. toys 12. wheel."]),
 (70, "Let us Practise A, B (page 134)", [
  "A. chil-dren, buy-ing, sell-ing, yes-ter-day – clap for each syllable.",
  "B. ball, bell, doll; letter, button, kettle; dress, grass."]),
 (71, "Phonics C • Language game (page 135)", [
  "C. ll – well, call, mall, tall; ss – dress, mess, bless, guess; tt – bitter, better, flatter, sitter.",
  "Game ‘Find the word’: two teams run to the board and point to the word the teacher says; the team with more points wins."]),
 (72, "Let us Practise – Our Fair (page 136)", [
  "1. C) Camel and Horse.",
  "2. B) These are trees.",
  "3. A) chess.",
  "4. a) Children were buying toys. b) The weather was cold yesterday.",
  "5. children, good, people.",
  "6. Words from a fair picture: giant wheel, balloons, toys (also merry-go-round, sweets, stalls)."]),
 (72, ET, edom("Role play, clapping syllables, language game", "things in a fair, fill in the blanks, alphabetical order", "text reading, was/were, singular–plural, phonic drill (ll, ss, tt)", "role play about visiting a fair")),
]
