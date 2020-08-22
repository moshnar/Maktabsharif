#Initials the list of number
for num in range(10,99):
        rem = sum = 0


        n = num
#Calculate the sum of digits
        while(num > 0):
            rem = num%10
            sum = sum + rem
            num = num//10
#check the number is Harshad number
        if(n%sum == 0):
            print(n)