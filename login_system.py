import csv
from datetime import datetime
now=datetime.now()
date=now.strftime("%Y-%m-%d")
time=now.strftime("%H-%M-%S")
import getpass
import hashlib
status=''
login_sys_menu=('''1. SignUp
2. Login
3. Change Password
4. Forgot password
5. login history
6. show success login history
7. show fail login history
8. count total login history
 ''')
print(login_sys_menu,end='')
choice=int(input("enter choice :"))
if choice == 1:  #signUp
        user=input("enter your username :")
        with open("users.csv","r") as f:
            read_file=csv.reader(f)
            header1=next(read_file)
            found=False
            for row1 in read_file:
                if row1[0]==user:
                    found=True
                    print("already exit")
                    break
        if not found :            
            with open("users.csv","a",newline='') as f:
                write=csv.writer(f)
                password=getpass.getpass("enter your password :")
                hash_input= hashlib.sha256(password.encode()).hexdigest()
                write.writerow([user,hash_input])
                print("account has been created")    
    
elif choice == 2:   #login
    attempt=0
    while attempt < 3:
        user=input("enter your username :")
        password=getpass.getpass("enter your password :")
        hash_input=hashlib.sha256(password.encode()).hexdigest()
        found=False
        with open("users.csv","r") as f:
            read_user=csv.reader(f)
            header=next(read_user)
            for row in read_user:
                if row[0]== user and row[1] == hash_input:
                    found=True
                    print("login successfully")
                    break
        if found:
            break 
        else:
            attempt+=1
            print("wrong password")
            print("attempt left :",3-attempt)       
    if attempt==3:
        print("Account Lock")

elif choice == 3:   #change password
    rows=[]
    user=input("enter your username :")
    password=input("enter old password :")
    hash_input=hashlib.sha256(password.encode()).hexdigest()

    found=False
    with open("users.csv","r") as f:
        read_user=csv.reader(f)
        header=next(read_user)
        for row in read_user:
            if row [0] == user and row[1] == password:
                found=True
                new_pass=getpass.getpass("enter new password :")
                hash_new=hashlib.sha256(new_pass.encode()).hexdigest()
                confirm_pass=getpass.getpass("enter confirm password :")
                hash_confirm=hashlib.sha256(confirm_pass.encode()).hexdigest()
                if hash_new!=hash_confirm :
                    print("password mismatch")
                else :    
                    print("password match")
                    row[1]=hash_new
            rows.append(row)

    if not found:
        print("Wrong Password") 
    else:
        with open("users.csv","w",newline='') as f:
            write=csv.writer(f)
            write.writerow(header)
            write.writerows(rows)
            print("change password successfully")                   

elif choice==4 :  #forgot password
    rows2=[]
    user=input("enter your username :")
    found = False
    with open("users.csv","r") as f:
        read_user=csv.reader(f)
        header=next(read_user)
        for row in read_user:
            if row[0]==user:
                found = True
                new_password=getpass.getpass("enter new password :")
                con_password=getpass.getpass("enter confirm password :")
                if new_password!=con_password:
                    print("password not match")
                else :
                    hash_new_pass=hashlib.sha256(new_password.encode()).hexdigest()
                    row[1]=hash_new_pass
            rows2.append(row)
    if not found :
        print("user isn't exit")
    else:
        with open("users.csv","w",newline='') as f:
            write=csv.writer(f)
            write.writerow(header)
            write.writerows(rows2)
            print("password reset successful")

elif choice == 5 :  #login history

    # with open("login_history.csv","w",newline='') as f:
    #     write=csv.writer(f)
    #     write.writerow(["user","date","time","status"])      

    user=input("enter your username :")
    password=getpass.getpass("enter old password :")

    with open("users.csv","r") as f:
        read_user=csv.reader(f)
        header=next(read_user)
        found=False
        for row in read_user:
            if row[0]==user and row[1] == password:
                found=True
                print("login successfully")
                status='success'
                with open("login_history.csv","a",newline='') as f:
                    write=csv.writer(f)
                    write.writerow([user,date,time,status])    
    if not found:
        print("login falid")    
        status='fail'
        with open("login_history.csv","a",newline='') as f:
            write=csv.writer(f)
            write.writerow([user,date,time,status])

elif choice == 6:  #success login hsitoy
    with open("login_history.csv","r") as f:
           read_history=csv.reader(f)

           for row in read_history :
                if row[3]=='success':
                    print(f"user : {row[0]},date : {row[1]},time : {row[2]},satus : {row[3]}")   
                            
elif choice == 7:  # fail login history
    with open("login_history.csv","r") as f:
           read_history=csv.reader(f)

           for row in read_history :
                if row[3]=='fail':
                    print(f"user : {row[0]},date : {row[1]},time : {row[2]},satus : {row[3]}") 

elif choice == 8:   # total count history
    count=0
    with open("login_history.csv","r") as f:
           read_history=csv.reader(f)
           next(read_history)
           for row in read_history :
                count+=1 
    print("total number of login history:",count)                      
else :
    print("invalid choice")                      
