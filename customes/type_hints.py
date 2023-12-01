x = 'Atabek'
my_list = []
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# 1
greet(x) # prints string, but doesn't return

def greet_return(name: str) -> str:
    return f"Hello, {name}!"

# 2
greet_return(x) # can't see it but it returns a string

# you can append return value to data structures
my_list.append(greet_return(x))
print(my_list)
