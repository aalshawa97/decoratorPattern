#Abdullah Mutaz Alshawa
#6/16/23
# This is a sample Python script for the decorator pattern.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #Formatted strings
    message = f'Mashallah, {name} is a coder!'
    print(message)

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
@do_twice
def greet(name):
    print(f"Hello, {name}!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #my_inp = input*
    #print_hi('PyCharm')
    greet("World")
    name = input('What is your name?')
    #Error checking
    if len(name) < 1:
        raise Exception("Error, why did you not supply a name?")
    print_hi(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
