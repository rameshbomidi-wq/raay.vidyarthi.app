# Unit 3 (contd.) – Study skills, grammar, The Ball Poem – English_Final.pdf పేజీలు 33–40
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S, IMG
B = EB(4, 'en3')

# ---------- LEVEL-1 : RISING STAR (p33–34) ----------
B.rcr(1, [(33, 3, 14)], 'i) The bar diagram represents the favourite fruits of students (number of students who like each fruit).\n'
      'ii) Banana (150 students).\niii) b) 90\niv) b) Orange (80)\nv) a) Banana is liked by 150 students', mk=4)
B.items[-1] = B.items[-1][:3] + (B.items[-1][3] + IMG('eng/qb_fruits', 'Favourite Fruits of Students – bar diagram'),) + B.items[-1][4:]
B.g(1, (33, 16), [((33, 17), 'The thief was caught by the police yesterday.'),
                  ((33, 18), 'We were told an interesting story by my grandmother.  (or) An interesting story was told to us by my grandmother.')])
B.g(1, (33, 19), [((33, 20), 'Ravi found an old map in the attic of his grandfather’s house.'), ((33, 21), 'We saw an eagle flying over the river.'),
                  ((33, 22), 'She wants to become an architect and work for an international company.'), ((33, 23), 'There was an accident near the railway station this morning.'),
                  ((33, 24), 'My father bought an umbrella from the shop near the bus stand.')])
B.g(1, (33, 25), [((33, 26), 'You should see a doctor immediately.  (or) Why don’t you consult a doctor?'),
                  ((33, 27, 28), 'You should wear a helmet while riding a bike.'),
                  ((34, 1, 2), 'You should prepare for the exam instead of watching TV.'),
                  ((34, 3), 'You should not eat too much junk food.'),
                  ((34, 4), 'You should not come late to school.  (or) You had better start early to reach school in time.'),
                  ((34, 5, 6), 'You should use the dustbins and not throw plastic bottles on the playground.')])
B.g(1, (34, 7), [((34, 8), 'run away (escape): The thief ran away when he saw the police.'),
                 ((34, 9), 'come around (visit / return): Please come around to my house this evening.'),
                 ((34, 10), 'pick up (lift / collect): Please pick up the waste paper from the floor.'),
                 ((34, 11), 'look at (direct one’s eyes towards): Look at the beautiful rainbow in the sky.'),
                 ((34, 12), 'fly over (fly above): A flock of birds flew over our village.')])
B.g(1, (34, 13), [((34, 14, 18), 'i) – b (stop sleeping)  ii) – d (go down into something)  iii) – c (remain on the surface)  iv) – a (become exhausted)')], mk=2)
B.g(1, (34, 19), [((34, 20), 'conducter → conductor'), ((34, 21), 'royalti → royalty'), ((34, 22), 'serman → sermon'),
                  ((34, 23), 'precius → precious'), ((34, 24), 'pasenger → passenger')])
B.ce(1, (34, 26, 32),
     '10th May, 1994, Pretoria                                                    11:00 p.m.\n'
     'Dear Diary,\n'
     'Today is the most memorable day of my life. I took the oath as the first black President of South Africa at the Union Buildings in Pretoria. '
     'Leaders and ambassadors from more than 140 countries came to share our joy. Reporters crowded around me for interviews. My message to them was simple: “Let freedom reign. Never, never again shall this beautiful land experience the oppression of one by another.”\n'
     'I remembered the thousands of patriots who sacrificed their lives for this day. I felt humble and grateful.\n'
     'Now the real work begins. My plan of action:\n'
     '1. Unite all races – black and white – as one rainbow nation, with equal rights for all.\n'
     '2. Provide free and good education to every child.\n'
     '3. Build houses, supply drinking water, electricity and health care to the poor.\n'
     '4. Create jobs and reduce poverty.\n'
     '5. Heal the wounds of apartheid through truth, forgiveness and reconciliation.\n'
     'The road ahead is long, but with the support of my people I am confident. I feel tired, but very happy.\n'
     'Nelson Mandela', lid='en2')
B.ce(1, (34, 33, 37),
     'D.No. 3-45, Gandhi Nagar,\nGudur, SPSR Nellore Dist.\n12th January, 2027.\n\nDear Sravya,\n'
     'I am fine here and hope you are fine too. Recently I read the lesson “Nelson Mandela: Long Walk to Freedom”. Mandela fought relentlessly against apartheid and spent 27 years in prison for the freedom of his people. His story made me think about our own freedom fighters.\n'
     'India was ruled by the British for nearly 200 years. Thousands of brave men and women sacrificed their comforts, families and even their lives for our freedom. '
     'Mahatma Gandhi led the nation through truth and non-violence. Bhagat Singh, Rajguru and Sukhdev went to the gallows smiling. Subhas Chandra Bose formed the Indian National Army. Rani Lakshmi Bai fought bravely in 1857. Alluri Sitarama Raju fought for the tribal people of our Andhra region, and Potti Sriramulu gave up his life for Andhra State.\n'
     'Because of their sacrifices we enjoy freedom today. We must respect our national flag, study well, obey the laws and serve our country.\n'
     'Please read the stories of our freedom fighters during your holidays. Convey my regards to Mummy and Daddy.\n\n'
     'Your loving brother,\nRavi.\n\nAddress on the envelope:\nTo\nB. Sravya, Class VIII,\nD.No. 3-45, Gandhi Nagar, Gudur.', lid='en2')

# ---------- LEVEL-2 : SHINING STAR (p35) ----------
B.g(2, (35, 3), [((35, 4), 'Let the project be finished before Friday.'), ((35, 5), 'Let the report be sent to me today.'),
                 ((35, 6), 'Was the lesson explained by the teacher?'), ((35, 7), 'Is the book being given by you?'),
                 ((35, 8), 'Will the treat be given by him?'), ((35, 9), 'Why are the fees paid by him?'), ((35, 10), 'Can the work be completed by Sarvaani?')])
B.g(2, (35, 11), [((35, 12, 16), 'i) – b (move towards the front)  ii) – c (jump into something)  iii) – d (stop trying)  iv) – a (become frightened)')], mk=2)

# ---------- The Ball Poem – LEVEL-1 (p36–38) ----------
B.rcr(1, [(36, 1, 16)], '1. Because his ball has bounced into the harbour and is lost; he is shocked and overcome by grief.\n'
      '2. The ball symbolises his childhood days (innocence) – losing it is his first experience of loss.\n'
      '3. B) harbour\n4. A) childhood memories\n5. A) The poet wants the boy to learn from his own experience.')
B.rcr(1, [(36, 17, 30)], '1. He is learning the “epistemology of loss” – what it means to lose something and how to bear it.\n'
      '2. It means facing the loss bravely, accepting it and moving on in life.\n3. B) desperate\n4. A) the understanding of loss\n5. B) accept loss and move on')
B.rcr(1, [(37, 1, 14)], 'Correct order: b, d, a, c, e\nb) First aid can save lives.\nd) Wound should be covered with bandage.\na) We shouldn’t panic.\nc) We should call Ambulance.\ne) We should learn first aid.', mk=2)
B.g(1, (37, 16), [((37, 17, 18), '(a) in → of  (b) has → have  (c) as → so  (d) celebrate → celebration', 'en4'),
                  ((37, 19, 21), '(a) what – correct  (b) some for → some of  (c) on – correct  (d) find → found   [also: was → were]', 'en5')], mk=2)
B.g(1, (37, 22), [((37, 23), 'when'), ((37, 24), 'for'), ((37, 25), 'for')])
B.g(1, (37, 26), [((37, 27), 'He told the members of his family that they would all go hungry that year.', 'en1'),
                  ((37, 28), 'The pilot asked the co-pilot if (whether) he could hear him.'),
                  ((37, 29), 'Siri said that she could still recall the typical fragrance of those flowers.')])
B.g(1, (37, 30), [((37, 31, 36), '(a) saw – observed  (b) Storm – cyclone  (c) huge – enormous  (d) enough – sufficient')], mk=2)
B.g(1, (38, 1), [((38, 2, 3), '(a) afraid × brave (fearless)  (b) near × far  (c) upwards × downwards  (d) confident × nervous (diffident)')], mk=2)
B.g(1, (38, 4), [((38, 5), 'uncertain'), ((38, 6), 'dangerous')])

# ---------- The Ball Poem – LEVEL-2 (p38–40) ----------
B.rcr(2, [(38, 9, 23)], '1. Into the water of the harbour.\n2. The boy’s grief at losing his ball – nothing, not even the promise of other balls, can console him.\n'
      '3. B) water\n4. B) worried\n5. A) the boy wants only his own ball')
B.rcr(2, [(38, 24, 39)], '1. He senses his first responsibility in a world of possessions – things are lost and money cannot buy them back.\n'
      '2. Loss is a part of life; money is external and cannot replace the value of things we love – we must learn to accept loss.\n'
      '3. B) responsibility\n4. B) external\n5. A) lost things cannot always be recovered')
B.rcr(2, [(39, 1, 15)], '1. He is learning the epistemology of loss – how to stand up (bear the loss) knowing that every man must one day lose something.\n'
      '2. His eyes are described as desperate.\n3. A) desperate\n4. A) face loss\n5. B) to recover from difficulties')
B.rcr(2, [(39, 16, 32)], 'Correct order: B, D, C, A, E\nB) Water is a valuable natural resource.\nD) Many places are facing water shortages.\n'
      'C) People should use water wisely in their daily lives.\nA) Rainwater harvesting is an effective way to conserve water.\nE) Saving water today will protect the future.', mk=2)
B.g(2, (39, 34), [((39, 35, 37), '(a) were → are  (b) in place → in place from  (c) ensuring → ensure  (d) superiority → superior', 'en5'),
                  ((40, 1, 5), '(a) princes → prince’s  (b) a → an  (c) wound → wounded  (d) profuse → profusely', 'en7')], mk=2)
B.g(2, (40, 6), [((40, 7), 'to'), ((40, 8), 'to'), ((40, 9), 'for')])
B.g(2, (40, 10), [((40, 11), 'Lencho told his wife that they were really going to get some water then.', 'en1'),
                  ((40, 12), 'The woman told her boys to come for dinner.', 'en1'),
                  ((40, 13), 'She told her father that Naveena was trying to help her.')])
B.g(2, (40, 14), [((40, 15, 18), '(a) brink – edge  (b) muster up – gathered  (c) courage – courage  (d) plunge – jump')], mk=2)
B.g(2, (40, 19), [((40, 20, 21), '(a) outwards × inwards  (b) still × moving  (c) soaring × falling (sinking)  (d) afraid × brave (fearless)')], mk=2)
B.g(2, (40, 22), [((40, 23), 'unable'), ((40, 24), 'successfully')])
B.ce(2, (40, 26, 29),
     'Mother: Did you see that? Our youngest son has finally flown!\n'
     'Father: Yes, I saw it. I was worried that he would never learn to fly.\n'
     'Mother: For days he stood on the ledge, afraid. His brothers and sister flew away, but he could not muster up courage.\n'
     'Father: We even called him a coward and threatened to let him starve there.\n'
     'Mother: Today I picked up a piece of fish and flew near him. I stopped just out of his reach.\n'
     'Father: That was clever! He must have been very hungry.\n'
     'Mother: Yes. Maddened by hunger, he dived at the fish. He fell, then spread his wings and soared!\n'
     'Father: I am proud of you. You knew that hunger would overcome his fear.\n'
     'Mother: Now he is flying with the whole family over the sea. He even landed on the water.\n'
     'Father: Let us teach him to dive for fish tomorrow. Our son is no longer afraid.\n'
     'Mother: Yes, he only needed a little push and a lot of love.')
B.ce(2, (40, 30, 32),
     'Wife: You look very tired. How was your flight from Paris?\n'
     'Pilot: It was the strangest night of my life. Over France I flew into huge black storm clouds.\n'
     'Wife: Oh God! Why didn’t you fly around them?\n'
     'Pilot: I did not have enough fuel to fly around them, so I took the risk and flew into the storm.\n'
     'Wife: Then what happened?\n'
     'Pilot: Everything went black. My compass and radio stopped working. I could not contact Paris control.\n'
     'Wife: How terrible! How did you find your way?\n'
     'Pilot: Suddenly I saw another aeroplane – a black one with no lights. Its pilot waved to me to follow him. I followed him like an obedient child.\n'
     'Wife: Thank God! Did you thank him?\n'
     'Pilot: When I came out of the clouds, I saw the runway lights and landed safely. But the black aeroplane had disappeared. The woman in the control centre said mine was the only aeroplane in the sky.\n'
     'Wife: Then who helped you?\n'
     'Pilot: I don’t know. It is a mystery. I am just grateful to be home with you.')
B.ce(2, (40, 33, 38),
     'Sunday, 14th July                                                               9:00 p.m.\n'
     'Dear Diary,\n'
     'Today is the happiest day of my life – I flew for the first time!\n'
     'Before the flight: For two days I stood alone on the ledge. My brothers and little sister flew away easily, but I was afraid that my wings would not support me. My family laughed at my cowardice and left me hungry. I felt lonely, ashamed and very hungry.\n'
     'Then my mother flew towards me with a piece of fish and stopped just out of my reach. Maddened by hunger, I dived at the fish. For a moment I was terrified and fell into space.\n'
     'After the flight: Suddenly my wings spread out. The wind rushed under me and I soared! I flew over the vast green sea with little ridges moving on it. I turned my beak sideways and cawed in amusement. My family flew around me, praising me. I even landed on the water – it did not swallow me!\n'
     'Now I feel proud, confident and free. I have learnt that fear goes away when we try.\n'
     'Young Seagull')
ITEMS = B.items
