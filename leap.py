n=int(input("enter the year"))

if n%4==0:
   if n%100==0:
     if n%400==0:
       print("the year "+str(n)+" is leap year")
     else:
       print("the year "+str(n)+" is not leap year")
   else:
     print("the year "+str(n)+" is leap year")
else:
  print("the year "+str(n)+" is not leap year")    
