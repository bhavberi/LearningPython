import random
import os
import time
#Importing Login module
import login

def private():
    s=''
    letters='qwertyuioplkjhgfdsazxcvbnm'
    letters+=letters.upper()
    letters+='234567890'
    letters+="!@#$%^&*?/'"
    for i in range(8):
        s+=random.choice(letters)
    return 'AB '+s

passcode,correct = 0,private()
_pass=False

def main(quiz_no=1,passpercent=65):
    global passcode,correct
    passcode=correct
    file='quiz '+str(quiz_no)+'.txt'
    quiz(file,passpercent)

def quiz(file,passpercent):
    global _pass
    if passcode!=correct:
        print("Fake")
        time.sleep(2.5)
        os._exit(1)
        return
    marks=0
    ob=open(file,'r')
    ans=eval(ob.readline())
    total_ques=len(ans.keys())
    q=ob.readlines()
    done=[]
    no=0
    max_no=int(2*(total_ques/3))
    while True:
        i=random.randint(1,total_ques)
        k=0
        for a in done:
            if i==a:
                k=1
        if k==1:
            continue
        no+=1
        if no>max_no:
            break
        if no<=max_no:
            line=(i-1)*5
            print('\n',no,'.',q[line][2:],end='',sep='')
            for a in range(line+1,line+5):
                print(q[a],end='')
            user_ans=input("Enter your answer -<a/b/c/d>- -> ")
            if user_ans.isdigit():
                q=int(user_ans)
                if q==1:
                    user_ans='a'
                elif q==2:
                    user_ans='b'
                elif q==3:
                    user_ans=='c'
                elif q==4:
                    user_ans=='d'
            if user_ans.lower()==str(ans[i]):
                print('Correct')
                marks+=1
                print("Marks :",marks)
            else:
                print('Wrong')
                print("Marks :",marks)
            done+=[i,]
    print("\nTotal marks obtained are : ",marks,"/",max_no)
    if marks >=((passpercent/100)*max_no):
        _pass = True
    ob.close()
if __name__ == '__main__':
    if login.admin():
        main()
