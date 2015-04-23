def beef(arg1):
    if arg1 is "Bucky":
        print("helo Bucky")
    elif arg1 is "Lucy":
        print("Hi Lucy")
    else:
        print("enter a name")


def bitcoin_to_usd(btc):
    convert = btc * 500
    print(convert)


# bitcoin_to_usd(3)

def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

bucky_age = allowed_dating_age(27)
# print(bucky_age)


def gender(sex="unkwonw"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)
''''
gender('m')
gender('f')
gender()
'''''

def mult(*args):
    total = 0
    for a in args:
        total += a
    print(total)

# mult(2, 45, 17)

def healt_calc(age, apples, cigaretes):
    reslut = (100 - age)+ (apples * 1.5) -(cigaretes * 2)
    print(reslut)

bucky_data = [27, 15, 20]

healt_calc(*bucky_data)
healt_calc(bucky_data[0], bucky_data[1], bucky_data[2])



