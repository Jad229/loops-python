# Divisible by 3 say Fizz
# Divisible by 5 say Buzz
# Divisible by 3 & 5 say FizzBuzz

for number in range(1, 101):
    if(number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)