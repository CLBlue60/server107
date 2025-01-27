ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

#print the sum of all numbers in the list
def example1():
    total = 0
    for age in ages:
        total = total + age
    print(total)

example1()


#count how many users are 21 or older
def example2():
    count = 0
    for age in ages:
        if age >= 21:
            count = count + 1
    print(count)

example2()

#how many users are between 30 and 40 years old
def example3():
    count = 0
    for age in ages:
        if age >=30 and age <= 40:
            count = count +1
    print("There are "+ str(count)+" users between 30 and 40 years old")

example3()
