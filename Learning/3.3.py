class UnderAge(Exception):
    def __init__(self, args):
        self._args = args

    def __str__(self):
        return("Exception, Human under age 18 he is {}".format(self._args))

    def get_args(self):
        return self._args

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print("under age")
        print(e)
    else:
        print("You should send an invite to " + name)

send_invitation("eldad",20)
