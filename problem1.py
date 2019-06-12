import datetime
name=input("Enter Your Name :")
age=int(input("Enter your age :"))
now = datetime.datetime.now()
print(name," when you will be 95 the year will be ",(95-age)+now.year)
