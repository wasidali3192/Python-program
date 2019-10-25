


num = int(input("How many terms? "))

# first two terms we have to declare

n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid

if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(n1)
else:
   print("Fibonacci sequence upto",num,":")
   while count < num:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
