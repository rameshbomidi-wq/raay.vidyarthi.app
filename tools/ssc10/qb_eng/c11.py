# Unit 6 – Madam Rides the Bus – LEVEL-1, English_Final.pdf పేజీలు 78–81
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S
B = EB(11, 'en6')
L = 1
B.rcr(L, [(78, 4, 28)], '1. Valliammai.\n2. Standing in the front doorway of her house and watching what was happening in the street outside.\n'
      '3. B) The bus passing through her street.\n4. A) She had no playmates of her own age.\n5. A) Encourage them to find safe and meaningful ways to engage with their surroundings.')
B.rcr(L, [(78, 29, 41), (79, 1, 9)], '1. He was jolly and fond of joking; he teasingly called her “madam”, offered her a front seat and asked her permission to start the bus.\n'
      '2. She was overcome with shyness; avoiding everyone’s eyes, she walked quickly to an empty seat and sat down.\n'
      '3. B) Because the conductor was joking with her and calling her ‘madam’.\n4. B) Whether they could start the journey.\n5. A) Treat them kindly and help them feel comfortable.')
B.g(L, (79, 11), [((79, 12), 'Ravi said that he was preparing for his English exam.'), ((79, 13), 'Mother told me to finish my homework before dinner.'),
                  ((79, 14), 'The teacher said that the Earth revolves around the Sun.  (universal truth – tense not changed)'),
                  ((79, 15), 'Meena said that she had visited her grandparents the previous weekend.'),
                  ((79, 16), 'The doctor advised the patient to take that medicine twice a day.')])
B.g(L, (79, 17), [((79, 18, 22), '(a) a → an  (b) hardly → hard  (c) in → on  (d) It → Its'),
                  ((79, 23, 27), '(a) in – correct  (b) organise → organised  (c) An → The  (d) because but → because'),
                  ((79, 28, 31), '(a) bestest → best  (b) at → in  (c) help → helps  (d) They → Its')], mk=2)
ADV = [((79, 33), 'You should concentrate on your studies; exams are near.'), ((79, 34, 35), 'You should reduce your screen time and play outdoor games instead.'),
       ((79, 36, 37), 'You should not throw plastic waste on the road. You must use the dustbin and keep the surroundings clean.'),
       ((79, 38, 39), 'You should prepare regularly instead of worrying; then you will feel confident.'),
       ((79, 40), 'You should use a bucket of water instead of a hose pipe to wash your car.'),
       ((79, 41), 'You should eat fruits, vegetables and home-cooked food instead of junk food.'),
       ((79, 42, 43), 'You should always wear a helmet and follow road safety rules.'),
       ((80, 1), 'You should start early from home and be punctual.'),
       ((80, 2, 3), 'You should take part actively in classroom activities; it will build your confidence.'),
       ((80, 4, 5), 'You should not use your mobile phone late at night; you must sleep early and get enough rest.')]
B.g(L, (79, 32), ADV)
B.g(L, (80, 6, 7), [((80, 8, 12), '(a) curious – interested  (b) favourite – beloved  (c) happening – occurring  (d) playmates – companions'),
                    ((80, 13, 17), '(a) enjoyable – pleasant  (b) elaborate – detailed  (c) unusual – uncommon  (d) fascinating – captivating'),
                    ((80, 18, 23), '(a) crept – slipped  (b) overwhelming – strong  (c) wistfully – thoughtfully  (d) kindle – ignite')], mk=2)
B.g(L, (80, 24), [((80, 25, 28), '(a) short × long  (b) curious × uninterested (indifferent)  (c) favourite × disliked  (d) own × another’s'),
                  ((80, 29, 32), '(a) fascinating × boring  (b) nearest × farthest  (c) passed × stopped  (d) filled × emptied')], mk=2)
RF = [((80, 35, 36), 'excitement; curious'), ((80, 37, 38), 'carefully; determination'), ((80, 39, 40), 'cheerful; kindness'),
      ((80, 41, 42), 'proud; confidence'), ((81, 1, 2), 'smoothly; comfortable'), ((81, 3, 4), 'interest; beautiful'),
      ((81, 5, 6), 'politely; friendliness'), ((81, 7, 8), 'sad; silent'), ((81, 9, 10), 'unaware; naturally'), ((81, 11, 12), 'enjoyable; independence')]
B.g(L, (80, 33, 34), RF)
B.ce(L, (81, 14, 23),
     'Conductor: Hey, stop the bus! Stop the bus! A little madam wants to get on.\n'
     'Valli: (climbing in) I am not a child. I have a ticket fare. Here are thirty paise for the town.\n'
     'Conductor: Oh, please don’t be angry with me, my fine madam! Here, have a seat right up there in front. Everybody, make way for madam!\n'
     'Valli: (shyly) Thank you.\n'
     'Conductor: May we start now, madam? Here is your ticket. Are you going alone?\n'
     'Valli: Yes, I have my ticket and my money. Nobody needs to look after me.\n'
     'Conductor: You are a brave girl! Why do you stand on the seat?\n'
     'Valli: I want to see everything outside – the canal, the palm trees, the green fields and the mountains.\n'
     'Conductor: Look! A cow is running in front of the bus.\n'
     'Valli: (laughing) Oh, how funny! It is running with its tail up.\n'
     'Conductor: Will you get down at the town and have a drink?\n'
     'Valli: No, thank you. I will go back in the same bus. I have money for the return ticket.\n'
     'Conductor: You are a real madam – smart and confident! Enjoy your journey.')
B.ce(L, (81, 24, 33),
     'Friend: Valli, where were you this afternoon? I couldn’t find you anywhere.\n'
     'Valli: Can you keep a secret? I went to the town on the bus all by myself!\n'
     'Friend: Really? How did you manage it?\n'
     'Valli: I planned it for months. I listened to people talking and learnt that the town is six miles away, the fare is thirty paise one way and the journey takes forty-five minutes.\n'
     'Friend: But where did you get the money?\n'
     'Valli: I saved every coin. I didn’t buy peppermints, toys or balloons, and I didn’t even ride the merry-go-round. I saved sixty paise.\n'
     'Friend: You are amazing! What did you see?\n'
     'Valli: A canal, palm trees, green fields, distant mountains and a blue sky. A young cow ran in front of the bus – it was so funny! In the town I saw big shops and crowds of people.\n'
     'Friend: Did you enjoy the return journey too?\n'
     'Valli: Not really. On the way back I saw that same cow lying dead by the road. It had been hit by a vehicle. I felt very sad and didn’t look out of the window after that.\n'
     'Friend: That’s sad. How do you feel now?\n'
     'Valli: Proud that I did it myself, but I have also learnt that life and death are part of the same journey.')
B.ce(L, (81, 34, 37),
     'Thursday, 8 p.m.\n'
     'Dear Diary,\n'
     'Today my dream came true – I rode the bus all by myself to the town and back!\n'
     'For months I had been planning this trip. I saved sixty paise by not buying peppermints or toys. At one o’clock, when Mother was taking her nap, I slipped out and waved to the bus.\n'
     'The conductor laughed and called me “madam”. Everyone laughed and I felt shy, but I didn’t let anyone treat me like a child. I paid my own fare.\n'
     'What a lovely ride it was! I knelt on the seat and saw a canal, palm trees, grasslands, distant mountains and the blue sky. A young cow ran in front of the bus with its tail high up – I laughed till tears came.\n'
     'In the town I saw big, decorated shops and so many people. I didn’t get down; I came back in the same bus.\n'
     'But on the way back I saw the same cow lying dead by the road. My joy vanished. I felt so sad.\n'
     'Now I am back home and nobody knows my secret. I feel proud and grown-up, but I can’t forget the poor cow.\nValli')
B.ce(L, (81, 38, 41),
     'Thursday, 9 p.m.\n'
     'Dear Diary,\n'
     'Today I met the most amazing passenger of my career – a little girl of about eight named Valli.\n'
     'At one o’clock, during the slack hours, she waved and stopped my bus. I had to lift her in, but she said proudly, “I can get in by myself.” When I joked and called her “madam”, the passengers laughed, and she was shy for a moment, but she held her head high.\n'
     'She paid her own fare of thirty paise and refused to be treated like a child. When an old woman tried to talk to her, she politely kept her distance. She knelt on the seat and enjoyed every sight outside with wide eyes.\n'
     'At the town she did not get off. When I offered her a cold drink, she refused – she had counted her money for the return ticket. What a planner!\n'
     'On the way back she became quiet after seeing a dead cow by the road. She is a sensitive child.\n'
     'I have taken many passengers, but never one so confident and independent. That little madam has truly impressed me.\nThe Conductor')
B.ce(L, (81, 42, 44),
     'Thursday, 8 p.m.\n'
     'Dear Diary,\n'
     'My first bus journey was the happiest day of my life – until the return trip.\n'
     'On the way to the town, a young cow had run in front of the bus with its tail up, and I had laughed so much. But on the way back, I saw the same beautiful cow lying dead by the roadside. It had been hit by some vehicle.\n'
     'My heart sank. A few minutes ago it was so full of life, running and playing. Now it was still. I felt a lump in my throat. All my excitement vanished and I did not want to look out of the window anymore.\n'
     'I kept thinking: how uncertain life is! Something so full of life can be gone in a moment. Joy and sorrow come together in life.\n'
     'I will never forget that cow. Today I learnt not only how to travel alone but also an important lesson about life and death.\nValli')
ITEMS = B.items
