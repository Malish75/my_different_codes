"""
Strong password generator with a choice of arbitrary length from 8 to 10000
"""
import random

def pass_gen():
    """ Strong password generator
    :return: yours password as str
    """
    len_pass = int(input("Enter the password length (number): "))
    l_up, l_low, symb, num = 'ABCDEFGHIKLMNOPQRSTVXYZ', 'abcdefghiklmnopqrstvxyz',"@#$&", '0123456789'
    password = ''

    while True:
        if len_pass > 10000:
            len_pass = int(input("Too big! Length of number < 10к: "))
        elif len_pass < 8:
            len_pass = int(input("The length is recommended not less than 8: "))
        else:
            break

    while len(password) <= len_pass:
        password += random.choice(l_up)
        password += random.choice(l_low)
        password += random.choice(num)
        password += random.choice(l_up)
        password += random.choice(l_low)
        password += random.choice(num)
        password += random.choice(symb)

    return password[:len_pass]

print(pass_gen())