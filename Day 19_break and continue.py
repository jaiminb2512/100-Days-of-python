#day 19

#break statement
for i in range(12):
    if (i == 10):
        print("This is point break the loop")
        break
    print("5 *",i,"=",5*i)


#continue statement
#this statement use to skip particular any point

for i in range(12):
    if (i == 10):
        print("This is point loop will skip that point")
        continue
    print("5 *", i, "=", 5 * i)
