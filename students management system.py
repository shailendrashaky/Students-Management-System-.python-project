# Simple Student Management System (No Roll No, No Storage)

print("_______________________________")

print("\n *****WELCOME TO STUDENT MANAGEMENT SYSTEM*****")

l=["abhishek","sonam","ashish"]

def view_list():
    for i in range(len(l)):
        print(l[i])

def add_data():
    x=input("\n Enter the name:")
    l.append(x)
    print("name added sucessfully...")



def remove_data():
    name=input("Enter the name to remove:")
    if name in l:
        l.remove(name)
        print("record deleted suceesfully...")

    else:
        print("record not found...")


def search_data():
    s=input("\nEnter the name to search:")
    if s in l:
        print("name found!!!")
    else:
        print("record not found....")

while True:
    print("______________________")
    print("                                          ")
    print("Please choose any one options:\n")
    print("1. To view student list")
    print("2. To add new list")
    print("3. To remove the data")
    print("4. To search data")
    print("5. Exit")

    ch=int(input("\nEnter your choice..."))
    if ch==1:
        view_list()
    elif ch==2:
        add_data()
    elif ch==3:
        remove_data()
    elif ch==4:
        search_data()
    elif ch==5:
        exit()
    else:
        print("wrong input")
    g=input("Do U Continue this (y/n):")
    print("____________________")

    if(g=="y"):
        continue
    elif(g=="n"):
        break
    

    
