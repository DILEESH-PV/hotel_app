import mysql.connector
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
    print("7 Exit")
    ch=int(input("Enter the choice"))
    
    if(ch==1):
        print(" Added Tea ")
        qty=int(input("Enter the quantity"))
        total+=10*qty
        item.append("Tea x"+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==2):
        print("Added Coffee")
        qty=int(input("enter the quantity"))
        total+=15*qty
        item.append("Coffee x"+str(qty))
        #print("quantity= ",qty)
        #print("total=",total)
    elif(ch==3):
        print("Added Burger")
        qty=int(input("enter the quantity"))
        total+=40*qty
        item.append("Coffee x"+str(qty))
        print("quantity= ",qty)
        print("total=",total)
    elif(ch==4):
        print("Added Sandwich")
    elif(ch==5):
        print("Added Alpham")
    elif(ch==6):
        print("Generating bill")
    elif(ch==7):
        break