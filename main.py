# while loops :
i=1
while i<=10:
   i+=1
   if i == 8:
       break
print(i)
print("the loop has ended")


# for loops
for letter in "fatima" :
    print (letter)


buddies =["hhghh" , "lllllll" ,"kkkkkk"]
for buddy in buddies :


    print(buddy)
print(len("buddies"))


for x in range(4,11):
        print(x)

for w in range (len(buddies)):
    print(w)


for w in range (3):
    print(w)

    for index in range (6):
        if index % 2 == 0 :
          print(index, " is an even num")
        else:
          print (index, "is an odd num")

buddies = ("ali ", "ahmed"  ,"lofy")
for onepiece in buddies :
    if  onepiece == "zoro":
        print(onepiece ,"is my friend")
        break
    else:
        print(onepiece, "is not found")


buddies = ("ali ", "ahmed", "zoro" ,"lofy")
for onepiece in buddies :
    if  onepiece == "zoro":
        print(onepiece ,"is my friend")
        break
    else:
        print(onepiece, "is not found")



for x in range (5, 9) :
           if x ==6:
               continue
           print(x, "is the num")

