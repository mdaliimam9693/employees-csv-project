import csv
students_menu=('''
1.Add
2.Show
3.Search
4.Delete
5.Filter                              
''')
print(students_menu,end='')

choice=int(input("enter your choice :"))

if choice == 1:
    ## add student
    id_stu=input("enter student id :")
    name=input("enter student name :").title()
    age=input("enter student age  :")
    course=input("enter student course :").upper()
    marks=input("enter student marks :")

    with open("students.csv","r") as f:
        read=csv.reader(f)
        next(read)
        found=False
        for row in read:
            if row[0]==id_stu:
                found=True
                print("duplicate i'd not allow")
        if not found:        
            with open("students.csv","a",newline='') as f:
                write=csv.writer(f)
                write.writerow([id_stu,name,age,course,marks])
                print("add sucessfuly")   

elif choice == 2 :
    ## show student data
    with open("students.csv","r") as f:
        read=csv.reader(f)
        next(read)
        for row in read:
            print(f"id : {row[0]},name : {row[1]},age : {row[2]},course : {row[3]},marks : {row[4]}")

elif choice == 3 :
    ## searching student by student id 
    search=input("enter student id :")
    with open("students.csv","r")  as f:
        read=csv.reader(f)
        next(read)
        found=False
        for row in read:
            if row[0]==search:
                found = True
                print("found")
                print(f"id : {row[0]},name : {row[1]},age : {row[2]},course : {row[3]},marks : {row[4]}")
    if not found:
        print("sorry , not found")

elif choice == 4 :
    rows=[]
    search=input("enter student id :")
    with open("students.csv","r")  as f:
        read=csv.reader(f)
        header=next(read)
        found=False
        for row in read:
            if row[0]==search:
                found = True
            else:    
                rows.append(row)    
                
    if not found:
        print("sorry , not found")
    else :
        with open("students.csv","w",newline='') as f:
            write=csv.writer(f)
            write.writerow(header)
            write.writerows(rows)
            print("delete successfully")  
elif choice ==5:
    with open("students.csv","r")  as f:
        read=csv.reader(f)
        next(read)
        found = True
        for row in read:
            if row[4] > '90':
                found=True
                print(f"id : {row[0]},name : {row[1]},age : {row[2]},course : {row[3]},marks : {row[4]}")                           
    if not found :
        print("no one else")                               
else :
    print("invalid choice")        
