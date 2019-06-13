

import datetime



name=input("enter your name")
time=datetime.datetime.now().hour



print('present time is',time)

if(time >= 6 and time< 12):
	print("good morning", name)
elif(time >= 12 and time < 16 ):
	print("good after noon", name)
elif(time >= 16 and time <20):
	print("good evening", name)
elif(time>=20 and time <=24 or time >=0 and time <6):
	print("this is good night", name)

