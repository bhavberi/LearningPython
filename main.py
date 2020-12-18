import csv
import time
import os
import webbrowser
import warnings
from getpass import getpass

warnings.simplefilter("error", category=Warning)

#Importing the other user-defined modules
import login
import quiz_main

def read(level='level -1'): #Function to display the module of the particular level
    with open(level+'.txt','r') as ob:
        print(ob.read())
    if level=='level -1': #For final level
        time.sleep(1)
        quiz_only(level)
        return
    time.sleep(6) #Time given for reading the text
    input("Press any key to continue to the quiz -> ")
    quiz_only(level) #Proceeding for conducting the quiz

def quiz_only(level):
    passpercent=65
    if level=='level -1':
        passpercent=80 #More Pass Percentage for the final quiz
    quiz_main.main(level[6:],passpercent)
    if quiz_main._pass:
        print("\n\t~~~ Passed !! ~~~")
        if level!='level -1':
            print("You have passed",level)
        level_increase() #After passing the quiz, increasing the level of the user
        print()
    else:
        print("\n\tFail!! \n\t~~Please Try Again~~")
        menu()

def exit(): #Exit function
    print("\nThanks for using this software.\n\tBy Bhav and Amanvir")
    time.sleep(1.7)
    print("\t\t   ^ ^  ")
    print("\t\t ! ` ` !")
    print("\t\t    '   ")
    print("\t\t   <->  ")
    print()
    print("You can download the files from the link\nhttps://github.com/bhavberi/LearningPython\n\tOr\nhttps://repl.it/@bhavberi/LearningPython")
    time.sleep(2.8)
    os._exit(1) #For closing the program forcefully.

def show_all_logindetails(): #For admin to see the details of all the users enrolled till now.
    obr=open('Login Details.csv','r')
    read=csv.reader(obr)
    print('Serial\tUsername\t Next Level\t Package Type\t Password')
    print('~~Name \t\tPhone Number\tEmail \t\tCity')
    count=0
    for i in read:
        count+=1
        print()
        print('    ',count,'\t',i[0],'\t',i[2],'\t',i[3],'\t',i[1])
        print('~~',i[4],'\t',i[6],'  \t',i[5],'\t',i[7])
    menu()

def web():
    print()
    print("For Github link(For the Source Code), press 1")
    print("For repl.it link(For online interpreter), press 2")
    ch=int(input('-> '))
    print()
    if ch==1:
        print('https://github.com/bhavberi/LearningPython')
        print('\nThis is the Github link, either copy it and then paste in your browser,\nOr enter 9 to open the link directly in your browser.\nPress any other key to go back to menu.')
        ch1=input('-> ')
        if ch1=='9':
            webbrowser.open_new('https://github.com/bhavberi/LearningPython')
            time.sleep(3.1)
            input('To continue back, press enter key.')
            menu()
            return
        else:
            menu()
            return
    elif ch==2:
        print('https://repl.it/@bhavberi/LearningPython')
        print('\nThis is the Repl link, either copy it and then paste in your browser,\nOr enter 9 to open the link directly in your browser.\nPress any other key to go back to menu.')
        ch1=input('-> ')
        if ch1=='9':
            webbrowser.open_new('https://repl.it/@bhavberi/LearningPython')
            time.sleep(3.1)
            input('To continue back, press enter key.')
            menu()
            return
        else:
            menu()
            return
    else:
        print("Wrong Entry.")
        menu()
        return

def level_increase():
    global username,user_details
    fields=['username','password','level','package','name','email','phone','city']

    obw=open('Login_Details.csv','w',newline='') #Another file to which details will be first written and then this file will be renamed.
    data=csv.DictWriter(obw,fieldnames=fields)

    obr=open('Login Details.csv','r')
    read=csv.reader(obr)

    for i in read:
        d=dict() #Dictionary with the details of users with modified level also
        if i[0].lower()==username:
            level=i[2]
            if level=='Over':
                level='level 1'
            elif level=='level -1':
                level='Over'
            elif level=='level 2':#Last level
                level='level -1'
            else:
                level='level '+str(int(level[6:])+1)

            d['username']=i[0]
            d['password']=i[1]
            d['level']=level
            d['package']=i[3]
            d['name']=i[4]
            d['email']=i[5]
            d['phone']=i[6]
            d['city']=i[7]
            
            data.writerow(d)
            
        else:       
            d['username']=i[0]
            d['password']=i[1]
            d['level']=i[2]
            d['package']=i[3]
            d['name']=i[4]
            d['email']=i[5]
            d['phone']=i[6]
            d['city']=i[7]
            
            data.writerow(d)
    obw.close()
    obr.close()    
    os.remove('Login Details.csv')
    os.rename('Login_Details.csv','Login Details.csv')
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        for i in data:
            if i[0].lower()==username:
                user_details=i #Updating the user details which the program is using.
    menu()

def update_password():
    global username,user_details
    fields=['username','password','level','package','name','email','phone','city']

    obw=open('Login_Details.csv','w',newline='') #Another file to which details will be first written and then this file will be renamed.
    data=csv.DictWriter(obw,fieldnames=fields)

    obr=open('Login Details.csv','r')
    read=csv.reader(obr)

    for i in read:
        d=dict() #Dictionary with the details of users with modified level also
        if i[0].lower()==username:

            while True:
                try:
                  password=getpass("Enter password(min. 6 digits long) (Secured entry) -> ")
                except:
                  password=input("Enter password(min. 6 digits long) -> ")
                if len(password)<6:
                    print("\nPassword must be atleast 6 letters long")
                    continue
                print('\nEntered Password -> ',end='')
                print('*'*len(password))
                try:
                  cpass=getpass("Confirm you password (Secured entry) -> ")
                except:
                  cpass=input("Confirm you password -> ")
                if cpass==password:
                    break
                print("\nOriginal and Confirmatory Password's doesn't match\nPlease enter again.")
                ch=input('To try again, press 1\nElse press enter key')
                if ch!='1':
                  menu()
                  return
            
            d['username']=i[0]
            d['password']=password+'#ab'
            d['level']=i[2]
            d['package']=i[3]
            d['name']=i[4]
            d['email']=i[5]
            d['phone']=i[6]
            d['city']=i[7]
            
            data.writerow(d)
            
        else:       
            d['username']=i[0]
            d['password']=i[1]
            d['level']=i[2]
            d['package']=i[3]
            d['name']=i[4]
            d['email']=i[5]
            d['phone']=i[6]
            d['city']=i[7]
            
            data.writerow(d)
    obw.close()
    obr.close()    
    os.remove('Login Details.csv')
    os.rename('Login_Details.csv','Login Details.csv')
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        for i in data:
            if i[0].lower()==username:
                user_details=i #Updating the user details which the program is using.
    menu()

def menu(): #Main menu function from where all other functions are called.

    print()
    if user_details[2]=='Over':
        print("You have completed your course.\n\nTo restart the course enter 1 or 0\nElse press Enter key")
        print("To update your passord, press 2\nElse press Enter key")
        i=input("-> ")
        if i=='0' or i=='1':
            level_increase()
        elif i=='2':
            update_password()
            menu()
        else:
            exit()
    if user_details=='admin':
        print("To Continue to the module and then quiz, press 1")
        print("To continue to the quiz, press 9")
        print("To see the login details of all the users till now, press 5")
    elif user_details[3]=='Complete':
        print("To Continue to the module and then quiz, press 1")
        print("To update your passord, press 2")
    else:
        print("To continue to the quiz, press 9")
        print("To update your passord, press 2")
    print("For Source File/Online Interpreter of this program, press 0")
    print("Else press any other key to exit")
    ch=input("-> ") #Input of the choice of the user
    
    if ch.isdigit():
        choice=int(ch)
    else:
        choice=-1
    
    if choice==-1:
        exit()
    elif choice==0:
        web()
    elif choice==2:
        if user_details!='admin':
            update_password()
        else:
            exit()
    elif choice==1:
        if user_details=='admin':
            level_ask='level '+input("Enter number of level to see(For final, enter -1) : ")
            read(level_ask)
        else:
            if user_details[3]=="Quiz":
                exit()
            read(user_details[2])
    elif choice==9:
        if user_details=='admin':
            level_ask='level '+input("Enter number of level to see(For final, enter -1) : ")
            quiz_only(level_ask)
        else:
            if user_details[3]=='Complete':
                exit()
            if user_details[2]=='level -1':
                read(user_details[2])
            else:
                quiz_only(user_details[2])
    elif choice==5:
        if user_details=='admin':
            show_all_logindetails()
        else:
            exit()
    else:
        exit()

def welcome():
    print()
    time.sleep(0.5)
    print('\t\tA')
    time.sleep(1.5)
    print('\t\t\t&')
    time.sleep(1.5)
    print('\t\t\t\tB')
    time.sleep(1.5)
    print('\t\tSoftwares')
    time.sleep(0.7)
    print()
    q=0
    while q<29:
      print('-~',end='')
      q+=1
    time.sleep(1.5)
    print('\n')
    time.sleep(1.5)
    print("This software is developed by 'Bhav Beri' & 'Amanvir Singh'\n")
    time.sleep(0.9)
    q=0
    while q<29:
      print('-~',end='')
      q+=1
    time.sleep(1.5)
    print('\n')
    time.sleep(1.5)

#Start of the execution of the main file            
welcome()

#Calling login module and checking the initials of the user
login.login()
username=login.username()
user_details=''
if username=='adminab' or username=='computer':#For admin
    user_details='admin'
with open('Login Details.csv','r') as ob:
    data=csv.reader(ob)
    for i in data:
        if i[0].lower()==username:
            user_details=i

#After logining in of the user, start of the main module for the quizzes and the learning part. 
menu()
