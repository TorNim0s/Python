import File1

class BirthdayCard(File1.GreetingCard):
    def __init__(self, recipient = "Dana Ev", sender = "Eyal Ch", sender_age = 0):
        File1.GreetingCard.__init__(self, recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        print("sender: {}, recipient: {}, age: {}".format(self._sender,self._recipient, self._sender_age))
