import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (5, 14)
L = {
 "id": "en5", "no": 5, "t": "3.1 Healthy Foods – Healthy Habits", "m": [11], "ty": "Rhyme & Activities", "th": "Health and Nature",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 3: Health and Nature (pages 69–78)",
 "sum": "Children talk about a picture of fruits and vegetables. They recite the rhyme “Fruits for all…!” – three yellow mangoes, three red apples and three green guavas on the tree are shared with the traveller, the bird, the squirrel, the rabbit, the parrot, the monkey and with you. They recite “This is the way we brush our teeth / wash our face / comb our hair, early in the morning” (good habits). They learn names of vegetables and fruits, healthy food (fish, pulses, nuts, milk, eggs), -ing action words (bathing, eating, reading, watching, singing), ‘This is…’ for near things and ‘That is…’ for far things, and the sounds v, m, r.",
 "te": "పండ్లు–కూరగాయల చిత్రం గురించి మాట్లాడటం. “Fruits for all” రైమ్ – చెట్టుపై మామిడి, ఆపిల్, జామ పండ్లను బాటసారి, పక్షి, ఉడుత, కుందేలు, చిలుక, కోతి, మనతో పంచుకోవడం. “This is the way we brush our teeth” రైమ్ – ఉదయం మంచి అలవాట్లు. కూరగాయలు, పండ్ల పేర్లు, ఆరోగ్యకరమైన ఆహారం, -ing పదాలు, This (దగ్గర) – That (దూరం), v, m, r శబ్దాలు.",
 "pts": [
  "1. Rhyme “Fruits for all”: Three yellow mangoes – one for the traveller who rests under the tree, one for the bird who nests on the tree, one for you to share with me.",
  "2. Three red apples – for the squirrel who runs up the tree, the rabbit who lives under the tree, and you. Three green guavas – for the parrot, the monkey, and you.",
  "3. Sight words: who, one, for, tree.",
  "4. Rhyme “This is the way…”: we brush our teeth, wash our face, comb our hair, read our books – early in the morning (good habits).",
  "5. Vegetables: tomato, potato, onion, cabbage, brinjal, cauliflower, carrot, radish, peas. Fruits: orange, guava, jackfruit, pineapple, apple, mango, banana, watermelon.",
  "6. Healthy food: fruits, vegetables, milk, eggs, fish, pulses, nuts, rice. Junk food (chips, cool drinks, too many sweets) is not good.",
  "7. -ing words (doing now): bathing, eating, reading, watching, singing, going, trimming.",
  "8. ‘This is…’ for near things (This is a house.); ‘That is…’ for far things (That is a tree.).",
  "9. Sounds: v – van, vote, vet, violet, very; m – mat, map, man, mug, milk; r – red, rat, ram, rod, run.",
  "10. Action words: run, jump, cry, laugh, sleep, brush, sneeze, drink, sit, write, clap, snap, walk, eat, read."],
 "w": [["healthy", "ఆరోగ్యకరమైన"], ["habit", "అలవాటు"], ["traveller", "బాటసారి"], ["rest", "విశ్రాంతి"], ["nest", "గూడు కట్టు"], ["share", "పంచుకో"], ["squirrel", "ఉడుత"], ["vegetables", "కూరగాయలు"], ["pulses", "పప్పు దినుసులు"], ["nuts", "గింజలు (వేరుశనగ, జీడిపప్పు)"], ["brinjal", "వంకాయ"], ["radish", "ముల్లంగి"], ["peas", "బఠానీలు"], ["guava", "జామ"], ["comb", "దువ్వు"]],
 "gr": {"t": "This / That • -ing words", "p": [
  "This is a boy. (near – దగ్గర)  That is a kite. (far – దూరం)",
  "This is an apple. – ‘an’ before a, e, i, o, u sounds.",
  "-ing: eat → eating, read → reading, sing → singing (పని జరుగుతోంది)."]},
 "qa": [
  ["Who rests under the mango tree?", "The traveller."],
  ["Who nests on the tree?", "The bird."],
  ["Who runs up the apple tree?", "The squirrel."],
  ["When do we brush our teeth?", "Early in the morning."],
  ["Name a green vegetable.", "Peas / cabbage."],
  ["What do we say for a far thing?", "That is …"]
 ],
 "act": "Recite both rhymes with actions. Show real fruits/vegetables and name them. Point to near and far things in class and say ‘This is…/That is…’. Play ‘Act Out’ – mime action words (run, jump, clap…). Make a healthy lunch-box chart.",
 "kn": "Eat a rainbow – fruits and vegetables of many colours keep us healthy. Wash fruits and hands before eating.",
 "qz": [
  ["How many yellow mangoes were on the tree?", "Three", "Two", "Four", "One"],
  ["Who rests under the mango tree?", "The traveller", "The parrot", "The monkey", "The rabbit"],
  ["Who nests on the tree?", "The bird", "The squirrel", "The rabbit", "The traveller"],
  ["Who runs up the apple tree?", "The squirrel", "The parrot", "The monkey", "The bird"],
  ["Who lives under the apple tree?", "The rabbit", "The bird", "The parrot", "The man"],
  ["Who jumps up the guava tree?", "The monkey", "The rabbit", "The bird", "The traveller"],
  ["Colour of the guavas in the rhyme?", "Green", "Red", "Yellow", "Blue"],
  ["Which is a healthy habit?", "Brushing teeth", "Eating junk food", "Sleeping late", "Not bathing"],
  ["Which is a green vegetable?", "Peas", "Tomato", "Carrot", "Onion"],
  ["A healthy lunch box has…", "Rice, pulses and vegetables", "Chips and cool drink", "Sweets and chocolates", "Only biscuits"],
  ["The kite is far away. We say…", "That is a kite.", "This is a kite.", "These is a kite.", "Those is a kite."],
  ["The book is in my hand. We say…", "This is a book.", "That is a book.", "Those is a book.", "It are a book."],
  ["Which word rhymes with ‘man’?", "fan", "mat", "map", "milk"],
  ["Which word starts with the ‘v’ sound?", "van", "mat", "red", "rat"],
  ["Which word starts with the ‘r’ sound?", "run", "mug", "van", "vet"],
  ["‘read’ + ing =", "reading", "readding", "readeing", "readng"],
  ["Which is a vegetable?", "brinjal", "guava", "orange", "pineapple"],
  ["Which is a fruit?", "jackfruit", "radish", "cabbage", "onion"],
  ["‘This is the way we brush our teeth’ – when?", "Early in the morning", "At midnight", "In the afternoon only", "Never"],
  ["Which is NOT healthy food?", "Chips", "Milk", "Fruits", "Pulses"]
 ],
 "wb": {"ws": [], "mis": ["Using ‘this’ for far things and ‘that’ for near things.", "Writing ‘a apple’ – correct is ‘an apple’."], "qz": []},
 "tg": []
}
SEC = [
 (5, "Let us Interact (page 69)", [
  "1. I see many fruits and vegetables (in a big heap).",
  "2. Fruits: banana, mango, apple, papaya, watermelon, pineapple, grapes, orange, guava. Vegetables: tomato, brinjal, cabbage, cauliflower, carrot, beans, pumpkin, onion (look at the picture).",
  "3. Red fruits: apple, pomegranate, watermelon (inside), strawberry, cherry.",
  "4. Green vegetables: peas, beans, cabbage, spinach (leafy vegetables), ladies finger, bottle gourd.",
  "5. I like mango and carrot the most (own answer).",
  "6. We eat fruits and vegetables to be healthy and strong; they give us vitamins and keep away diseases."]),
 (6, "Let us Recite – Fruits for all (page 70)", [
  "Recite with actions. Sight words: who, one, for, tree.",
  "Let us Think: 1. The apple tree shares its fruits with the squirrel, the rabbit and you (me).",
  "2. Circle ‘for’ and ‘on’ in the poem (e.g., ‘One for the bird who nests on the tree’).",
  "3. The man (traveller) is taking rest under the mango tree.",
  "4. I share my toys, books, food and chocolates with my brother/sister (own answer)."]),
 (7, "Words • Rhyme – This is the way (page 71)", [
  "Read the words: traveller, rest, nest, share, hang, squirrel – observe the spelling.",
  "Recite ‘This is the way we brush our teeth… wash our face…’ with actions."]),
 (8, "Rhyme continued • Let us Learn (page 72)", [
  "This is the way we comb our hair, comb our hair, comb our hair; this is the way we comb our hair, early in the morning.",
  "This is the way we read our books, read our books, read our books; this is the way we read our books, early in the morning.",
  "More lines (teacher): This is the way we take a bath… This is the way we go to school…",
  "Let us Learn A: tomato, potato, onion – read aloud and repeat."]),
 (9, "Vegetables and fruits (page 73)", [
  "Vegetables: cabbage, brinjal, cauliflower, carrot, radish, peas.",
  "Fruits: orange, guava, jackfruit, pineapple – read aloud and repeat."]),
 (10, "Healthy food • -ing words (page 74)", [
  "B. Healthy food: fish, eggs, milk, pulses, nuts, fruits, vegetables.",
  "C. -ing words: bathing, eating, reading – observe the spelling (verb + ing)."]),
 (11, "-ing words • Let us Write A (page 75)", [
  "-ing words: going, trimming, watching, singing (trim → trimming – double m).",
  "A. This is a house. That is a tree. This is a boy. That is a toy. This is a flower. That is a pot. (This – near, That – far)"]),
 (12, "Let us Write B • Let us Practise (page 76)", [
  "B. This is a watermelon. That is an apple. This is a girl. That is a kite. This is a banana. That is a monkey. (Look at the picture: near → This, far → That.)",
  "Let us Practise: v – van, vote, vet, violet, very; m – mat, map, man, mug, milk; r – red, rat, ram, rod, run. Say aloud and repeat."]),
 (13, "Let us Do – Act Out (page 77)", [
  "Mime the action words: run, jump, cry, laugh, sleep, brush, sneeze, drink, sit, write, clap, snap, walk, eat, read.",
  "More action words: swim, dance, sing, kick, throw, cut, cook, sweep."]),
 (14, "Let us Practise – Healthy Foods (page 78)", [
  "1. C) Brushing teeth.",
  "2. C) Peas.",
  "3. B) Rice, pulses, and vegetables.",
  "4. That is a kite.",
  "5. Healthy foods: fruits, milk (also vegetables, eggs, pulses).",
  "6. Rhyming words with ‘an’: fan, man (also van, pan, can)."]),
 (14, ET, edom("Recite the rhyme with actions, enacting action words", "identify fruits and vegetables, healthy vs junk food, action words, This & That", "names of fruits and vegetables, phonic drill (v, m, r)", "reciting the rhyme in rhythm, acting out action words")),
]
