n= int(input("enter the number"))
s=n
rev=0
while n!=0 :
   rev=int(rev*10+n%10)
   n=int(n/10)
   print(n)
   
print("rev of the number "+str(s)+" is "+str(rev))

