import login
import csv
import time
import os
import quiz_main

def read(level='level -1'):
    with open(level+'.txt','r') as ob:
        print(ob.read())
    if level=='level -1':
        time.sleep(1)
        quiz_only(level)
        return
    time.sleep(6)
    input("Press any key to continue to the quiz -> ")
    quiz_only(level)

def quiz_only(level):
    passpercent=65
    if level=='level -1':
        passpercent=80
    quiz_main.main(level[6:],passpercent)
    if quiz_main._pass:
        print("\n\t~~~ Passed !! ~~~")
        if level!='level -1':
          print("You have passed",level)
        level_increase()
        print()
    else:
        print("\n\tFail!! \n\t~~Please Try Again~~")
        menu()

def exit():
    print("\nThanks for using this software.\n\tBy Bhav and Amanvir")
    time.sleep(1.7)
    print("\t\t   ^ ^  ")
    print("\t\t ! ` ` !")
    print("\t\t    '   ")
    print("\t\t   <->  ")
    time.sleep(1.8)
    os._exit(1)
def show_all_logindetails():
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

    

def level_increase(): #Max. Level set to 1 till now To be changed afterwards
    global username,user_details
    fields=['username','password','level','package','name','email','phone','city']

    obw=open('Login_Details.csv','w',newline='')
    data=csv.DictWriter(obw,fieldnames=fields)

    obr=open('Login Details.csv','r')
    read=csv.reader(obr)

    for i in read:
        d=dict()
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
                user_details=i
    menu()

def menu():
    print()
    if user_details[2]=='Over':
      print("You have completed your course.\nTo restart the course enter 1 or 0\nElse press Enter key")
      i=input("-> ")
      if i=='0' or i=='1':
          level_increase()
      else:
          exit()
    if user_details=='admin':
        print("To Continue to the module and then quiz, press 1")
        print("To continue to the quiz, press 9")
        print("To see the login details of all the users till now, press 5")
    elif user_details[3]=='Complete':
        print("To Continue to the module and then quiz, press 1")
    else:
        print("To continue to the quiz, press 9")
    print("Else press any other key to exit")
    ch=input("-> ")
    if ch.isdigit():
      choice=int(ch)
    else:
      choice=0
    if choice==0:
        exit()
    elif choice==1:
        if user_details=='admin':
            level_ask='level '+input("Enter number of level to see(For final, enter -1) : ")
            read(level_ask)
        else:
            read(user_details[2])
    elif choice==9:
        if user_details=='admin':
            level_ask='level '+input("Enter number of level to see(For final, enter -1) : ")
            quiz_only(level_ask)
        else:
            quiz_only(user_details[2])
    elif choice==5:
      show_all_logindetails()
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
            
welcome()

login.login()
username=login.username()
user_details=''
if username=='adminab' or username=='computer':
    user_details='admin'
with open('Login Details.csv','r') as ob:
    data=csv.reader(ob)
    for i in data:
        if i[0].lower()==username:
            user_details=i
  
menu()
