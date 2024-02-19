def decimalToBinary(self, num):
    # ToDo: Write Your Code Here.
    result = list()

    # This call happens log(n) times, where n is the size of the num in binary
    while num > 0:
        remainder = num % 2
        result.append(remainder)
        num = num // 2

    # this call happens 1 times for every digit in result which is log(n) digits
    
    # therfore the runtime of this function is log n
    return ''.join(str(i) for i in result)
