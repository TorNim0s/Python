import functools

class InvalidID(Exception):
    """
    Exception that called when an id is not 9 numbers.
    """
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return ("invalid ID, required 9 numbers -> input{} ".format(self._id))

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
    try:
        if len(str(id)) != 9:
            raise InvalidID(id)

        list_numbers = list(str(id)) # make a list of the id numbers (in str format)
        sumofnumbers = combinenumber(checknumber(multiplynum(convertoint(list_numbers)))) # make the math on the id to check if valid

        if sumofnumbers % 10 == 0: # check if the sum of the numbers after the math is divided by 10 with no remander
            return True
        return False

    except InvalidID as error:
        print(error)

class IDIterator:
    """
    create valid ids
    """
    def __init__(self):
        self._id = 123456780 # create id and give him the value of before the first valid id

    def __iter__(self):
        return self # point on the current id

    def __next__(self):
        """
        :return: the next valid id if id is 9 numbers
        """
        self._id += 1

        while not check_id_valid(self._id): # loop until valid id has been choosed
            if len(str(self._id)) > 9:
                raise StopIteration

            self._id += 1

        return self._id

def id_generator (id):
    """
    :param id: the start point to generate ids
    :return: next valid id
    """
    while len(str(id)) == 9:
        id += 1
        while not check_id_valid(id):  # loop until valid id has been choosed
            id += 1
        yield id

def main():
    id = iter(IDIterator()) # create an id iter maker

    for i in range(10):
        print(next(id))  # print 10 valid ids

    valid_id = id_generator(123456780) # create an id generator

    for i in range(10):
       print(next(valid_id)) # print 10 valid ids

if __name__ == "__main__":
    main()
