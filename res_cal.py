
print("*************Result Marks Calculator*************\n")
print("\nEnter the Subjuect Marks: \n")

eng=int(input("English \n"))
math=int(input("Math \n"))
phy=int(input("Physics \n"))

persent= ((eng+math+phy)/300)*100
print("---------------------------")
print ("The Persentage is :",persent,"%")
print("---------------------------")

print('And The Grade is :')
if persent >=80:
	print("A+")
elif persent >=70:
	print("A")
elif persent >=60:
	print("B")
elif persent >=50:
	print("C")
else:
	print("F")


print ('---------------------By MUQEET------------------------')