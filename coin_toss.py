# FILE NAME - coin_toss.py
# NAME: Amy Nuessle
# DATE: March 2, 2026
# BRIEF DESCRIPTION:  Randomly return Heads or Tails. Random number between 1 and 100 (inclusive), if 51 or greater tails, Otherwise Heads
# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
########## ENTER YER CODE BELOW THIS LINE ##########
flip = random.randint(1, 100)
print("===== Coin Flipper =====")
if flip >= 51:
    print("Tails")
else:
    print("Heads")







########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? figuring out how to start, and confused which random function to use. Also made mistakes on the greater than 51 and where to use the colon. Sought help from the builder assistant







'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[x] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.
'''
