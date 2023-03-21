
queue = []

while True:
   print("Initial queue")
   print(queue)
   s=int(input('To enter element into queue press 1 and to delete element from queue press 2 and press 3 to quit'))
   if s==1:
      p=input('enter the element to be inserted into queue')
      queue.append(p)
   elif s==2:
      print("\nElements dequeued from queue")
      print(queue.pop(0))
      print("\nQueue after removing elements")
      print(queue)
   elif s==3:
      break
print('bye')



