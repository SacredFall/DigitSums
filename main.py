def DigitSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

numbers = []
x = int(input('What is your lower bound?'))
y = int(input('What is your higher bound?'))
digitsum = int(input('What digit sum should your numbers sum to?'))
for i in range(x,y):
    a = DigitSum(i)
    if(a == digitsum):
        #print(i)
        numbers.append(int(i))


print(f'You have {len(numbers)} digit(s) with a digit sum of {digitsum}')
print(f'Here is your list: {numbers}')





