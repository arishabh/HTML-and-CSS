import random

userno = int(input("What are the number of things you want to add: "))
userlist = []

for i in range (userno):
    print ("What is your item number:",(i+1))
    userlist.append(input())

while userlist:    
    print("So this is your current list:",userlist)
    remove = random.choice(userlist)
    print("Here is the item to remove",remove)
    response = input("Do you want to remove this item? (y/n): ")      
    if (response == 'y'):
        userlist.remove(remove)
    print()  
