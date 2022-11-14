import sys
import sqlite3
import random as r
class customer:
    bank_name='Welcome To SBI BANK'
    conn=None
    def __init__(self):
        self.conn=sqlite3.connect('customer.db')
        self.cursor=self.conn.cursor()
        self.cursor.execute("create table if not exists customer(accno int primary key,name varchar(20),balance int)")
    def getaccount(self):
        accno=r.randint(100001,999999)
        name=input("Enter Your Name")
        balance=int(input("Enter your balance"))
        self.cursor.execute("insert into customer values(?,?,?)",(accno,name,balance))
        self.conn.commit()
        print("Hello",name,"Your Account got Created")
        self.cursor.execute("select accno from customer where name='{}'".format(name))
        AccountNumber=self.cursor.fetchone()
        for i in AccountNumber:
          print("plz notedown your AccountNumber:",i)
        sys.exit()
    def deposit(self):
        acno=int(input("Enter your account number"))
        dpst=int(input("Enter your amount to deposit"))
        self.cursor.execute("update customer set balance=balance+{} where          accno={}".format(dpst,acno))
        self.conn.commit()
        self.cursor.execute("select balance from customer where accno={}".format(acno))
        bal=self.cursor.fetchone()
        for i in bal:
            print("Hi After deposit your balance Amount is:",i)
    def withdraw(self):
        acno=int(input("Enter your account number"))
        wdamt=int(input("Enter your amount to withdraw"))
        self.cursor.execute("select balance from customer where accno={}".format(acno))
        bal=self.cursor.fetchone()
        t=0
        for i in bal:
            t=int(i)
        if wdamt>t:
            print("Sorry..Insufficient Funds in Your Account")
            sys.exit
        else:
            self.cursor.execute("update customer set balance=balance-{} where accno={}".format(wdamt,acno))
            self.conn.commit()
        self.cursor.execute("select balance from customer where accno={}".format(acno))
        bal=self.cursor.fetchone()
        for i in bal:
           print("Hi After withdraw your balance Amount is:",i)
    def loaddata(self):
        #self.conn = sqlite3.connect("customer.db")
        acno=int(input("enter your account number"))
        query = "SELECT * FROM customer where accno={}".format(acno)
        self.cursor.execute(query)
        r=self.cursor.fetchone()
        print(r)
    def alldata(self):
        #self.conn = sqlite3.connect("customer.db")
        #acno=int(input("enter your account number"))
        query = "SELECT * FROM customer"
        self.cursor.execute(query)
        rows=self.cursor.fetchall()
        for i in rows:
         print(i)
        self.conn.close()
print("Welcome to Python",customer.bank_name)
c1=customer()
print("Are You Existing Customer or New Customer")
print("E-Existing\nN-New Customer")
option=input("choose your option")
if option=='N' or option=='n':
    c1.getaccount()
elif option=='E' or option=='e':
  while True:
    print("D-Deposit\nW-Withdraw\nS-Show\nA-all\nE-Exit")
    option=input("choose your option")
    if option=='D' or option=='d':
        c1.deposit()
    elif option=='W' or option=='w':
          c1.withdraw()
    elif option=='S' or option=='s':
          c1.loaddata()
    elif option=='A' or option=='a':
        c1.alldata()
    else:
        print("Invalid Option choose valid Option please")
    
