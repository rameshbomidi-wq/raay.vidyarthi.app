# Unit 3 – Two Stories about Flying (His First Flight, Black Aeroplane) / How to Tell Wild Animals – English_Final.pdf పేజీలు 27–32
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S
B = EB(3, 'en3')

# ---------- LEVEL-1 : RISING STAR ----------
B.rcr(1, [(27, 4, 24)], '1. Because his family had left him alone on the ledge as he was afraid to fly; they wanted to make him fly on his own (out of hunger).\n'
      '2. He saw his older brother catch his first herring and devour it, standing on a rock.\n3. B) How to fly, skim the waves, and dive for fish\n4. A) proud\n'
      '5. B) Encourage him patiently and help him to gain confidence.')
B.rcr(1, [(27, 25, 38), (28, 1, 8)], '1. To find out where he was and who the other pilot was, so that he could say ‘Thank you’ to him.\n'
      '2. She said that no other aeroplanes were flying that night in the storm; his was the only one she could see on the radar.\n'
      '3. A) a runway with lights\n4. A) One\n5. A) Thank the person and appreciate the help')
B.rcr(1, [(28, 9, 24)], '1. If a beast whose hide is peppered (covered) with spots leaps on you, you will know it is the Leopard.\n'
      '2. It is funny that you can identify the leopard only after it has leapt on you; roaring with pain is useless because it will only leap again and again.\n'
      '3. B) spots\n4. B) Leap again\n5. A) covered with spots')
B.rcr(1, [(28, 25, 39)], '1. While walking round your yard.\n2. The tone is humorous (light-hearted and playful).\n3. A) hugs you very hard\n4. A) a gentle touch or hug\n5. B) give you one more caress')
B.g(1, (29, 2), [((29, 3), 'The lesson is explained clearly by the teacher.'), ((29, 4), 'The bicycle is repaired by my father every Sunday.'),
                 ((29, 5), 'The guests are offered fresh juice by them.  (or) Fresh juice is offered to the guests by them.')])
B.g(1, (29, 6), [((29, 7, 8), '(a) see → saw  (b) his → their  (c) preen → preening  (d) at → on')], mk=2)
B.g(1, (29, 9), [((29, 10), 'brutalty → brutality'), ((29, 11), 'oppresser → oppressor'), ((29, 12), 'imposible → impossible'),
                 ((29, 13), 'aparthed → apartheid'), ((29, 14), 'fasinate → fascinate')])
B.g(1, (29, 15, 17), [((29, 18), 'break out (start suddenly): A fire broke out in the market last night.'),
                      ((29, 19), 'push to the limits (make someone use all their strength): The hard training pushed the athletes to their limits.'),
                      ((29, 20), 'come about (happen): How did this change come about?'),
                      ((29, 21), 'take away (remove): The storm took away the roofs of many huts.'),
                      ((29, 22), 'look up to (respect, admire): We look up to Dr. A.P.J. Abdul Kalam as our role model.')])
B.g(1, (29, 23), [((29, 24, 29), 'i) – c (not anymore)  ii) – b (finally)  iii) – a (after some time)  iv) – d (with astonishment)'),
                  ((29, 30, 36), 'i) – b (fly with one wing higher than the other)  ii) – a (move in a curved path)  iii) – c (support oneself on)  iv) – d (move from one side to the other)')], mk=2)

# ---------- LEVEL-2 : SHINING STAR ----------
B.rcr(2, [(30, 3, 29)], '1. He was maddened by hunger and dived at the piece of fish in his mother’s beak.\n'
      '2. The wind rushed against his feathers and wings; he did not fall but soared gradually downwards and outwards, and then upwards – he was flying.\n'
      '3. A) To make the young seagull fly towards the fish\n4. A) Confident\n5. B) Encouraging them to try on their own can build confidence.')
B.rcr(2, [(30, 30, 39), (31, 1, 16)], '1. He saw two long straight lines of lights – a runway, an airport.\n'
      '2. Because the pilot of the black aeroplane had guided him safely through the storm to the airport when his compass and radio were not working.\n'
      '3. C) No other flight was there on Radar.\n4. B) long straight lines of light\n5. B) gratitude')
B.rcr(2, [(31, 17, 32)], '1. In the jungles in the east.\n2. The tone is humorous (playful).\n3. B) large and tawny\n4. B) It roars at you.\n5. A) yellowish-brown')
B.rcr(2, [(31, 33, 42), (32, 1, 6)], '1. It is a noble wild beast with black stripes on a yellow ground (body); the poet humorously says, notice if he eats you.\n'
      '2. The tone is humorous (light and funny).\n3. A) black stripes on a yellow body\n4. B) identify\n5. B) eats you')
B.rcr(2, [(32, 7, 21)], '1. Because a novice (beginner) may be confused (nonplussed) as many beasts of prey look alike and are dangerous.\n'
      '2. The belief that crocodiles shed false tears (“crocodile tears”) while eating their prey.\n3. B) merry smiles\n4. B) Crocodile\n5. A) confuse')
B.g(2, (32, 23), [((32, 24), 'Let the door be closed.'), ((32, 25), 'Let the old man be helped, please.  (or) You are requested to help the old man.'),
                  ((32, 26), 'Let water not be wasted.')])
B.g(2, (32, 27), [((32, 28, 29), '(a) writer → writers  (b) trying → try  (c) meaned → meaning  (d) his → their'),
                  ((32, 30, 31), '(a) made → make  (b) using → used  (c) and → but  (d) seeing → see')], mk=2)
B.g(2, (32, 32), [((32, 33, 37), 'i) – b (move towards the front)  ii) – c (jump into something)  iii) – d (stop trying)  iv) – a (become frightened)'),
                  ((32, 38, 42), 'i) – b (return or arrive)  ii) – a (move away)  iii) – c (pull into pieces)  iv) – d (direct one’s eyes towards)')], mk=2)
ITEMS = B.items
