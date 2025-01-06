# class college:
#     def __init__(self,name,course):
#         self.n=name
#         self.c=course
#     def print(self):
#         print(self.n,self.c)
# c=college("mec",2026)
# c.print()

# class a:
#     def __init__(self,age,place):
#         self.a=age 
#         self.p=place
#     def display(self):
#         print("name and place:",self.a,self.p)
# s=a(19,"rasipuram")
# s.display()

#single inheritance
# class Account:
#     accountNo=0
#     accountBal=0.0
#     accountHolder=""
#     def __str__(self):
#         return str(self.accountNo)+" "+self.accountHolder+" "+str(self.accountBal)+"\n"
# #single
# class Card(Account):
#     cardNumber=0
#     def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
#         self.cardNumber=cn
#         self.transactions=[]
#         self.accountNo=anum
#         self.accountHolder=ahold
#         self.accountBal=abal
#     def __add__(self,amt):
#         self.accountBal+=amt
#         print(amt,"deposited to",self.accountHolder)
#         self.transactions.append('Credit')
#     def __sub__(self, draw):
#         if self.accountBal>=draw:
#             self.accountBal-=draw
#             print(draw,"has been withdrawn from ",self.accountHolder)
#             self.transactions.append('Debit')
#         else:print("Insufficient account balance")
#     def countTrans(self):
#         creCount=self.transactions.count('Credit')
#         debCount = self.transactions.count('Debit')
#         charges=0
#         if creCount>=5:
#             charges+=(creCount-5)*10
#         if debCount>=3:
#             charges+=(debCount-3)*20
#         print("Total charges on transaction count is",charges)
#         self.accountBal-=charges
#         print("Charges debited in your account")
#     def __str__(self):
#         return str(super(Card, self).__str__())+"\n"+str(self.cardNumber)+" "+str(self.accountBal)+"\n"
# a1=Account()
# a1.accountNo=1456;a1.accountHolder="Nandha";a1.accountBal=15000.0
# print(a1)

# c1=Card(789456123,9876787,"Annamalai",777.9)
# c1+4000
# print(c1)
# c1-1800
# print(c1)
# c1-200
# c1+1000
# c1-100
# c1-500
# c1+10000    
# c1-100
# c1+4000
# print(c1)
# c1.countTrans()

# multilevel Inheritance
# class college:
#     def getstudentinfo(self):
#         self.__rollno=input("enter roll number:")
#         self.__name=input("enter name:")

#     def printstudentinfo(self):
#         print("roll number:",self.__rollno,"name:",self.__name)

# class BE(college):
#     def getBE(self):
#       self.getstudentinfo()
#       self.__p=int(input("enter physics marks:"))
#       self.__c=int(input("enter chemistry marks:"))
#       self.__m=int(input("enter maths marks:"))
    
#     def printBE(self):
#         self.printstudentinfo()
#         print("marks in different sub:",self.__p,self.__c,self.__m)

#     def calctotalmarks(self):
#         return(self.__p+self.__c+self.__m)
    
# class result(BE):
#     def getresult(self):
#         self.getBE()
#         self.__total=self.calctotalmarks()
#     def putresult(self):
#         self.printBE()
#         print("total marks oot of 300:",self.__total)

# college=result()
# college.getresult()
# college.putresult()

#encapsulation
# class mobile:
#     __model=""
#     __price=0.0
#     __ram=0
#     __internal=0
#     def setmodel(self,mod=""):
#         self.__model=mod
#     def getmodel(self):
#         return self.__model
#     def setprice(self,pri=""):
#         self.__price=pri
#     def getprice(self):
#         return self.__price
#     def setram(self,ra=""):
#         self.__ram=ra
#     def getram(self):
#         return self.__ram
#     def setinternal(self,internal=""):
#         self.__internal=internal
#     def getinternal(self):
#         return self.__internal

# mob1=mobile()
# mob1.setmodel("iq3")
# mob1.setprice(80000)
# mob1.setram(128)
# mob1.setinternal(128)
# print(mob1.getmodel(),mob1.getprice(),mob1.getram(),mob1.getinternal())

# mob2=mobile()
# mob2.setmodel("iq4")
# mob2.setprice(85000)
# mob2.setram(256)
# mob2.setinternal(256)
# print(mob2.getmodel(),mob2.getprice(),mob2.getram(),mob2.getinternal())

#  Hierarchy inheritance:

# from array import *

# class Stocks:
#     products=array('i')
#     def show(self):print("Products are: ",self.products)

# class Jaysurya(Stocks):
#     def __init__(self,hey):
#         self.products=array('i')
#         self.products.extend(hey)
#     def search(self):
#         budget=int(input("Enter the price  search:"))
#         for x in self.products:
#             if x<=budget:print(x)
# class Reliance(Stocks):
#     def __init__(self,hai):
#         self.products = array('i')
#         self.products.extend(hai)
#     def getByPosition(self,start,stop):
#         print(self.products[start:stop])

# j=Jaysurya([5000,300,800,780,150])
# r=Reliance([100,200,300,400,500,600,800,1000])

# j.search()

# r.getByPosition(0,5)
# r.show()
# j.show()


# from abc import *

# class Falcon(ABC):
#     def __init__(self):
#         self.mine={78,33,10,40,923,42,56,5,75,477,3,56}
#     #abstract function        
#     def heyThere(self):
#         pass
    

# class Winter(Falcon):
#     def heyThere(self):
#         print(self.mine)


# win=Winter()
# win.heyThere()

#POLYMORPHISM
# class Bird: 
#     def sound(self):
#         print("CUCKKOO")

#     def fly(self):
#         print("its can be flying the birds")
# class Bird1(Bird):
#     def cockatail(self):
#         print("cuteiee")
# class Bird2(Bird):
#     def Lovebirds(self):
#         print("couple of love")
# obj1=Bird()
# obj2=Bird1()
# obj3=Bird2()
# obj1.sound()
# obj1.fly()
# obj1.sound()
# obj2.cockatail()
# obj1.sound()
# obj3.Lovebirds()
# obj1.fly()  

#multiple 

# class travels:
#     def name(self):
#         print("YBM TRAVELS")
# class travels1:
#     def name1(self):
#         print("KPN TRAVELS")
# class main(travels,travels1):
#     def luxury(self):
#         print("enjoy the journey of happiness")

# m=main()
# m.name()
# m.name1()
# m.luxury()

# overloading
# class sam:
#     def aa(self,a):
#         print(a)
#     def aa(self,a,b):
#         print(a+b)
#     def aa(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.aa(10)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# o=over()

# print("Sum",o.load(10))
# print("sum1",o.load(10,20)) 
# print("sum",o.load(10,20,30))


#multiple args passing 
# class multiple:
#     def add(self,*args):
#         sum=40
#         for i in args:
#             sum+=i
            
#         print("add values:",sum)
            
# m=multiple()
# #m.add(20)
# m.add(40,50)
# m.add(40,50,100)
# m.add(40,50,100,200)
# m.add(10,20,60,100,150)
# m.add(10,20,30,40,50,60,70)

#OVERRIDING
# class sam:
#     def name(self):
#         print("sampk")
# class raja(sam):
#     def name(self):
#         super().name()
#         print("raja")
# class arun(raja):
#     def name(self):
#         super().name()
#         print("ARUN")
# # s=arun()
# # s.name()
# # s1=raja()
# # s1.name()
# s=arun()
# s.name()





