def happy_number(number):
    ''' Check if a number is a happy number or not.

    :param number: The number to check.
    :type number: int
    '''
    seen = set()
    while number not in seen:
        seen.add(number) 
        digits = [int(x) for x in str(number)]
        number = sum([x**2 for x in digits])
        if number == 1:
            print("Your number is \'Happy\', yay!")
            return
        elif number == 4:
            print("Your number is sad :(")


if __name__ == "__main__":
    number = int(input("Enter a number to see if it's Happy or sad: "))
    happy_number(number)