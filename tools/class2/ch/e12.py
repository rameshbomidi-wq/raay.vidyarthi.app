import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dom2 import edom, ET
S = 'eng'
PAGES = (73, 84)
L = {
 "id": "en12", "no": 12, "t": "6.2 Wheels on the Bus…", "m": [2], "ty": "Rhyme & Activities", "th": "Things and Vehicles",
 "by": "Blossoms-2 English Reader Sem-2 – Unit 6: Things and Vehicles (pages 137–148)",
 "sum": "Rhyme “Wheels on the bus”: the wheels on the bus go round and round, the horn goes beep beep beep, the doors go open and shut, and the driver says “Move on back” – all through the town. Children learn names of vehicles (bus, train, bicycle, helicopter, auto, car, tractor, ship, boat, aeroplane, lorry, motorcycle), speak about a vehicle (colour, wheels, where it moves), use ‘has’ (he, she, it, one) and ‘have’ (I, you, we, they, many), sort vehicles by land/water/air, rearrange words into sentences, clap syllables and learn the magic ‘e’ (i–e: time, nine, kite).",
 "te": "“Wheels on the bus” రైమ్ – బస్సు చక్రాలు గుండ్రంగా, హారన్ బీప్ బీప్, తలుపులు తెరుచుకుని మూసుకుంటాయి, డ్రైవర్ ‘Move on back’ అంటాడు. వాహనాల పేర్లు, వాహనం గురించి మాట్లాడడం, has/have, నేల–నీరు–గాలి వాహనాలు, పదాల క్రమం సరిచేయడం, syllables, magic ‘e’ (time, kite).",
 "pts": [
  "1. The wheels on the bus go round and round – all through the town.",
  "2. The horn on the bus goes beep, beep, beep.",
  "3. The doors on the bus go open and shut.",
  "4. The driver on the bus says, “Move on back.”",
  "5. Sight words: wheels, round, all, move, town.",
  "6. Speak about a vehicle: This is a car. This is a blue car. It has four wheels. It runs on the road. I like to travel in it.",
  "7. ‘has’ with he, she, it and one name: He has an auto. She has a car. It has four wheels. ‘have’ with I, you, we, they and many: They have bicycles. Children have books.",
  "8. Land: bus, car, train, jeep, bicycle, truck, scooter, cart, lorry, taxi, tractor. Water: ship, boat. Air: aeroplane, helicopter.",
  "9. Syllables: au-to, lor-ry, bul-lock, dri-ver, bi-cy-cle.",
  "10. Magic ‘e’ (i–e, long i): time, nine, kite, site, bike, smile, shine, pipe, pine, hide, file, like, side, dine, fine, ripe, wife, life, knife."],
 "w": [["wheel", "చక్రం"], ["round", "గుండ్రంగా"], ["horn", "హారన్"], ["shut", "మూయు"], ["through", "గుండా"], ["town", "పట్టణం"], ["driver", "డ్రైవర్"], ["vehicle", "వాహనం"], ["helicopter", "హెలికాప్టర్"], ["tractor", "ట్రాక్టర్"], ["ship", "ఓడ"], ["boat", "పడవ"], ["aeroplane", "విమానం"], ["bullock cart", "ఎడ్లబండి"], ["lorry", "లారీ"]],
 "gr": {"t": "has / have • Magic e", "p": [
  "has – he, she, it, one name: Kumar has a blue bag. A hen has two wings.",
  "have – I, you, we, they, many: We have bicycles. Mary and Jaya have shoes.",
  "Magic e: kit → kite, pin → pine, rip → ripe (e is silent, i says its name)."]},
 "qa": [
  ["How do the wheels on the bus go?", "Round and round."],
  ["What does the horn say?", "Beep, beep, beep."],
  ["What does the driver say?", "Move on back."],
  ["A car ___ four wheels (has/have)?", "has"],
  ["Name two water vehicles.", "Ship, boat."],
  ["Which vehicle flies high with two wings?", "Aeroplane."]
 ],
 "act": "Recite the rhyme with actions (rolling hands, pressing the horn, opening–closing doors). Play the paper-ball flashcard game and speak 4–5 sentences about a vehicle. Survey vehicles in your street (type, wheels, colour) and make a table. Play the vehicle-sound guessing game.",
 "kn": "Road safety: wear a helmet on a bike, a seat belt in a car; cross the road at the zebra crossing.",
 "qz": [
  ["The wheels on the bus go…", "round and round", "beep beep beep", "open and shut", "move on back"],
  ["The horn on the bus goes…", "beep beep beep", "round and round", "open and shut", "move on back"],
  ["The doors on the bus go…", "open and shut", "round and round", "beep beep", "up and down"],
  ["The driver says…", "Move on back", "Beep beep", "Open and shut", "Round and round"],
  ["All through the…", "town", "sky", "sea", "forest"],
  ["Correct sentence:", "The wheels on the bus go round and round.", "The doors on the bus go beep beep beep.", "The horn on the bus goes open and shut.", "The driver goes round and round."],
  ["Has two wings and flies high:", "Aeroplane", "Train", "Auto", "Ship"],
  ["We ___ bicycles.", "have", "has", "is", "was"],
  ["Sumathi ___ a pencil.", "has", "have", "are", "were"],
  ["A hen ___ two wings.", "has", "have", "are", "am"],
  ["Children ___ books.", "have", "has", "is", "was"],
  ["‘UATO’ rearranged:", "AUTO", "OUTA", "TAOU", "UOTA"],
  ["‘TAIRN’ rearranged:", "TRAIN", "RAINT", "NAIRT", "TRAIM"],
  ["‘HISP’ rearranged:", "SHIP", "HIPS", "PISH", "SHPI"],
  ["Which travels in water?", "boat", "bus", "tractor", "helicopter"],
  ["Which travels in air?", "helicopter", "ship", "tractor", "bus"],
  ["Which travels on land?", "tractor", "ship", "aeroplane", "boat"],
  ["Rearrange: has / He / a / bicycle", "He has a bicycle.", "Has he a bicycle.", "A bicycle has he.", "He a has bicycle."],
  ["Syllables in ‘bicycle’?", "3", "1", "2", "4"],
  ["Magic ‘e’ word with long i:", "kite", "kit", "sit", "pin"]
 ],
 "wb": {"ws": [], "mis": ["Using ‘have’ with he/she (She have a car) – correct: She has a car.", "Spelling ‘aeroplane’, ‘motorcycle’, ‘bicycle’."], "qz": []},
 "tg": []
}
SEC = [
 (73, "Let us Interact (page 137)", [
  "1. I see many vehicles on the road, in water and in the sky (look at the picture).",
  "2. Vehicles: bus, car, auto, bicycle, lorry, train, ship, boat, aeroplane, helicopter.",
  "3. I like the train most because it is big, fast and comfortable (own answer).",
  "4. The train (also the bus) carries more people.",
  "5. A boat / ship / aeroplane in flight does not use wheels to move (boat and ship have no wheels).",
  "6. Road: bus, car, auto, bicycle, lorry; Water: ship, boat; Air: aeroplane, helicopter."]),
 (74, "Rhyme – Wheels on the bus (page 138)", [
  "Recite with actions. Sight words: wheels, round, all, move, town."]),
 (75, "Let us Think • New words • Let us Speak (page 139)", [
  "Match: 1. wheels – round and round; 2. horn – beep beep beep; 3. doors – open and shut; 4. driver – move on back.",
  "New words: beep, horn, through, shut.",
  "Let us Speak (example): This is a bus. This is a red bus. It has six wheels. It runs on the road. I like to travel in it."]),
 (76, "Let us Learn A (page 140)", [
  "A. a bus, a train, a bicycle, a helicopter (and other vehicles in the pictures) – read aloud and repeat."]),
 (77, "Let us Learn B – has/have (page 141)", [
  "He is Naresh. He has an auto. She is Sruthi. She has a car. Anu and Abhi are classmates. They have bicycles. It is a tractor. It has four wheels. Anjali and Lavanya are friends. They have many toys."]),
 (78, "Let us Learn C • Let us Write A (page 142)", [
  "C. 1. A car has four wheels. 2. A hen has two wings. 3. Children have books. 4. Sumathi has a pencil. 5. Mary and Jaya have shoes.",
  "A. Land: bus, car, train, jeep, bicycle, truck, scooter, cart, lorry, taxi, tractor. Water: ship, boat. Air: aeroplane, helicopter."]),
 (79, "Let us Write B, C (page 143)", [
  "B. Vehicles: bus, car, auto, train, bicycle, lorry, ship, aeroplane, tractor (any).",
  "C. road, ship, car, bus, train, lorry, bicycle, aeroplane, motorcycle."]),
 (80, "Let us Write D – rearrange (page 144)", [
  "1. He has a bicycle. 2. She has a car. 3. They have a red car. 4. Children have a school bus. 5. Ravi has two cute puppies."]),
 (81, "Let us Practise A, B (page 145)", [
  "A. au-to, lor-ry, bul-lock, dri-ver, bi-cy-cle.",
  "B. Magic e (i–e): time, nine, kite; site, bike, smile, shine; pipe, pine, hide, file; like, side, dine, fine; ripe, wife, life, knife."]),
 (82, "Let us Do (page 146)", [
  "A. Survey table (own data), e.g.: motorcycle – 2 wheels – red; car – 4 – white; auto – 3 – yellow; bicycle – 2 – black; tractor – 4 – red.",
  "Answers depend on your survey: 1. most common vehicle (often motorcycle). 2. most seen colour. 3. Four-wheelers: car, tractor, jeep, taxi, lorry (lorries may have more).",
  "B. Vehicle identification game – make the sound (beep beep, chuk chuk) and let others guess."]),
 (83, "Let us Practise – Wheels on the bus (page 147)", [
  "1. B) (the picture of the boy playing with a toy car – check the pictures).",
  "2. B) The wheels on the bus go – round and round.",
  "3. B) Aeroplane.",
  "4. a) We have bicycles. b) Sumathi has a pencil.",
  "5. AUTO, TRAIN, SHIP.",
  "6. Land: bus, tractor; Air: helicopter, aeroplane; Water: boat, ship."]),
 (83, ET, edom("Reciting with actions, role play, vehicle game", "vehicle names, land–air–water vehicles, rearranging sentences", "rhyme, has/have, phonic drill (magic e)", "vehicle identification game, rhythm")),
 (84, "Mind Map (page 148)", [
  "Revise all Sem-2 units with the mind map: Unit 3 Health and Nature (healthy food, plants), Unit 4 Our Celebrations (festivals, birthday), Unit 5 Our Community and People (village, helpers), Unit 6 Things and Vehicles (fair, vehicles)."]),
]
