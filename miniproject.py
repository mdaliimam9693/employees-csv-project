import pandas as pd
import csv

dt=pd.read_csv("students.csv")
print("Students Dashboard")
print('-'* 30)

# total student
tol_stu=len(dt)
print("total students :",tol_stu)

# average marks
avg_marks=dt['marks'].mean()
print("average marks :",avg_marks)

# topper 
topper=dt.loc[dt['marks'].idxmax()]
print(f"Topper name :{topper['name']}")

#last
last=dt.loc[dt['marks'].idxmin()]
print(f"students name :{last['name']}")

# pass / fail
pass_stu=len(dt[dt['marks']>=40])
fail_stu=len(dt[dt['marks']<40])
print("number of pass :",pass_stu)
print("number of fail :",fail_stu)
