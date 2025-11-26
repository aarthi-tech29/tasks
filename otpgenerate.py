# import random

# def generate_otp(length=4):
#     digits = "0123456789"
#     otp = "".join(random.choice(digits) for _ in range(length))
#     return otp

# print("Your OTP is:", generate_otp())

# import random
# import string
# import time
# import os

# def generate_otp(length=4, visible_seconds=5):
#     digits = string.digits
#     otp = "".join(random.choice(digits) for _ in range(length))

#     print(f"Your OTP is: {otp}")
#     time.sleep(visible_seconds)

#     os.system('cls')

#     print("OTP expired!")

# generate_otp(4, 5)