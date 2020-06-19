name = input("what's the safe word:")
age = input("how many rings on them trees:")


def print_string():
    print(name + age)

print_string()

def print_anything(any="any", thing="thuing"):
    print(any + thing)


print_anything(name, age)

def number_decades(hazzah):
    return int(hazzah)//10

print(number_decades(age))