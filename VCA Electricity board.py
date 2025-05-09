import mysql.connector as sql , random , datetime as dt
conn=sql.connect(host='localhost',user='root',passwd='',database='electricity_supply_board')
if conn.is_connected():
    print("successfully connected")
c1=conn.cursor()
def connect():
    conn=sql.connect(host='localhost',user='root',passwd='',database='electricity_supply_board')
def new_cust():
    a=1
    while a==1:
        username=getusername()
        password=input("Enter your password:")
        confirmpasswd=input("Confirm your password:")
        if password==confirmpasswd:
            insertinuser(username,password)
        else:
            print('your confirm password is incorrect')
            print('Try again')
            continue
        boxid=getboxid()
        print("Your boxid is", boxid)
        name=input('Enter your Name  :')
        address=input('Enter your Address  :')
        phoneno=int(input('Enter your PHONE NUMBER  :'))
        email=input('Enter your email  :')
        bankname=input('Enter your BANK NAME  :')
        card_no=int(input('Enter your CARD NUMBER  :'))
        insertincust(username,boxid,name,address,phoneno,email)
        insertintran(boxid,bankname,card_no,0,0,0,0,0,None)
        break
def getboxid():
    same="y"
    while same=="y":
        u=random.randrange(1000000,9999999)
        c1.execute("select * from cust_detail") 
        alldata=c1.fetchall()
        for i in alldata:
            if u==i[0][0]:
                continue
        same="n"
    return u
def getusername():
    same="y"
    while same=="y":
        u=input("Enter your username :")
        c1.execute("select * from user")
        alldata=c1.fetchall()
        for i in alldata:
            if u==alldata[0][0]:
                print("This username is taken.")
                break
        else:
            same="n"
    return u
def updateacc():
    print("What do you want to update")
    print('1.Password')
    print('2.Contact Details')
    print('3.Bank Details')
    choice3=int(input("Enter your choice"))
    if choice3==1:
        username=input("Enter your username :")
        password=input("Enter your new password:")
        updateinuser(password,username)
    if choice3==2:
        boxid=int(input("enter your boxid"))
        name=input('Enter your name  :')
        address=input('Enter your address  :')
        phoneno=int(input('Enter your PHONE NUMBER  :'))
        email=input('Enter your email  :')
        updateincust(name,address,phoneno,email,boxid)
    if choice3==3:
        boxid=int(input("enter your boxid"))
        bankname=input('Enter your BANK NAME  :')
        card_no=int(input('Enter your CARD NUMBER  :'))
        updateintran(bankname,card_no,boxid)
    conn.commit()
    connect()
def updateincust(a1,a2,a3,a4,bid):
    upcomm="update cust_detail set name=%s,address=%s,phoneno=%s,email=%s where boxid=%s"
    r=(a1,a2,a3,a4,bid)
    c1.execute(upcomm,r)
def updateintran(a1,a2,bid):
    upcomm="update billing set bankname=%s,card_no=%s where boxid=%s"
    r=(a1,a2,bid)
    c1.execute(upcomm,r)
def updateintran2(a1,a2,a3,a4,a5,a6,bid):
    upcomm="update billing set unit=%s,amount=%s,GST=%s,totalamount=%s,amountdue=%s,duedate=%s where boxid=%s"
    r=(a1,a2,a3,a4,a5,a6,bid)
    c1.execute(upcomm,r)
def updateinuser(a1,uname):
    upcomm="update user set password=%s where username=%s"
    r=(a1,uname)
    c1.execute(upcomm,r)
def insertintran(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    r=(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    incomm="insert into billing values(%s, %s, %s, %s, %s, %s, %s,%s,%s)"
    c1.execute(incomm,r)
    conn.commit()
    connect()
def insertincust(a1,a2,a3,a4,a5,a6):
    r=(a1,a2,a3,a4,a5,a6)
    incomm="insert into cust_detail values(%s, %s, %s, %s, %s, %s)"
    c1.execute(incomm,r)
    conn.commit()
    connect()
def insertinuser(a1,a2):
    r=(a1,a2)
    incomm="insert into user values(%s, %s)"
    c1.execute(incomm,r)
    conn.commit()
    connect()
def faq():
    print("1.What are the requirements to become an DESC consumer?")
    print("2.General Safety Measures")
    print("3.How to increase the sanctioned load?")
    print("4.I have a billing complaint. What should I do?")
    print("5.What is the procedure of Billing?")
    print("6.How to transfer name of service conncetion?")
    print("7.What should I do to change my tariff?")
    print("8.How do I get a temprory connection?")
    print("9.How do I calculate my power comsumption?")
    print("10.I have not received this month's bill. What should I do now?")
    print("11.Ask something else")
    ans="yes"
    while ans=="yes":
        choicee=int(input("Please Enter your choice-"))
        if choicee==1:
            print("1.Apply in A-1 form at the section office for domestic/commercial")
            print("2.For industrial at Sub-division/division along with no objectioncertificate required")
            print("3.After load survey, you will be given quotation for payment of charges which includes")
            print("service connection charges , Service Line Charges,Security deposit etc.")
        elif choicee==2:
            print("1.Consumer should install safety equipments like Earth leakage / overload & short circuit")
            print("protection ( circuit breakers / switches )near point of supply.")
            print("2.Healthy earthing should be installed at your premises.")
            print("3.ISI marked cables and equipments of proper capacity should be used for installation")
            print("and wiring should be done through only licensedElectrical Contractors.")
            print("4.Always use proper capacity fuse wire in main switches.")
        elif choicee==3:
            print("For increasing the sanctioned load the domestic, commercial and industrial (LT) consumers")
            print("should apply to the concerned Sectional and Sub-divisional in charge.")
            print("The HT consumers should apply to the Superintending Engineer.")
            print("After confirming the feasibility, the load is sanctioned and the quotation is")
            print("issued which includes additional Service Line Charges, Security deposit.")
        elif choicee==4:
            print("Not to worry! Just do either of the followings:Reach us by calling our 24 X 7 toll free no.")
            print("19122 anytime,Send an e-mail to helpdesk.electricity@vca.com orVisit your nearest Customer Care Centre")
        elif choicee==5:
            print("After installation the billing section is supplied with data containing")
            print("Meter details, initial meter reading . As per the predetermined cyclic")
            print("order the first bill is issued. The bills are issued monthly, bimonthly and quarterly")
            print("for Domestic, non-domestic, industrial, Agricultural consumers.")
            print("The payment of bills is to be made as per the last due date shown on the bill.")
        elif choicee==6:
            print("The Name transfer application along with document supporting the change of")
            print("ownership, no objection/consent letters if any and fresh application with applicable")
            print("fee may submitted to concerned Assistant Engineer/Operation & Maintenance of TANGEDCO.")
            print("However, name transfer will not be effected to services under disconnection.")
            print("Application forms are available in the website.")
        elif choicee==7:
            print("You may contact your area's Assistant Engineer/Operation & Maintenance and give a")
            print("requisition letter explaining the purpose of tariff change along withdocumentary proof.")
        elif choicee==8:
            print("temporary supply can be extended on application to concerned Assistant")
            print("Executive Engineer/Operation & Maintenance by intending consumer with")
            print("required charges and on the receipt of deposit.")
        elif choicee==9:
            print("You can use an energy calculator (called as bill budgeter) on many websites.")
            print("You can enter your average daily usage of the listed appliances and the calculator")
            print("will give you the monthly consumption in units.")
        elif choicee==10:
            print("Bills are prepared and dispatched each month on a specific date.")
            print("However, in case of non-receipt of your bill, you can :Call us on our 24 X 7")
            print("toll free number 19122  anytime. Or Send an e-mail helpdesk.electricity@vca.com")
        elif choicee==11:
            print("Feel free to place a call to our 24 X 7 toll free call center at 19122")
            print("and get answered by our customer service representative. within 2 minutes.")
        else:
            print("Enter a valid choice")
        ans=input("Do you want to ask more questions(yes/no)?")
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + dt.timedelta(days=4)
    return (next_month - dt.timedelta(days=next_month.day))
def makebill():
    c1.execute("select * from billing")
    data=c1.fetchall()
    for i in data:
        amtdue=i[6]
        boxid=i[0]
        unit=random.randint(50,1000)
        amount=10*unit
        GST=(15/100)*amount
        totalamount=amount+GST+amtdue
        duedate=last_day_of_month(dt.date.today())
        updateintran2(unit,amount,GST,totalamount,amtdue,duedate,boxid)
c='YES'
cont="yes"
while c.upper()=='YES':
    print('************************WELCOME TO VCA ELECTRICITY BOARD************************')
    print(dt.datetime.now())
    print('1.NEW USER')
    print('2.EXISTING USER')
    print('3.Admin')
    print('4.EXIT')
    choice1=int(input('ENTER YOUR CHOICE:'))
    if choice1==1:
        new_cust()
        cont="yes"
    elif choice1==2:
        data=[]
        while data==[]:
            username=input('Enter your username:')
            info2="select password from user where username='{}'".format(username)
            c1.execute(info2)
            data=c1.fetchall()
            if data==[]:
                print("Please Enter Valid username")
        password=input('Enter your password:')
        if data[0][0]!=password:
            print('password is incorrect')
            c=input("do you want to try again?(yes or no)")
            continue
        cont="yes"
    elif choice1==3:
        data=[]
        while data==[]:
            username=input('Enter your username:')
            info2="select password from admin where username='{}'".format(username)
            c1.execute(info2)
            data=c1.fetchall()
            if data==[]:
                print("Please Enter Valid username")
        password=input('Enter your password:')
        if data[0][0]!=password:
            print('password is incorrect')
            c=input("do you want to try again?(yes or no)")
            continue
        cont="yes"
    elif choice1==4:
        c='no'
        continue
    else:
        print("INVALID CHOICE.Please try again")
        continue
    print('************************WELCOME TO VCA ELECTRICITY BOARD************************')
    while cont.upper()=='YES':
        if choice1==2 or choice1==1:
            print("1.ACCOUNT SETTINGS")
            print("2.TRANSACTION")
            print("3.VIEW CUSTOMER DETAILS")
            print("4.Frequently Asked Questions")
            print('5.EXIT')
            choice2=int(input('ENTER YOUR CHOICE'))
            if choice2==1:
                print('1.Update Account')
                print('2.Delete Account')
                choice12=int(input('ENTER YOUR CHOICE:'))
                if choice12==1:
                    updateacc()
                    cont=input("do you want to continue?(yes or no)")
                elif choice12==2:
                    boxid=input("ENTER YOUR BOXID:")
                    info10=c1.execute("select * from billing where boxid="+str(boxid))
                    data3=c1.fetchall()
                    amtdue=data3[0][7]
                    totalamount=data3[0][6]
                    if amtdue>0 or totalamount>0:
                        print("Please clear all the dues first")
                        continue
                    info8=c1.execute("select username from cust_detail where boxid='{}'".format(boxid))
                    user=c1.fetchall()
                    info6=c1.execute("delete from billing where boxid='{}'".format(boxid))
                    info7=c1.execute("delete from cust_detail where boxid='{}'".format(boxid))
                    info8=c1.execute("delete from user where username='{}'".format(user[0][0]))
                    c1.execute(info6)
                    c1.execute(info7)
                    c1.execute(info8)
                    conn.commit()
                    print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY DELETED")
                    c="no"
                    cont="no"
                    break
            elif choice2==2:
                boxid=int(input('Enter your boxid :'))
                info10="select * from billing where boxid="+str(boxid)
                info11="select * from cust_detail where boxid="+str(boxid)
                c1.execute(info10)
                data3=c1.fetchall()
                c1.execute(info11)
                data4=c1.fetchall()
                amtdue=data3[0][6]
                if amtdue==0:
                    print('you have already paid the bill')
                else:
                    print("Mr/Mrs",data4[0][2])
                    print("Address-",data4[0][3])
                    print("Your Meter Device ID is",boxid)
                    print('Dear customer, you have used ',data3[0][3],'units of electricity.')
                    print('One unit currently is of 10 ruppees')
                    toda=dt.date.today()                    
                    deadline=data3[0][8]
                    totalamount=data3[0][6]
                    amtdue=data3[0][7]
                    print("Your previous Month due=",amtdue)
                    if deadline<toda:
                        delta=toda-deadline
                        fine=(delta.days)*5
                        totalamount+=fine
                        print('You have dealyed for ',toda-deadline,'days.The fine per day is 5 rupees.')
                        print('Your Total due including fine is',totalamount)
                    else:
                        print('Your Total due including GST is',totalamount)
                    p=input("Please Enter YES to transact")
                    if p.upper()=="YES":
                        print("Transaction successful")
                        print("You have paid the bill")
                        updateintran2(0,0,0,0,0,None,boxid)
                    else:
                        print('please pay the bill sooner')
                cont=input("do you want to continue?(yes or no)")
            elif choice2==3:
                boxid=int(input('Enter your boxid :'))
                info4="select * from cust_detail where boxid=" + str(boxid)
                c1.execute(info4)
                data1=c1.fetchall()
                for row in data1:
                    print("username: ", row[0])
                    print("Your meter device ID:",row[1])
                    print("Person name:",row[2])
                    print("Residential address:",row[3])
                    print("phone number:",row[4])
                    print("email:",row[5])
                info5="select * from billing where boxid=" + str(boxid)
                c1.execute(info5)
                data2=c1.fetchall()
                for row in data2:
                    print("Bank Name : ",row[1])
                    print("Card number:",row[2])
                    print("Unit:",row[3])
                    print("Due Amount:",row[6])
                cont=input("do you want to continue?(yes or no)")
            elif choice2==4:
                faq()
                cont=input("do you want to continue?(yes or no)")
            elif choice2==5:
                c='no'
                cont="no"
            else:
                print("INVALID CHOICE.Please try again")
        elif choice1==3:
            print("1.Display Customer Detail")
            print("2.BIllING")
            print("3.Company Transaction")
            choice3=int(input('ENTER YOUR CHOICE'))
            if choice3==1:
                c1.execute("select * from cust_detail")
                data=c1.fetchall()
                for i in data:
                    print(i)
                cont=input("do you want to continue?(yes or no)")
            elif choice3==2:
                makebill()
                cont=input("do you want to continue?(yes or no)")
            elif choice3==3:
                c1.execute("select * from billing")
                data=c1.fetchall()
                for i in data:
                    print(i)
                cont=input("do you want to continue?(yes or no)")
            else:
                print("Invalid Choice, please try again")
else:
    print("THANK  YOU!!!!  VISIT AGAIN!!!!")
conn.commit()
