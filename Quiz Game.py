#Quiz Game
Question={"Elon Musk is the founder of Tesla.":"Yes",
          "Apple has the highest networth across the world in the year 2022.":"Yes",
          "Google was Founded in the year 2000.":"No",
          "Seoul is not the capital city of South Korea.":"No",
          "is Bitcoin a perfect investment,Yes or No.":"Yes",
          "Apia is the capital city of San Marimo.":"No",
          "Rabat is the capital city of Morocco.":"Yes",
          "SteveJobs is the founder of Apple Inc.":"Yes",
          "Delhi is the India's largest city by population.":"No",
          "The Python Programming Language was created by Guido van Rossum.":"Yes",
          "Windows was launched in the year 1980.":"No",
          "El Apostol was the first known animated movie.":"Yes",
          "The current CEO of Dell is Enrique Lores.":"No",
          "The net worth of the Swiss Bank is much greater than any bank.":"No"}
import random
Questionlist=[]
while(len(Questionlist)!=5): # list of 5 questions
    i=random.choice(list(Question.keys())) #Choose Random question from question pool and make a list of it
    if(i not in Questionlist):
        Questionlist.append(i) # make a list of random qustions
score=0
print(""" 8""""8                  8""""8                    
8    8 e   e e  eeeee   8    " eeeee eeeeeee eeee 
8    8 8   8 8  "   8   8e     8   8 8  8  8 8    
8    8 8e  8 8e eeee8   88  ee 8eee8 8e 8  8 8eee 
8 ___8 88  8 88 88      88   8 88  8 88 8  8 88   
8e8888 88ee8 88 88ee8   88eee8 88  8 88 8  8 88ee 
                                                   """)
for i in Questionlist:
    print("\n"+i)
    q=input("\nEnter Yes or No: ")
    if(q==Question[i]):
        print("\nRight answer! +1 point")
        score+=1
    else:
        print("\nWrong answer!")
print("\nTotal Score is :",score)
print("Thanks for Playing")