import csv
print("1. sign up\n2. login\n3. change password")
choice=int(input("enter number :"))
if choice == 1:
        user=input("enter your username :")
        with open("login.csv","r") as f:
            read_file=csv.reader(f)
            header1=next(read_file)
            found=False
            for row1 in read_file:
                if row1[0]==user:
                    found=True
                    print("already exit")
                    break
        if not found :            
            with open("login.csv","a",newline='') as f:
                write=csv.writer(f)
                password=input("enter password :")
                write.writerow([user,password])
                print("account has been created")    
    
if choice == 2:
    attempt=0
    while attempt < 3:
        user=input("enter your username :")
        password=input("enter password :")
        found=False
        with open("login.csv","r") as f:
            read_user=csv.reader(f)
            header=next(read_user)
            for row in read_user:
                if row[0]== user and row[1] == password:
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

if choice == 3:
    rows=[]
    user=input("enter your username :")
    password=input("enter old password :")
    found=False
    with open("login.csv","r") as f:
        read_user=csv.reader(f)
        header=next(read_user)
        for row in read_user:
            if row [0] == user and row[1] == password:
                found=True
                new_pass=input("enter new password :")
                row[1]=new_pass
            rows.append(row)
    if not found:
        print("Wrong Password") 
    else:
        with open("login.csv","w",newline='') as f:
            write=csv.writer(f)
            write.writerow(header)
            write.writerows(rows)
            print("change password successfully")                   