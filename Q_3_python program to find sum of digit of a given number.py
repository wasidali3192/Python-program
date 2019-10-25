#Name = Mohd_Shakir
#Roll_No = 08
#Enrollment_No = A180478



num = int(input("Enter a number: "))
# initializing sum to zero
sum = 0

# going through every digit using every for loop
while num > 0:
    d = num%10
    num = num//10
    sum +=d

print("The sum of digits of number is",sum)
