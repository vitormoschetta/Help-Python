from random import randint

def is_even(num):
    if num in [1,3,5,7,9]:
        return False
    if num == 2:
        return True
    while True:
        a,b = randint(0, num), randint(0,num)

        if (a * b) == num:
            return is_even(a) or is_even(b)


result = is_even(8)
print(result)