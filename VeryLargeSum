'''
write a function to calculate the sum of two very large numbers that are represented as strings
num1 = '99999999999999999999999999999999999999999999999999.......9'
num2 = '99999999999999999999999999999999999999999999999999............9'

'''


def v_largesum(num1, num2):
    
    num3 = ''     #string to hold the sum of two numbers

    if len(num1) == len(num2):  # if length of both strings(numbers) are same
       
        carry = 0   # variable to hold the carry value after adding two digits
        
        for x in range(len(num1) - 1, -1, -1):  # loop from last index to first of both strings
        
            num_one = int(num1[x])              # get the value at index i and convert it to integer
            num_two = int(num2[x])              # get the value at index i and convert it to integer
            sum = num_one + num_two + carry     # add the two digits and previous carry if any
            carry = sum/10                      # carry generated after adding the two values 
            rem = sum % 10                      # sum value excluding the carry
            num3 = str(rem) + num3              # add the rem value to new string in the front of the string  which will hold the sum

    else:                       # if the two strings(numbers) have different length
        n1 = len(num1)          #length of first string
        n2 = len(num2)          #length of second string


    #Finding the length of string
    #smalln: length of shorter string
    #highn : length of longer string
    #larset: longer string
    #shift:  the difference in length of two strings

    
        if n1<n2:
            smalln = n1
            highn = n2
            larset = num2
            shift = n2-n1
        else:
            smalln = n2
            highn = n1
            larset = num1
            shift = n1-n2

        carry = 0
        
    #looping from last index to part where both string have same length
        
        for x in range(highn-1, shift-1, -1):
            num_one = int(larset[x])
            num_two = int(num2[x-shift])
            sum = num_one + num_two + carry
            carry = sum/10
            rem = sum % 10
            num3 = str(rem) + num3
            
    #looping in the remaining of the larger string
        
        for x in range(shift-1 ,-1, -1):
            num_two = int(larset[x])
            sum = num_two + carry   #only carry required and the values in index of larger string 
            carry = sum/10
            rem = sum % 10
            num3 = str(rem) + num3
        
    #num3: contains sum
    # appending the last carry
    
    return str(carry) + num3


num1 = '9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
num2 = '9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'

print v_largesum(num1,num2)
    

