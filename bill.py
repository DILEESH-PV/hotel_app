import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
mycursor=mydb.cursor()
total=0
item=[]
while(True):
    print("\n please select an option")
    print("1 Tea-------10rs")
    print("2 Coffee ---15rs")
    print("3 Buger ----40rs")
    print("4 Sandwich -60rs")
    print("5 Alpham ---170rs")
    print("6 Generate Bill")
    print("7 view all transaction")
    print("8 day wise transaction summary")
    print("9 transaction summary for a period")
    print("10 Exit")
    ch=int(input("Enter the choice"))
    
    if(ch==1):
        print(" selected Add Tea option ")
        qty=int(input("Enter the quantity"))
        total+=10*qty
        item.append("Tea x "+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==2):
        print(" selected Add Coffee option")
        qty=int(input("enter the quantity"))
        total+=15*qty
        item.append("Coffee x "+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==3):
        print("selected Add Burger option")
        qty=int(input("enter the quantity"))
        total+=40*qty
        item.append("burger x "+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==4):
        print("selected Add Sandwich option")
        qty=int(input("enter the quantity"))
        total+=60*qty
        item.append("Sandwich x "+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
        
    elif(ch==5):
        print("selected Add Alpham option")
        qty=int(input("enter the quantity"))
        total+=170*qty
        item.append("Alpham x   "+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==6):
        print(" selected Generating bill option")
        name=input("Enter name")
        phn=input("Enter the phone number")
        print("========= BILL========")
        print("\n Name  : ",name)
        print("\n Mob   : ",phn)
        date=datetime.today().strftime('%Y-%m-%d')
        print("\n Date  : ",date)
        print("\n============================")
        print("\n Orderd items")
        for i in item:
            print(i)
        print("\nTotal amount = ",total)
        print("\n Thank you visit again\n\n")
        sql="INSERT INTO `bill`(`name`, `phno`, `amout`, `date`) VALUES (%s,%s,%s,now())"
        data=(name,phn,total)
        mycursor.execute(sql,data)
        mydb.commit()
        print("data inserted successfully on the database")
        total=0
        item=[]        
    elif(ch==7):
        date=input("Enter the date in 'yyyy-mm-dd' format")
        sql="SELECT * FROM `bill` WHERE `date`='"+date+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("\nselected view all recipe")
    elif(ch==10):
        break