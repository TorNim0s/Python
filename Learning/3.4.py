class UsernameOutOfBound(Exception):
    def __init__(self, args):
        self._args = args

    def __str__(self):
        return("Current input is out of bound 3 - 18 -> input: {}".format(self._args))

    def get_args(self):
        return self._args

class PassOutOfBound(Exception):
    def __init__(self, args):
        self._args = args

    def __str__(self):
        return("Current input is out of bound 8 - 40-> input: {}".format(self._args))

    def get_args(self):
        return self._args

class InvalidLetter(Exception):
    def __init__(self, letter, username):
        self._letter = letter
        self._username = username

    def __str__(self):
        return("Wrong syntax, must has only english letter, numbers, or under scor -> input: {} letter {}".format(self._letter, self._username))

    def get_args(self):
        return self._letter

class PasswordMissingCharacter(Exception):
    def __init__(self, lettter):
        self._letter = lettter

    def __str__(self):
        return ("Missing 1 of the components - {}".format(self._letter))

    def get_args(self):
        return self._letter

class Uppercase(PasswordMissingCharacter):
    def __init__(self, lettter):
        self._letter = lettter

    def __str__(self):
        return ("Missing Upper letter for the password -> ".format(self._letter))

    def get_args(self):
        return self._letter

class Lowercase(PasswordMissingCharacter):
    def __init__(self, lettter):
        self._letter = lettter

    def __str__(self):
        return ("Missing Lower letter for the password -> ".format(self._letter))

    def get_args(self):
        return self._letter

class Digit(PasswordMissingCharacter):
    def __init__(self, lettter):
        self._letter = lettter

    def __str__(self):
        return ("Missing Digit letter for the password -> ".format(self._letter))

    def get_args(self):
        return self._letter

class Special(PasswordMissingCharacter):
    def __init__(self, lettter):
        self._letter = lettter

    def __str__(self):
        return ("Missing Special letter for the password -> ".format(self._letter))

    def get_args(self):
        return self._letter

def check_input(username, password):
    try:
        if len(username) > 16 or len(username) < 3:
            raise UsernameOutOfBound(username)

        for letter in username:
            if not str(letter).isalnum:
                raise InvalidLetter(letter, username)

        if len(password) > 40 or len(password) < 8:
            raise PassOutOfBound(password)

        Upper = False
        Lower = False
        Num = False
        Sign = False

        for letter in password:
            if letter.isalpha():
                if letter.isupper():
                    Upper = True
                else:
                    Lower = True

            if letter.isdigit():
                Num = True

            if not letter.isalnum():
                Sign = True
        if not Upper:
            raise Uppercase(password)
        elif not Lower:
            raise Lowercase(password)
        elif not Num:
            raise Digit(password)
        elif not Sign:
            raise Special(password)


    except UsernameOutOfBound as e:
        print(e)
        getinput()

    except InvalidLetter as e:
        print(e)
        getinput()

    except PassOutOfBound as e:
        print(e)
        getinput()

    except PasswordMissingCharacter as e:
        print(e)
        getinput()

    else:
        print("OK")

def getinput():
    username = input("enter username")
    password = input("enter password")
    check_input(username,password)

def main():
    getinput()

main()