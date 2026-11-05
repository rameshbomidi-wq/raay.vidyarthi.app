# Footprints without Feet (S.R.) / The Tale of Custard the Dragon / Madam Rides the Bus grammar – English_Final.pdf పేజీలు 86–91
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S, IMG
B = EB(13, 'en6')
SR = 'sr5'

# ---------- LEVEL-1 : RISING STAR ----------
B.rcr(1, [(86, 3, 26)], '1. a) She tried to eject him\n2. b) not to be visible\n3. b) without clothes and money.\n4. c) His footprints in the mud\n'
      '5. a) Intelligence should be used responsibly and ethically.', lid=SR)
B.rcr(1, [(86, 27, 38), (87, 1, 12)], '1. b) He was invisible.\n2. a) cold meat\n3. b) Warm clothes, shoes, an overcoat and a wide-brimmed hat\n4. b) on a pile of quilts\n'
      '5. b) Scientific ability should be used with honesty and responsibility.', lid=SR)
B.rcr(1, [(87, 13, 29)], '1. The kitten was called Ink and the mouse was called Blink.\n2. Because the dragon was a coward (soft and timid like custard).\n'
      '3. c) The little yellow dog\n4. b) cowardly\n5. b) We should not judge someone’s courage without knowing their true character.')
B.g(1, (87, 31), [((87, 32), 'Valli said that she wanted to ride the bus alone.'), ((87, 33), 'The conductor told Valli not to stand on the seat.'),
                  ((87, 34), 'Valli told the conductor that she didn’t have any friends travelling with her.'),
                  ((87, 35), 'The elderly woman advised Valli that she should not travel alone.'),
                  ((87, 36), 'The conductor wished Valli (little madam) a safe journey.')])
B.g(1, (87, 37), [((87, 38), 'A ticket was issued to Valli by the conductor.  (or) Valli was issued a ticket by the conductor.'),
                  ((87, 39), 'Many passengers were carried to the town by the bus.'),
                  ((88, 1), 'The beautiful scenery was observed by Valli during the journey.'),
                  ((88, 2), 'Valli’s courage was appreciated by the passengers.'), ((88, 3), 'Valli was dropped at her destination by the bus.')])
B.g(1, (88, 4), [((88, 5), 'a (a young cow)'), ((88, 6, 7), 'a (a cheerful man)')])
B.g(1, (88, 8, 9), [((88, 10, 13), '(a) brave – fearless  (b) bought – purchased  (c) happy – joyful  (d) fast – rapid'),
                    ((88, 14, 17), '(a) eager – excited  (b) small – tiny  (c) lovely – beautiful  (d) looked – glanced')], mk=2)
B.g(1, (88, 18, 19), [((88, 20, 21), '(a) happy × sad  (b) new × old  (c) beautiful × ugly  (d) quickly × slowly'),
                      ((88, 22, 24), '(a) carefully × carelessly  (b) easy × difficult  (c) full × empty  (d) started × finished (ended)')], mk=2)
B.ce(1, (88, 26, 33),
     'Distribution of Sports Equipment in Z.P. High Schools (June 2026)\n'
     'The table gives details of the sports equipment distributed to Z.P. High Schools in June 2026. In all, 75 items were distributed. '
     'Cricket bats of the SG brand in brown colour were given in the largest number – 20. Cosco volleyballs (yellow) came next with 18, followed by 15 white Nivia footballs. '
     '12 black Yonex badminton rackets were supplied. Green Vinex chess boards were the fewest, with only 10 distributed. '
     'Thus outdoor games like cricket, volleyball and football received more equipment than indoor games like chess. This distribution will encourage students to take part in sports and stay fit.')

# ---------- LEVEL-2 : SHINING STAR ----------
B.rcr(2, [(89, 3, 20)], '1. b) to try the stocks (to find clothes and something to hide his invisible head)\n2. a) He didn’t have clothes\n'
      '3. b) Clothes and something to cover his invisible head\n4. b) Drury Lane\n5. b) Difficult situations should be handled honestly without breaking the law.', lid=SR)
B.rcr(2, [(89, 21, 40)], '1. b) noise in the study\n2. a) chink of money being taken\n3. b) Money\n4. c) A poker\n'
      '5. a) One should face unexpected situations with courage and presence of mind.', lid=SR)
B.rcr(2, [(90, 1, 18)], '1. Ink and Blink (the kitten and the mouse).\n2. Custard cried for a nice safe cage.\n3. b) a barrel full of bears\n4. a) As brave as a tiger in a rage\n'
      '5. b) We should not judge courage only by what someone says or appears to be.')
B.g(2, (90, 20), [((90, 21), 'Valli said that the bus looked new and comfortable.'), ((90, 22), 'The conductor told Valli to buy a ticket if she wanted to travel.'),
                  ((90, 23), 'Valli told the conductor that she had saved sixty paise for that journey.'),
                  ((90, 24), 'The conductor told them to look at the beautiful green fields.'), ((90, 25), 'Valli said that she would come back by the same bus.')])
B.g(2, (90, 26), [((90, 27), 'Valli was welcomed warmly by the conductor.'), ((90, 28), 'Many green fields were passed by the bus.'),
                  ((90, 29), 'Valli’s confidence was admired by the passengers.'), ((90, 30), 'The bus journey was enjoyed by Valli.'),
                  ((90, 31), 'A bus ticket was bought by Valli.')])
B.g(2, (91, 1), [((91, 2), 'the (Valli boarded the bus…)'), ((91, 3), 'an (an unforgettable journey)')])
B.g(2, (91, 4, 5), [((91, 6, 7), 'carefully'), ((91, 8), 'enjoyable'), ((91, 9), 'excitement'), ((91, 10), 'politely')])
B.ce(2, (91, 12, 21),
     'Sale of Laptops by Smart Tech Electronics (March 2026)\n'
     'The table shows the number of laptops of different brands sold by Smart Tech Electronics in March 2026. A total of 63 laptops were sold. '
     'The grey Lenovo IdeaPad (2025 model) was the best seller with 18 units, followed by the silver Dell Inspiron (2025) with 15 units. '
     'The black HP Pavilion (2024) sold 12 units and the blue ASUS VivoBook (2025) sold 10. The white Acer Aspire (2024) was the least sold, with only 8 units. '
     'The 2025 models (43 units) were clearly more popular than the 2024 models (20 units), which shows that customers prefer the latest models.')
B.ce(2, [(91, 22, 23)],
     'Classification of Things\n'
     'The tree diagram shows how things around us are classified. All things are divided into two groups – living things and non-living things. '
     'Living things are further divided into plants and animals. Plants are of two kinds: flowering plants and non-flowering plants. '
     'Animals are grouped into three types according to their food habits: herbivores, which eat only plants (vegetarian); carnivores, which eat the flesh of other animals (non-vegetarian); and omnivores, which eat anything – both plants and animals. '
     'Thus the diagram gives a clear and simple picture of the classification of things in nature.')
B.items[-1] = B.items[-1][:3] + (B.items[-1][3] + IMG('eng/qb_things_tree', 'Tree diagram – Things'),) + B.items[-1][4:]
ITEMS = B.items
