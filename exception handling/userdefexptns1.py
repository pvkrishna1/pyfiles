import random
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
number=random.randint(1,10)
while True:
    try:
        i_num=int(input("enter a number: "))
        if i_num<number:
            raise ValueTooSmallError
        if i_num>number:
            raise ValueTooLargeError
        break
except(ValueTooSmallError):
    print("this value is too small try again")
except(ValueTooLargeError):
    print("this value is too large try again")
print("congratulations..! you guessed it correctly")
