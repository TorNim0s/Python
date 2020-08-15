import functools

def convertoint(list_str):
    """
    :param list_str: list of number in str format
    :return: list of number in int format
    """
    newlist = []
    for number in list_str: # loop on all of the number in the list
        newlist.append(int(number)) # convert them into int format

    return newlist # return list of numbers in int format

def multiplynum(list_numbers):
    """
    :param list_numbers: list of numbers to multiply
    :return: the numbers multiply following the rules
    ;command: the request is to multiply even positions, start from 0 so multiply the not even positions
    """

    for position in range(len(list_numbers)): # loop on all of the position in list_numbers
        if position % 2 != 0: # check if number is not in the even position
            list_numbers[position] *= 2 # multiply the number if not in the even position

    return list_numbers # return list of numbers multiplied

def checknumber(list_numbers):
    """
    :param list_numbers: check for numbers greater then 9
    :return: return list of number - if number was greater than 9 it sum the number -- 14 - 1 + 4 = 5
    """
    newlist = []
    for number in list_numbers:
        if number > 9:  # check if number is even
            number = functools.reduce(lambda x,y: int(x)+int(y), str(number)) # sum the number if greater than 9
        newlist.append(number) # adding the number to the new list

    return newlist # return new list with number not greater than 9

def combinenumber(list_numbers):
    return functools.reduce(lambda x, y: x + y, list_numbers) # combine all the numbers in the list

def check_id_valid(id):
    """
    :param id: ID is the id to check if is valid
    :return: True if id is valid, False if not
    """
    list_numbers = list(str(id)) # make a list of the id numbers (in str format)
    sumofnumbers = combinenumber(checknumber(multiplynum(convertoint(list_numbers)))) # make the math on the id to check if valid

    if sumofnumbers % 10 == 0: # check if the sum of the numbers after the math is divided by 10 with no remander
        return True
    return False

print(check_id_valid(123456782)) # print if id is valid -- True if valid -- False if not
