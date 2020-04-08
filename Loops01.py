# Creating a fizzbuzz loop
# for any number divisible by 3, print fizz
# for any number divisible by 5, print buzz
# for any number divisible by 3 & 5 (15), print fizzbuzz

for i in range(1, 100):
    if (i % 3) == 0 and (i % 5) == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

