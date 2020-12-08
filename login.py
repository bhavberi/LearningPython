import csv
import os
import random
import time
from getpass import getpass
import warnings

#Exit function to be called wherever program is terminating

warnings.simplefilter("error", category=Warning)

def private():
    s=''
    letters='qwertyuioplkjhgfdsazxcvbnm'
    letters+=letters.upper()
    letters+='234567890'
    letters+="!@#$%&*?/"
    for i in range(8):
        s+=random.choice(letters)
    return 'AB '+s
passcode,correct = 0,private()
user = ''

def login(): #For Calling
    global passcode,correct
    if __name__ == '__main__': #Checking whether program called directly or by any other module
        a=admin()
        if a==True:
            passcode=correct
            return main()
    else:
        passcode=correct
        return main()
    os.system('cls')

count=0
def main(): #Main method of login.py
    global passcode,correct
    if passcode!=correct:
        print("Fake")
        os._exit(1)
        return False
    global count
    print("\nIf you want to login as student, enter 1")
    print("If you want to signup as student, enter 2")
    print("If you want to login as admin, enter 3")
    print("To exit, enter 0")
    ch=input("-> ")
    if ch=='':
      choice=-1
    else :
      choice=int(ch)
    if choice==1:
        choice=0
        if signin()==True:
            return True
        else:
            return False
    elif choice==2:
        choice=0
        signup()
        return main()
    elif choice==3:
        choice=0
        if admin()==True:
            return True
        else:
            return False
    elif choice==0:
        choice=0
        print("\nThanks for using this software.\n\tBy Bhav and Amanvir")
        time.sleep(1.7)
        print("\t\t   ^ ^  ")
        print("\t\t ! ` ` !")
        print("\t\t    '   ")
        print("\t\t   <->  ")
        time.sleep(1.8)
        os._exit(1)
    else:
        count+=1
        if count>3:
            print("\nWrong inputs more than 3 times")
            print("Program Terminating")
            time.sleep(2.5)
            os._exit(1)
        else:
            print("Please select correct option")
            main()

def signup(): #For signup of student
    fields=['username','password','level','package','name','email','phone','city']
    d=dict()

    ob=open('Login Details.csv','a+',newline='')

    print('\n',end='')
    while True:
        print("Enter the username which you want to take(Atleast 3 letters long)\n(Condition to availability)")
        username=input("-> ")
        if len(username)<3:
            print("\n")
            continue
        if username_checker(username):
            break
        else:
            print("\nUsername not available\nPlease select any other username")

    while True:
        name=input("\nEnter your full name -> ")
        if len(name)<1:
            print("\n")
            continue
        else:
            break
    
    while True:
        email=input("Enter your full email (in form of abc@xyz.pqr) -> ")
        if len(email)<5:
            print("\n")
            continue
        if email_checker(email):
            break
        else:
            print("Please try again")

    while True:
        phone=input("Enter your phone number(in form of ABCDEFGHIJ) -> ")
        if phone_checker(phone):
               break
    
    while True:
        city=input("\nEnter your city name -> ")
        if len(city)<1:
            print("\n")
            continue
        else:
            break
        
    while True:
        try:
          password=getpass("Enter password(min. 6 digits long) -> ")
        except:
          password=input("Enter password(min. 6 digits long) -> ")
        if len(password)<6:
            print("\nPassword must be atleast 6 letters long")
            continue
        print('\nEntered Password -> ',end='')
        print('*'*len(password))
        try:
          cpass=getpass("Confirm you password -> ")
        except:
          cpass=input("Confirm you password -> ")
        if cpass==password:
            break
        print("\nOriginal and Confirmatory Password's doesn't match\nPlease enter again.")
    level='level 1'
    while True:
        print("\nEnter 1 for quizzes only package\nEnter 2 for complete package")
        p=(input("-> "))
        if len(p)==1 and p.isdigit():
            break
    p=int(p)
    if p == 1:
          package="Quiz"
    elif p==2:
          package='Complete'
    else:
          package='Complete'
          print("Wrong Input\nYour package has been set to Complete")

    cap_count=0
    while True:
        cap=captcha(random.randint(5,8))
        cap_count+=1
        print("Please enter this captcha (Case Sensitive) \nfor verification that user is not robot")
        print(cap)
        cap1=input('-> ')
        if cap1==cap:
            break
        print("\nWrong Captcha Entered")
        if cap_count==3:
            print("\nCaptcha validation failed")
            print("Program Terminating")
            time.sleep(2.5)
            os._exit(1)
        print("You have only",3-cap_count,'chances left')
    
    d['username']=username
    d['password']=password
    d['level']=level
    d['package']=package
    d['name']=name
    d['email']=email
    d['phone']=phone
    d['city']=city
    
    data=csv.DictWriter(ob,fieldnames=fields)
    data.writerow(d)
    ob.close()
def username_checker(username):
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        if username=='adminab' or username=='computer' or username=='admin':
            return False
        for i in data:
            if i[0]==username:
                return False
        return True 
def email_checker(email):
    email.strip()
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        for i in data:
            if i[5]==email:
                print("\nEmail already exists")
                return False
    for i in range(len(email)):
        if email[i]=='@':
            a=email[i+1:]
            for j in range(len(a)):
                if a[j]=='.':
                    b=a[j+1:]
                    if b!='':
                        return True
                    else:
                        break
    print("\nPlease check your email")
    return False
def phone_checker(phone):
    if len(phone)<10 or len(phone)>10:
           print("\nEnter complete phone number of 10 digits\nPlease try again")
           return False
    if not phone.isdigit():
           print("\nPlease enter correct phone number")
           return False
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        for i in data:
            if i[6]==phone:
                print("\nPhone Number already exists\nPlease try Again")
                return False
    return True
def captcha(l):
    s=''
    letters='qwertyuiplkjhgfdsazxcvbnm'
    letters+=letters.upper()
    letters+='123456789'
    letters+="!@$%^&*?/'"
    for i in range(l):
        s+=random.choice(letters)
    return 'AB '+s

def admin(): #For login of Admin
    global count,user
    count+=1
    if count>4:
        print("Entered wrong information more than 3 times !!!")
        time.sleep(2.5)
        os._exit(1)
    username=input("Enter username to login with (as admin) -> ")
    username.lower()
    if username!='adminab' and username!='computer':
        print("Wrong Username")
        admin()
    try:
      password = getpass("Enter password for username "+username+" -> ")
    except:
      password = input("Enter password for username "+username+" -> ")
    print('\n',end='')
    cap_count=0
    while True:
        cap=captcha(random.randint(6,8))
        cap_count+=1
        print("\nPlease enter this captcha (Case Sensitive) \nFor verification that user is not robot")
        print(cap)
        cap1=input('-> ')
        if cap1==cap:
            break
        print("\nWrong Captcha Entered")
        if cap_count==3:
            print("\nCaptcha validation failed")
            print("Program Terminating")
            time.sleep(2.5)
            os._exit(1)
        print("You have only",3-cap_count,'chances left')
    if username=='adminab' and password=='qwerty':
        print("Admin Logged In")
        time.sleep(2.5)
        user=username
        return True
        #os._exit(1)
    elif username=='computer' and password=='010101':
        print("Admin Logged In")
        time.sleep(2.5)
        user=username
        return True
        #os._exit(1)
    else:
        print("\nWrong Password ")
        admin()

def signin(): #For login of student
    global count
    count+=1
    if count>4:
        print("Entered wrong information more than 3 times !!!")
        print("Program Terminating")
        time.sleep(2.5)
        os._exit(1)
    username=(input("Enter the username of the student -> ")).lower()
    try:
      password = getpass("Enter password -> ")
    except:
      password = input("Enter password -> ")
    print('\n',end='')
    cap_count=0
    while True:
        cap=captcha(random.randint(6,8))
        cap_count+=1
        print("\nPlease enter this captcha (Case Sensitive) \nFor verification that user is not robot")
        print(cap)
        cap1=input('-> ')
        if cap1==cap:
            break
        print("\nWrong Captcha Entered")
        if cap_count==3:
            print("\nCaptcha validation failed")
            print("Program Terminating")
            time.sleep(2.5)
            os._exit(1)
        print("You have only",3-cap_count,'chances left')
    with open('Login Details.csv','r') as ob:
        data=csv.reader(ob)
        for i in data:
            if i[0].lower()==username:
                if i[1]==password:
                    print("\nLOGGED IN ")
                    time.sleep(3.5)
                    global user
                    user=username
                    return True
                    #os._exit(1)
    print("\nWrong Username or Password Information")
    signin()

def username():
    global user
    return user

if __name__ == '__main__':
    login()
