questions = [
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
              ["who is the president of the india?",
             "narendra", "rahul", "Indira", "Manmohan", "a"],
            
            ]

levels = [5000,"10 thousand","20 thousand","40 thousand","40 thousand","80 thousand","1.6 lakhs","3.2 lakhs","6.4 lakhs","12.8 lakhs","24 lakhs","50 lakhs","1 crore"]

i = 0 
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for rupees {levels[i]}")
    print(f"a.{question[1]}              b.{question[2]}")
    print(f"c.{question[3]}              d.{question[4]}")
    
    reply = input("Enter your correct answer(a to d) ")
    if reply == question[-1]:
        print("Coreect answer")
        
        totalprice = 0
        print(f"total price  which you won is {levels[i]}")
        money = levels[i]
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    
       
    elif money == levels[-1]:
        break
          
    else:
         print("Wrong answer!")
         break   
if (money == levels[6] ):
            print(f"Now you secured at {money[6]}")    
elif (money == levels[1] ):
            print(f"Now you secured at {money[1]}")
else : 
            print(f"You won the price of",money)