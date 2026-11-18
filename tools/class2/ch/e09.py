import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (44, 54)
L = {
 "id": "en9", "no": 9, "t": "5.1 My Grandpa’s Village", "m": [12], "ty": "Story & Activities", "th": "Our Community and People",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 5: Our Community and People (pages 108–118)",
 "sum": "Story “My Grandpa’s Village”: Sameera loves to visit her grandpa’s village. It is small and beautiful, near a river, with big coconut and banyan trees; she plays with her friends under the banyan tree. The village has a school, a hospital, a post office, a bank and a Grama Sachivalayam. Every house has a small garden; there are cows and goats; the air is fresh and the streets are clean; the people are kind and happy. Children learn names of places (‘What is this? – This is a post office.’), ‘I like to…’, describing words/adjectives and opposites (tall–short, fat–thin, big–small, clean–dirty), syllables and the blends bl, cl, fl.",
 "te": "“తాతయ్య గ్రామం” కథ – సమీర తాతయ్య ఊరు చిన్నది, అందమైనది, నది దగ్గర; కొబ్బరి, మర్రి చెట్లు; బడి, ఆసుపత్రి, పోస్టాఫీసు, బ్యాంకు, గ్రామ సచివాలయం; పరిశుభ్రమైన వీధులు, మంచి ప్రజలు. ప్రదేశాల పేర్లు, ‘I like to…’, విశేషణాలు, వ్యతిరేక పదాలు (tall–short…), syllables, bl, cl, fl శబ్దాలు.",
 "pts": [
  "1. Sameera loves to visit her grandpa’s village – small and beautiful, near a river.",
  "2. There are big coconut and banyan trees; she plays with her friends under the banyan tree.",
  "3. The village has a school, a hospital, a post office, a bank and a Grama Sachivalayam.",
  "4. Every house has a small garden; there are cows and goats; the air is fresh and the streets are clean.",
  "5. The villagers do different works; the people are kind and happy.",
  "6. Places: post office, bus stop, school, hospital, railway station, bank, market, park, village.",
  "7. ‘I like to…’: I like to visit my grandpa’s village. I like to go to the beach / market / park.",
  "8. Describing words (adjectives): tall, short, fat, thin, big, small, clean, dirty, good, smart, clever, beautiful.",
  "9. Opposites: tall × short, fat × thin, big × small, clean × dirty, hot × cold.",
  "10. Syllables: vil-lage, peo-ple, vis-it, hos-pi-tal, beau-ti-ful. Blends: bl – black, blue, blow, block, blood; cl – clap, class, close, clean, click; fl – flag, flower, flow, fly, flat."],
 "w": [["village", "గ్రామం"], ["river", "నది"], ["banyan tree", "మర్రిచెట్టు"], ["street", "వీధి"], ["villagers", "గ్రామస్థులు"], ["post office", "తపాలా కార్యాలయం"], ["hospital", "ఆసుపత్రి"], ["railway station", "రైల్వే స్టేషన్"], ["fresh", "తాజా"], ["clean", "శుభ్రమైన"], ["dirty", "మురికి"], ["kind", "దయగల"], ["friendly", "స్నేహపూర్వక"], ["calf", "దూడ"]],
 "gr": {"t": "Adjectives (describing words) & Opposites", "p": [
  "Adjectives describe a person, place or thing: A tall tree. A fat cat. A clean street.",
  "Opposites: tall – short, fat – thin, big – small, clean – dirty.",
  "I like to + action: I like to go to the park."]},
 "qa": [
  ["Whose village does Sameera visit?", "Her grandpa’s village."],
  ["Where is the village?", "Near a river."],
  ["Where does Sameera play?", "Under the banyan tree with her friends."],
  ["Name some places in the village.", "School, hospital, post office, bank, Grama Sachivalayam."],
  ["How is the air in the village?", "Fresh."],
  ["Opposite of ‘tall’?", "short."]
 ],
 "act": "Draw a map of your village with school, hospital, post office, bank. Play the opposite-word card game in a circle. Say ‘I like to go to…’ one by one. Clap syllables of village words.",
 "kn": "Grama Sachivalayam (village secretariat) provides government services to people in the village.",
 "qz": [
  ["Who loves to visit grandpa’s village?", "Sameera", "Rani", "Ravi", "Mary"],
  ["The village is near a…", "river", "sea", "mountain", "desert"],
  ["Sameera plays under the…", "banyan tree", "mango tree", "coconut tree", "neem tree"],
  ["Which is NOT in the village (story)?", "an airport", "a school", "a post office", "a bank"],
  ["The air in the village is…", "fresh", "dirty", "smoky", "hot"],
  ["The streets are…", "clean", "dirty", "broken", "dark"],
  ["The people are…", "kind and happy", "angry", "lazy", "sad"],
  ["Keeping surroundings clean makes them…", "beautiful", "dirty", "ugly", "smelly"],
  ["Friend has stomach pain. Take him to…", "Hospital", "Post office", "Bank", "Market"],
  ["An elephant is a ___ animal.", "big", "small", "thin", "short"],
  ["Opposite of ‘tall’?", "short", "big", "fat", "thin"],
  ["Opposite of ‘thin’?", "fat", "tall", "short", "small"],
  ["Opposite of ‘clean’?", "dirty", "fresh", "big", "good"],
  ["Adjective in ‘The fat cat is sleeping’?", "fat", "cat", "sleeping", "is"],
  ["Adjective in ‘The sun is hot today’?", "hot", "sun", "today", "is"],
  ["Where do we post letters?", "Post office", "Hospital", "School", "Bank"],
  ["Syllables in ‘hospital’?", "3", "1", "2", "4"],
  ["Which word begins with ‘fl’?", "flag", "black", "clap", "blue"],
  ["Which word begins with ‘cl’?", "class", "flow", "blow", "fly"],
  ["Which word begins with ‘bl’?", "blue", "clean", "flower", "class"]
 ],
 "wb": {"ws": [], "mis": ["Confusing ‘short’ (opposite of tall) and ‘small’ (opposite of big).", "Spelling: hospital, school, post office."], "qz": []},
 "tg": []
}
SEC = [
 (44, "Let us Interact (page 108)", [
  "1. I see a village/town with a railway station, bus stop, school, hospital, people and vehicles (look at the picture).",
  "2. Places: railway station, bus stop, school, hospital, post office, bank, market, temple, park.",
  "3. Yes, I visited a railway station with my family (own answer)."]),
 (45, "Story • Let us Think (page 109)", [
  "1. The children are playing under the banyan tree.",
  "2. Sameera likes to play with her friends.",
  "3. Places: a school, a hospital, a post office, a bank and a Grama Sachivalayam.",
  "4. The village looks small and beautiful – fresh air, clean streets, gardens, trees.",
  "5. In my holidays I like to go to my grandma’s village / a park / Tirupati (own answer)."]),
 (46, "New words • Ask and answer (page 110)", [
  "New words: banyan trees, street, people, visit, villagers, friendly, clean, beautiful.",
  "A. What is this? – This is a post office / a bus stop / a school / a hospital / a railway station."]),
 (47, "I like to… (page 111)", [
  "Hi, I am ______. I like to go to the park / the market / the fair / the circus / an exhibition. (Own sentences, e.g., Hi, I am Kiran. I like to go to the beach.)"]),
 (48, "Let us Learn A, B (page 112)", [
  "A. a hospital, a post office, a village, a school.",
  "B. A tall tree. A short plant. A fat cat."]),
 (49, "Adjectives • Let us Learn C (page 113)", [
  "A thin cat. A big buffalo. A small calf. A clean street. A dirty street. (tall, short, fat, thin, big, small, clean, dirty are adjectives.)",
  "C. 1. A big elephant. 2. A small rat. 3. A tall coconut tree. 4. A short rose plant. 5. A fat pig."]),
 (50, "Let us Write A, B (page 114)", [
  "A. hospital, school, post office, bank, Bus stop.",
  "B. 1. This is a post office. 2. This is a school. 3. This is a market/village. 4. This is a bank. 5. This is a park. 6. This is a hospital. (Check with the pictures.)"]),
 (51, "Let us Write C, D (page 115)", [
  "C. 1. The ant is small. 2. The buffalo is big. 3. The plant is short. 4. The coconut tree is tall.",
  "D. I am a good girl/boy. I am a tall/short girl/boy. I am smart. I am clever. (Write about yourself using good, tall, short, smart, clever, beautiful.)"]),
 (52, "Let us Practise A, B (page 116)", [
  "A. vil-lage, peo-ple, vis-it, hos-pi-tal, beau-ti-ful – clap for each syllable.",
  "B. bl – black, blue, blow; cl – clap, class, close; fl – flag, flower, flow."]),
 (53, "Phonics C • Language game (page 117)", [
  "C. bl – block, blow, blood, blend; cl – clean, clear, click, close; fl – fly, flew, flat, flesh.",
  "Game: pick an opposite-word card and find the classmate with the opposite (tall–short, fat–thin, big–small, clean–dirty, hot–cold, good–bad)."]),
 (54, "Let us Practise – My Grandpa’s Village (page 118)", [
  "1. C) beautiful.",
  "2. B) Hospital.",
  "3. C) big.",
  "4. tall × short; thin × fat.",
  "5. i) School ii) Park.",
  "6. A. fat B. hot."]),
 (54, ET, edom("Role play, clapping syllables, language game", "identify places, opposite words, fill in the blanks", "story reading, adjectives, phonic drill (bl, cl, fl)", "role play, describing our village")),
]
