# -*- coding: utf-8 -*-
"""assginment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LxNsgi-llACR-6tj2mrLg9dnhBkEfW8K
"""

#assignment on list,tuple,set,dictionary
list=[1,'pavan',2,'suresh']
print(list)
print(list[0])
list.append(100)
print(list)
list.insert(3,'kumar')
print(list)
list.remove('kumar')
print(list)

#Tuple
mytuple=(1,2,3)
print(mytuple)
print(type(mytuple))

#set
myset1={11,22,33,44,55}
print("the numbers are:",myset1)
myset1.add(66)
print(myset1)
myset2={55,66,77,88,99}
print(myset2)
myset3=myset1.union(myset2)
print(myset3)
myset4=myset1|myset2
print(myset4)

#dictionary
mydict={
    "pavan":'good boy',
    "suresh":'bad boy'
}
print(mydict)
mydict.update({"pavan":"bad boy","suresh":"good boy"})
print(mydict)
print(mydict["suresh"])

# 3 modes of read,write,append on file
# w for write in file
file= open("f.txt","w")
file.write("heyy hii!")
# r for read the file
file = open("f.txt",'r')
print(file.read())
# a for append(update data)
file = open("f.txt",'a')
file.write("heyy there!")
file = open("f.txt",'r')
print(file.read())
file.close()

#calculator
print("select a method to perform:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
method = input()
if method =='1':
  num1=int(input("enter your first number:"))
  num2=int(input("enter your second number:"))
  result=num1+num2
  print("the sum of two numbers is:",result)
elif method=='2':
  num1=int(input("enter your first number:"))
  num2=int(input("enter your second number:"))
  result=num1-num2
  print("the sub of two numbers is:",result)
elif method == '3':
  num1=int(input("enter your first number:"))
  num2=int(input("enter your second number:"))
  result=num1*num2
  print(result)
  print("the mul of two numbers is:",result)
elif method =='4':
  num1=int(input("enter your first number:"))
  num2=int(input("enter your second number:"))
  result=num1/num2
  print("the div of two numbers is:",result)
else:
  print("please choose any method")
file=open("calculator.txt","w")
file.write(str(result))
file.close()