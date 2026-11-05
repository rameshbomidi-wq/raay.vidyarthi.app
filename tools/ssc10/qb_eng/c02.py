# Unit 2 – A Tiger in the Zoo (poem) / A Triumph of Surgery (S.R.) – English_Final.pdf పేజీలు 16–26
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S, IMG
B = EB(2, 'en2')

# ---------- LEVEL-1 : RISING STAR ----------
B.rc(1, 16, 3, '1. Near the water hole.\n2. Plump deer pass near the water hole.\n3. A) shadow\n4. B) long grass\n5. A) natural habitat')
B.rc(1, 16, 16, '1. Around houses at the jungle’s edge.\n2. The villagers (the tiger terrorises the village).\n3. A) in jungle\n4. A) white fangs\n5. A) fierce')
B.rc(1, 16, 29, '1. In a concrete cell (a cage) in the zoo.\n2. The visitors.\n3. A) behind bars\n4. B) cage\n5. A) concrete cell')
B.rc(1, 17, 2, '1. A) He had become very fat\n2. C) cream cake and chocolates\n3. B) Mrs Pumphrey’s dog\n4. C) cut down on the sweet things\n5. B) He didn’t know to refuse food.', lid='sr1')
B.rc(1, 17, 29, '1. C) They decided he was an uninteresting object and ignored him.\n2. B) He gave him absolutely no food, but provided plenty of water.\n'
     '3. B) At the end of the second day.\n4. C) The greyhound dog living at the surgery.\n5. A) Because of his excess, surplus body fat.', lid='sr1')
B.rc(1, 18, 21, '1. B) He received no medicinal treatment at all\n2. B) He fought fiercely like a tiger to secure his share of food.\n'
     '3. B) She was anxious and constantly wanted the latest news regarding Tricki’s health.\n4. B) The narrator and his partners for breakfast.\n5. C) recovering from an illness.', lid='sr1')
JS = '(Jumbled sentences {Q. No. 17}) '
B.rcr(1, [(19, 24, 36)], 'Correct order: c, a, d, e, b\n'
      'c) Accidents can happen anywhere.\na) The wound should be covered with a clean bandage.\nd) Cool water should be poured on burns.\n'
      'e) An ambulance should be called quickly.\nb) Learning first aid is useful for everyone.', mk=2)
B.rcr(1, [(20, 1, 16)], 'Correct order: B, D, C, A, E\n'
      'B) Water is a valuable natural resource.\nD) Many places are facing water shortages.\nC) People should use water wisely in their daily lives.\n'
      'A) Rainwater harvesting is an effective way to conserve water.\nE) Saving water today will protect the future.', mk=2)
B.g(1, (20, 18), [((20, 19), 'I saw a girl who was singing beautifully.'), ((20, 20), 'This is Nirosha whom I was praising.'),
                  ((20, 21), 'The students whom the teacher punished were shouting.  (or) The teacher punished the students, who were shouting.')])
B.g(1, (20, 22), [((20, 23), 'in'), ((20, 24), 'during'), ((20, 25), 'into')])
B.g(1, (20, 26, 27), [((20, 28, 29), '(a) large × small  (b) hope × despair  (c) destroyed × created (built)  (d) sad × happy', 'en1'),
                      ((20, 30, 31), '(a) beginning × end  (b) freedom × slavery (bondage)  (c) peaceful × violent  (d) equality × inequality')], mk=2)
B.g(1, (20, 32), [((20, 33, 34), '(a) destroyed  (b) sadness', 'en1'), ((21, 1, 3), '(a) freedom  (b) achievement')], mk=2)
B.ce(1, (21, 4, 11), 'i) Confidence means the quality of having trust in people, plans or the future.\nii) ‘Confidently’ is an adverb.', mk=2)
B.ce(1, (21, 13, 17),
     'Mrs Pumphrey’s Feelings about Tricki\n'
     'Mrs Pumphrey loved her pet Tricki more than anything in the world. When Mr Herriot took Tricki to the veterinary hospital, she was heartbroken. '
     'She almost fainted and cried bitterly as the car moved away. She was sure that Tricki would pine and die without seeing her every day. '
     'At home she felt lonely and restless; the house looked empty without him. She worried day and night whether he was eating properly, sleeping comfortably and keeping warm. '
     'She rang up the surgery a dozen times a day for the latest news about his health. When she heard the word “convalescing”, she felt relieved and sent fresh eggs and bottles of wine to build up his strength. '
     'She counted the days till she could take her darling Tricki back home. Her feelings show her deep, though foolish, love for her pet.', lid='sr1')
B.ce(1, [(21, 18, 19)],
     'Favourite Beverage\n'
     'The pie chart shows the favourite beverages of a group of people. Cola is the most popular drink, liked by 27% of the people. '
     'Coffee comes next with 25%, followed closely by tea with 24%. Together, tea and coffee are the favourites of almost half (49%) of the people. '
     '13% of the people prefer other beverages. Water is the least preferred, chosen by only 11%. '
     'It is a matter of concern that cola, a soft drink with a lot of sugar, is the most popular, while healthy, plain water is the least liked. '
     'People should be made aware of the benefits of drinking more water and fewer sugary drinks.')
B.items[-1] = B.items[-1][:3] + (B.items[-1][3] + IMG('eng/qb_beverage', 'Favourite Beverage – pie chart'),) + B.items[-1][4:]

# ---------- LEVEL-2 : SHINING STAR ----------
B.rc(2, 22, 3, '1. In the shadow, sliding through long grass near the water hole.\n2. The mood is free, wild and natural – the tiger is shown as powerful and at ease in its natural home.\n'
     '3. B) near water hole\n4. B) long grass\n5. B) plump')
B.rc(2, 22, 16, '1. Around houses at the jungle’s edge.\n2. A frightening image of a fierce tiger snarling and baring his white fangs and claws, terrorising the village.\n'
     '3. B) jungle\n4. B) fangs\n5. B) village')
B.rcr(2, [(22, 29, 39), (23, 1, 3)], '1. In a concrete cell (cage) in the zoo.\n2. The mood is sad, helpless and angry – the strong tiger is caged and frustrated.\n'
      '3. B) in concrete cell\n4. A) visitors\n5. A) cannot use his natural power freely')
B.rcr(2, [(23, 5, 37)], '1. B) He was deeply shocked by how unhealthy Tricki looked.\n2. A) She assumed he was suffering from malnutrition.\n'
      '3. C) She thought he looked too weak and could not bear to deny him his favorite treats.\n4. B) He was too greedy and never refused any food.\n'
      '5. A) Pets need proper care, exercise, and attention.', lid='sr1')
B.rcr(2, [(24, 1, 34), (25, 1, 4)], '1. B) Cut his food right down and give him more exercise.\n2. A) She admitted it would be incredibly difficult for her to do.\n'
      '3. B) He had an entire wardrobe of tweed coats for cold weather and raincoats for wet days.\n4. B) He refused food, had bouts of vomiting, and lay panting on a rug.\n'
      '5. A) She truly cared for and loved her pet.', lid='sr1')
B.rcr(2, [(25, 5, 32), (26, 1, 4)], '1. B) for about a fortnight (two weeks)\n2. B) She was certain Tricki would pine away and die if he didn’t see her daily.\n'
      '3. B) Tricki’s favorite toys, separate day and night beds, cushions, and multiple bowls.\n4. B) He realized his car would never be able to hold all of Tricki’s luxury items.\n'
      '5. A) She was deeply attached to her pet.', lid='sr1')
B.g(2, (26, 6), [((26, 7), 'Food which is imported from other countries is expensive.'), ((26, 8), 'The lady whose cat died was very sad.'),
                 ((26, 9), 'My sister, whom I admire a lot, is leaving for Mumbai.')])
B.g(2, (26, 10), [((26, 11), 'of'), ((26, 12), 'off'), ((26, 13), 'on'), ((26, 14), 'in')])
B.g(2, (26, 15, 16), [((26, 17, 18), '(a) happy × sad  (b) heavy × light  (c) alive × dead  (d) worse × better', 'en1'),
                      ((26, 19, 21), '(a) bright × dull (dark)  (b) gathered × scattered (dispersed)  (c) largest × smallest  (d) newborn × old')], mk=2)
B.g(2, (26, 22), [((26, 23, 24), '(a) preparing  (b) replied', 'en1'), ((26, 25, 27), '(a) wound  (b) recovering')], mk=2)
ITEMS = B.items
