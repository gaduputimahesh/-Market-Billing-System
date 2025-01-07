from datetime import datetime
print("----------------Welcome---------------------------------------")
name=input("Enter  your name:")
#lists of items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Panner  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
colgate Rs 85/each  
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=[]
gst=[]


#rates of item
items={'rice':20,'sugar':30,'salt':15,'oil':80,'panner':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of item press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
     inp1=int(input("if you want to buy press 1 or 2 for exit:"))
     if inp1==2:
         break
     if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not avaliable")
     else:
         print("you entered wrong number")
inp=input("can i bill the items yes or no")
if inp=='yes':
 pass
 if finalamount!=0:
    print(25*"=","Mahesh supermarket",25*"=")
    print(28*" ","uravakonda")
    print("Name:",name,30*" ","Date:",datetime.now())
    print(75*"-")
    print("sno",8*" ","items",8*" ",'Quantity',5*" ",'price')
    for i in range(len(pricelist)):
        print(i,9*' ',ilist[i],9*' ',qlist[i],11*' ',plist[i])
    print(75*"-")
    print(40*" ",'TotalAmount:','Rs',totalprice)
    print(40*" ",'gst amount:','Rs',gst)
    print(75*"-")
    print(40*" ", 'finalAmount:', 'Rs',finalamount)
    print(75*"-")
    print(20*" ","Thanks for visiting")
    print("-------------------------------------*--------------------------------------------")














