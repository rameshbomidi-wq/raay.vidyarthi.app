import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (15, 25)
L = {
 "id": "en6", "no": 6, "t": "3.2 Our Friends in Nature", "m": [11], "ty": "Story & Activities", "th": "Health and Nature",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 3: Health and Nature (pages 79–89)",
 "sum": "Story “Rani’s Plant”: Rani took a seed from her grandfather Rajanna. She filled a pot with soil, put the seed in the soil and poured water. After a few days she saw a plant with flowers. She felt happy to see butterflies and bees on her plant. Ram and Sudha visit a garden: “What is this? – This is a rose. It is red… What are these? – These are lilies. They are white. What are those? – Those are sunflowers. They are yellow.” Children learn flower names, colours, singular–plural (add s/es), These/Those, and my, his, her, our, your, their, and the sounds l and g.",
 "te": "“రాణి మొక్క” కథ – తాతయ్య రాజన్న నుండి విత్తనం తీసుకుని కుండీలో మట్టి నింపి, నాటి, నీళ్ళు పోసింది; కొన్ని రోజులకు పూల మొక్క వచ్చింది; సీతాకోకచిలుకలు, తేనెటీగలు చూసి సంతోషించింది. రామ్–సుధ తోట సంభాషణ (This/That, These/Those, రంగులు). పూల పేర్లు, రంగులు, ఏకవచనం–బహువచనం (s/es), my, his, her, our, your, their, l, g శబ్దాలు.",
 "pts": [
  "1. Rani took a seed from her grandfather Rajanna.",
  "2. She filled the pot with soil, put the seed in the soil and poured some water.",
  "3. After a few days she saw a plant with flowers; she felt happy to see butterflies and bees.",
  "4. Dialogue: This is a rose – it is red. That is a marigold – it is orange. This is grass – it is green. These are lilies – they are white. Those are sunflowers – they are yellow.",
  "5. Flowers: sunflower, marigold, lily, jasmine, lotus, chrysanthemum, hibiscus, rose.",
  "6. Colours: red, yellow, blue, green, white, black, pink, brown, orange.",
  "7. Plural: add -s (rose – roses, pen – pens, boy – boys) or -es (class – classes, bush – bushes, glass – glasses, hero – heroes, brush – brushes).",
  "8. These are … (many, near); Those are … (many, far). This/That – one thing.",
  "9. Ownership words: I – my, He – his, She – her, We – our, You – your, They – their.",
  "10. Sounds: l – leg, lip, lion, left, lamp, like; g – go, gap, gas, gum, gun, get."],
 "w": [["seed", "విత్తనం"], ["sow", "నాటు/విత్తు"], ["soil", "మట్టి"], ["pour", "పోయు"], ["plant", "మొక్క"], ["pot", "కుండీ"], ["butterfly", "సీతాకోకచిలుక"], ["bee", "తేనెటీగ"], ["marigold", "బంతిపువ్వు"], ["jasmine", "మల్లెపువ్వు"], ["lotus", "తామరపువ్వు"], ["hibiscus", "మందారం"], ["chrysanthemum", "చామంతి"], ["sunflower", "పొద్దుతిరుగుడు పువ్వు"], ["roots", "వేళ్ళు"]],
 "gr": {"t": "These/Those • Singular–Plural • my/his/her/our/your/their", "p": [
  "This is a rose. (one, near) → These are roses. (many, near)",
  "That is a kite. (one, far) → Those are kites. (many, far)",
  "pen → pens; class → classes; bush → bushes; hero → heroes",
  "I am Abdul – these are my books. He is Ramesh – that is his bat. She is Mary – those are her balloons. They are Gopal and Aarif – those are their kites."]},
 "qa": [
  ["Who gave the seed to Rani?", "Her grandfather Rajanna."],
  ["What did Rani fill the pot with?", "Soil."],
  ["What did she see after a few days?", "A plant with flowers."],
  ["Which insects came to her plant?", "Butterflies and bees."],
  ["What colour are lilies?", "White."],
  ["Plural of ‘class’?", "classes."]
 ],
 "act": "Sow a seed in a pot/cup and water it daily; draw its growth. Role-play Ram and Sudha’s dialogue. Show flowers and say their colours. Hold one/many things near and far and say This/That/These/Those.",
 "kn": "Bees and butterflies carry pollen from flower to flower and help plants make fruits and seeds.",
 "qz": [
  ["Who is Rajanna?", "Rani’s grandfather", "Rani’s brother", "Rani’s teacher", "Rani’s friend"],
  ["What did Rani take from her grandfather?", "A seed", "A fruit", "A pot", "A flower"],
  ["Rani ___ the seed in the pot.", "put", "threw", "ate", "sold"],
  ["What did Rani pour?", "Water", "Milk", "Oil", "Juice"],
  ["After some days Rani saw a…", "plant", "pot", "bird", "stone"],
  ["How did Rani feel?", "Happy", "Angry", "Sad", "Afraid"],
  ["What colour is the rose (in the dialogue)?", "Red", "White", "Yellow", "Blue"],
  ["What colour is the marigold?", "Orange", "Green", "Blue", "Black"],
  ["Which flower is yellow?", "Sunflower", "Rose", "Lily", "Jasmine"],
  ["‘This/That’ is used for…", "One thing", "Many things", "Two persons", "No things"],
  ["You hold two apples. You say…", "These are apples.", "This is an apple.", "Those are apples.", "That is apples."],
  ["Many birds far away:", "Those are crows.", "This is crows.", "These is crows.", "That are crows."],
  ["Plural of ‘pen’?", "pens", "penes", "pen", "penns"],
  ["Plural of ‘bush’?", "bushes", "bushs", "bush", "bushies"],
  ["Plural of ‘hero’?", "heroes", "heros", "heroies", "hero"],
  ["‘He’ goes with…", "his", "her", "my", "their"],
  ["‘She’ goes with…", "her", "his", "our", "my"],
  ["‘They’ goes with…", "their", "our", "your", "my"],
  ["Which word starts with the ‘l’ sound?", "lion", "gun", "go", "gas"],
  ["Which word starts with the ‘g’ sound?", "gum", "leg", "lip", "lamp"]
 ],
 "wb": {"ws": [], "mis": ["Using ‘These is’ – correct is ‘These are’.", "Adding only ‘s’ to class/bush (classs) – add ‘es’."], "qz": []},
 "tg": []
}
SEC = [
 (15, "Let us Interact (page 79)", [
  "1. I see children, a teacher/elders, plants, trees and flowers (look at the picture).",
  "2. The children are in a garden (school garden).",
  "3. They are planting saplings and watering plants.",
  "4. Objects: pots, watering can, spade, saplings, flowers, trees, butterflies.",
  "5. Yes, I planted a sapling at home/school; I watered it daily and it grew (own answer)."]),
 (16, "Story – Rani’s Plant (page 80)", [
  "Read the story aloud: Rani took a seed from grandfather Rajanna → filled the pot with soil → put the seed → poured water → plant with flowers → butterflies and bees → Rani felt happy."]),
 (17, "New words • Let us Think (page 81)", [
  "New words: plant, sow, pour, soil, butterfly, bee.",
  "1. Rajanna is grandfather of Rani. 2. Rani took a seed from her grandfather. 3. She put the seed in the pot. 4. She saw a plant after some days. 5. Rani felt happy."]),
 (18, "Dialogue – Ram and Sudha (page 82)", [
  "Practise the dialogue in pairs: What is this? – This is a rose. It is red. / What is that? – That is a marigold. It is orange. / What is this? – This is grass. It is green. / What are these? – These are lilies. They are white. / What are those? – Those are sunflowers. They are yellow."]),
 (19, "Let us Learn A–C (page 83)", [
  "A. Flowers: sunflower, marigold, lily, jasmine, lotus, chrysanthemum, hibiscus, rose.",
  "B. Colours: red, yellow, blue, green, white, black, pink, brown, orange.",
  "C. Singular → Plural: rose – roses, pen – pens, crow – crows, book – books, boy – boys, class – classes, bush – bushes, glass – glasses, hero – heroes, brush – brushes."]),
 (20, "Let us Learn D – These / Those (page 84)", [
  "These are trees. (near) Those are trees. (far) These are fruits. Those are fruits. These are flowers. Those are flowers."]),
 (21, "Let us Learn E – my, his, her, their (page 85)", [
  "1. I am Abdul. These are my books. 2. He is Ramesh. That is his bat. 3. She is Mary. Those are her balloons. 4. She is Anitha. These are her bags. 5. They are Gopal and Aarif. Those are their kites."]),
 (22, "Ownership words • Let us Write A (page 86)", [
  "my – I, his – He, her – She, our – We, your – You, their – They.",
  "A. Missing letters: plant, flower, fruit, leaf, tree, roots."]),
 (23, "Let us Write B (page 87)", [
  "1. This is an apple. It is red.",
  "2. This is a leaf. It is green.",
  "3. These are roses. They are red.",
  "4. These are lilies. They are white.",
  "5. These are crows. They are black."]),
 (24, "Phonics • Let us Do (page 88)", [
  "l – leg, lip, lion, left, lamp, like; g – go, gap, gas, gum, gun, get. Practise aloud.",
  "Let us Do: colour the flower and write its name (e.g., sunflower – yellow petals, brown centre; or rose – red)."]),
 (25, "Let us Practise – Our Friends in Nature (page 89)", [
  "1. A) One thing.",
  "2. C) Sunflower.",
  "3. B) These are apples.",
  "4. his (for He), her (for She).",
  "5. pen – pens; class – classes.",
  "6. 1. plant 2. leaf."]),
 (25, ET, edom("Role play, colouring the flower", "fill in the blanks, flower names, singular–plural", "picture reading, story reading, phonic drill (l, g)", "role play, phonic drill, colouring")),
]
