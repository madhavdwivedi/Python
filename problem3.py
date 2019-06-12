#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

a1=[]
a2=[]

print("Numbers > 5:")
for i in adhoc :
	if i > 5 :
		print(i)
		a1.append(i)


print("Numbers <= 2:")
for i in adhoc :
	if i <= 2 :
		print(i)
		a2.append(i)


print("Numbers greater than 5 ,a1 =",a1)
print("Numbers less than or equals to 2 ,a2=",a2)


