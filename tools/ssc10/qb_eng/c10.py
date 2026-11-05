# Study skills, jumbled sentences, grammar (His First Flight / Black Aeroplane / Anne Frank) – English_Final.pdf పేజీలు 72–77
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h import EB, S, IMG
B = EB(10, 'en3')
A4 = 'en4'

def addimg(path, cap):
    B.items[-1] = B.items[-1][:3] + (B.items[-1][3] + IMG(path, cap),) + B.items[-1][4:]

# ---------- LEVEL-1 : RISING STAR ----------
B.rcr(1, [(72, 3, 17)], 'i) Mathematics (40%).\nii) 20% of 200 = 40 students.\niii) b) Science\niv) a) 20 students (10% of 200)\n'
      'v) a) The number of students who preferred Mathematics is greater than those who preferred Science.')
addimg('eng/qb_subjects', 'Student Favourite Subjects (Survey of 200 Students)')
B.rcr(1, [(72, 18, 18), (73, 1, 12)], 'i) Research & Development (R&D) – 45%.\nii) 20%.\niii) b) Marketing\niv) c) Human Resources (HR) – 10%\n'
      'v) a) The budget allocated to R&D (45%) is more than the budget allocated to Marketing (25%).\n'
      '(Note: statement b is also true – Operations + HR = 30% > Marketing 25%; c is false.)')
addimg('eng/qb_budget', 'Annual Budget Allocation')
B.rcr(1, [(73, 13, 23)], 'Correct order: C, E, B, A, D\nC. On his way home from school, Rohan noticed a wallet near the bus stop.\nE. He opened it carefully and found an identity card inside.\n'
      'B. Instead of keeping the money, he took the wallet to the nearest police station.\nA. The owner was contacted and thanked Rohan for his honesty.\nD. His good deed was appreciated by everyone.', mk=2)
B.g(1, (73, 25), [((73, 26), 'The pilot followed a mysterious aeroplane which guided him safely.'),
                  ((73, 27), 'Anne had many friends who admired her cheerful nature.', A4),
                  ((73, 28), 'The seagull saw his family whose calls encouraged him.'),
                  ((73, 29), 'The young seagull, who had been afraid for many days, finally flew across the sea.'),
                  ((73, 30), 'The pilot saw a runway which appeared after he came out of the storm.'),
                  ((73, 31), 'Anne had a father whose encouragement gave her confidence.', A4),
                  ((73, 32), 'The mother seagull, who wanted him to fly, encouraged her son.'),
                  ((73, 33), 'The black aeroplane, which had guided the pilot, vanished suddenly.')])
B.g(1, (73, 34), [((73, 35), 'The aeroplane was landed safely by the pilot.'), ((73, 36), 'Her diary was called Kitty by Anne.', A4),
                  ((73, 37), 'The young seagull was praised by the family.'), ((73, 38), 'The aeroplane was surrounded by the storm.'),
                  ((73, 39), 'The sky was covered by (with) the clouds.')])
B.g(1, (74, 1), [((74, 2), 'The mother seagull told her son that he could fly then.'), ((74, 3), 'Anne said that she felt lonely sometimes.', A4),
                 ((74, 4), 'Anne’s father advised her to write regularly.  (or) Anne’s father said that she should write regularly.', A4),
                 ((74, 5), 'The pilot said that he could not see anything in the storm.'), ((74, 6), 'Anne said that her diary was her best friend.', A4)])
B.ce(1, (74, 7, 15), '1. ‘Fourth’ (in North American English).\n2. In the US and Canada, a quarter is a coin worth 25 cents.', mk=2)
B.ce(1, (74, 16, 25), '1. ‘Enough’ is used before plural or uncountable nouns.\n2. Sufficient.', mk=2)
B.ce(1, (74, 26, 38), '1. Uncountable.\n2. Valentina Tereshkova.', mk=2)
B.g(1, (74, 39, 40), [((74, 41), 'fly a flag (display a flag on a pole): We fly the national flag on Independence Day.'),
                      ((75, 1), 'fly into a rage (become very angry): The king flew into a rage when he heard the news.'),
                      ((75, 2), 'fly along (move quickly): The bus flew along the empty highway.'),
                      ((75, 3), 'fly high (be very successful): Our school team is flying high this year.'),
                      ((75, 4), 'fly the coop (escape from a place): The parrot flew the coop when the cage was left open.')])
B.g(1, (75, 5), [((75, 6, 10), 'i) – a (progress)  ii) – d (deplete the supply)  iii) – b (escape)  iv) – c (contact)'),
                 ((75, 11, 15), 'i) – a (escape from a place)  ii) – c (move quickly / suddenly)  iii) – d (become very angry)  iv) – b (display a flag on a pole)')], mk=2)
DI = S(75, 17, 19) + '\n'
B.q(1, 8, DI + S(75, 20, 25),
    'Favourite Reading Materials of Students\n'
    'The table shows the favourite reading materials of 129 students (65 boys and 64 girls). Story books are the most popular, liked by 42 students – 18 boys and 24 girls. '
    'Science books come second with 32 students; interestingly, more boys (20) than girls (12) prefer them. Newspapers are read by 30 students, with girls (18) ahead of boys (12). '
    'Comics are the least popular, with 25 students (15 boys and 10 girls). On the whole, girls prefer story books and newspapers, while boys prefer science books and comics. '
    'It is encouraging that students read a variety of materials.')
B.q(1, 8, DI + S(75, 26, 32),
    'School Library Book Issue (One Week)\n'
    'The table shows the number of books issued by the school library in one week. Fiction is the most popular category: 125 fiction books were issued, with the highest number on Friday (30) and the lowest on Thursday (20). '
    'Science books come next with 96 issues; the demand was highest on Thursday (22). History is the least borrowed category with 75 books, ranging from 12 on Monday to 18 on Thursday. '
    'Altogether 296 books were issued during the week. Thursday was the only day when science and history books were borrowed more than on other days, while fiction stayed popular throughout the week.')
B.q(1, 8, DI + S(75, 33, 39),
    'Participation in School Clubs\n'
    'The table shows how many boys and girls take part in five school clubs. Altogether 202 students (101 boys and 101 girls) are members. '
    'The Sports Club is the most popular with 48 members, most of them boys (30). The Science Club comes second with 42 members, again with more boys (26) than girls (16). '
    'The Eco Club has 40 members, with slightly more girls (22). The Literary Club (37) and the Music Club (35) are preferred more by girls – 25 and 20 girls respectively. '
    'Thus boys show more interest in sports and science, while girls are more active in literary, music and eco clubs.')

# ---------- LEVEL-2 : SHINING STAR ----------
for (a, b), ans in [((76, 3), 'C, E, A, B, D\nC. Scientists successfully launched a weather satellite.\nE. The satellite began sending information about clouds and storms.\nA. Meteorologists used the data to improve weather forecasts.\nB. Farmers received timely warnings about heavy rainfall.\nD. The successful mission helped people prepare for disasters.'),
                    ((76, 14), 'E, B, C, D, A\nE. The school organised a science exhibition.\nB. Different groups displayed working models.\nC. Visitors asked questions and appreciated the creative ideas.\nD. The judges evaluated each project carefully.\nA. Finally, the best models received prizes during the closing ceremony.'),
                    ((76, 24), 'D, B, E, A, C\nD. People gathered in an open field to watch a solar eclipse.\nB. Scientists distributed special glasses for safe viewing.\nE. The Moon moved between the Earth and the Sun, making daylight fade.\nA. Everyone watched the rare event with excitement.\nC. After a few minutes, sunlight returned.'),
                    ((77, 1), 'C, D, B, E, A\nC. Students assembled in the playground early in the morning.\nD. Each student received a sapling and planting tools.\nB. Teachers explained the importance of protecting the environment.\nE. Together they planted trees around the campus and watered them.\nA. Everyone promised to care for the plants throughout the year.')]:
    end = {(76, 3): 13, (76, 14): 23, (76, 24): 33, (77, 1): 10}[(a, b)]
    rng = [(a, b, end)] if (a, b) != (76, 3) else [(76, 3, 13)]
    B.rcr(2, rng, 'Correct order: ' + ans, mk=2)
B.g(2, (77, 12), [((77, 13), 'Anne admired teachers who encouraged students to learn.', A4),
                  ((77, 14), 'The pilot, who reached the airport safely, thanked the unknown pilot.'),
                  ((77, 15), 'Anne lived in Amsterdam, which was her home before hiding.', A4),
                  ((77, 16), 'The seagull watched his brothers whose confident flying amazed him.'),
                  ((77, 17), 'Anne Frank was a talented girl whose diary inspired millions.', A4),
                  ((77, 18), 'The pilot entered the storm which was full of dark clouds.'),
                  ((77, 19), 'The young seagull found courage which changed his life forever.'),
                  ((77, 20), 'The mysterious pilot, who had helped the narrator, disappeared suddenly.')])
B.g(2, (77, 21), [((77, 22), 'Her homework was completed by Anne before writing in her diary.', A4),
                  ((77, 23), 'The lost aeroplane was guided by the mysterious pilot.'),
                  ((77, 24), 'Anne was encouraged by her father to write regularly.', A4),
                  ((77, 25), 'The landing lights were switched on by the pilot.'),
                  ((77, 26), 'Anne’s handwriting was praised by her teacher.', A4),
                  ((77, 27), 'The hungry young seagull was fed by the mother seagull.')])
B.g(2, (77, 28), [((77, 29), 'The control officer said that no other aeroplane had been flying that night.'),
                  ((77, 30), 'Anne said that she wanted to become a writer.', A4),
                  ((77, 31), 'The young seagull said that he was afraid to fly.'),
                  ((77, 32), 'The pilot said that he had enough fuel.'),
                  ((77, 33), 'The pilot said that he would land safely that night.'),
                  ((77, 34), 'Anne said that her classmates often made her laugh.', A4)])
ITEMS = B.items
