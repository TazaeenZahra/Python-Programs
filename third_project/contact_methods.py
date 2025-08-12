
contact={}

def save_contact():
    with open("Contact Book.txt","a") as f:
        for name,info in contact.items():
            f.write(f"{name.capitalize()},{info["phone number"]},{info["Email"]}\n")

def Addcontact():
    try:
        print("To exit, press e")
        while True:
            name=input("Enter name: ")
            if name == "e":
                break
            phone=input("Enter phone number: ")
            emial=input("Enter email: ")
            
            contact[name]={}
            contact[name]["phone number"]=phone
            contact[name]["Email"]=emial
            print(f"{name} added successfully!\n")
    except ValueError:
            print("invalid input\n")

def searchContact():
    name=input("Enter name: ")
    name=name.capitalize()
    with open("Contact Book.txt","r") as f:
        line=f.readline()
        while(line !=""):
            if name in line:
                print(f"contact found\n\n{line}\n")
                break
            line=f.readline()
        else:
            print("Contact not found\n")

def viewAllContacts():
    with open("Contact Book.txt","r") as f:
        print(f.read())

def deleteContact():
    name=input("Enter name: ")
    name=name.capitalize()
    Newlines=[]
    with open("Contact Book.txt", "r") as f:
        lines = f.readlines()
    if not any(name in line for line in lines):
        print(f"Contact '{name}' not found!")
        return 
    for line in lines:
        if name not in line:
            Newlines.append(line)
   
    with open("Contact Book.txt","w") as f:
        f.writelines(Newlines) 
    print(f"{name} delete successfully")   
           