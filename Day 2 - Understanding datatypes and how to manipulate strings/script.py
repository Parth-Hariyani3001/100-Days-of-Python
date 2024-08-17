# len method for string
print(len("Parth"))

# Subscripting
print("Hello"[-1])
print("Hello"[0])

# String
print("123"+"345")

# Variable = Whole number
print(123+345)

# Large integers
print(10_000_000)

# Floating point number
print(3.14)

# Boolean
print(True)
print(False)

# type method
print(type(123), type("Hello"))

# Type coversion
print(bool(9))
print(int("132"))
print(str(123))
print(float(321))

# Mathematical operators
print(10 + 2)
print(10 - 2)
print(10 / 2)
print(10 // 2)
print(10 ** 2)
print(10 * 2)

# PEMDAS
# ()
# **
#  * or /
#  + or -
print(3 * (3 + 3) / 3 - 3)

# Number manipulation 
bmi = 64 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))

# f strings
score = 70
height = 10.5
weight = 64
isWinning = True
print("Your score is : " + str(score))
print(f"YOur score is {score} and your height and weight is {height} , {weight} and your winning is {isWinning}")