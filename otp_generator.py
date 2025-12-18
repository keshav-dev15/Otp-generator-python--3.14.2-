import random

def otp_generator(length=4): #you can change the length here according to your need
    if length <= 0: #checks the length if it is positive and greayer that 0
        return "OTP length must be greater than 0"

    otp = "".join(str(random.randint(0, 9)) for _ in range(length)) #generates opt using random module then itirates for the given length after that converted into string for usong (.join) function
        return otp

final = otp_generator()
print(final)