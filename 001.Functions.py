def birthday_song(name):
    print("Happy Birthday to you......")
    print("Happy Birthday to you......")
    print("Happy Birthday ! Happy Birthday !......")
    print("Happy Birthday to you......")
    print(f"Happy Birthday {name}!")
birthday_song("bro")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print(add(1,2))
print(sub(2,3))
print(mul(2,3))
print(div(6,3))
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name=create_name("bro","code")
print(full_name)