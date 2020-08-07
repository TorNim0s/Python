"""
class Pixel:
    def __init__(self,x = 0,y = 0,red = 0,green = 0,blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        self._red = 83
        self._green = 83
        self._blue = 83

    def getmissing(self):
        if self._red == self._green and self._red == 0:
            return "Blue"
        elif self._green == self._blue and self._green == 0:
            return "Red"
        elif self._blue == self._red and self._red == 0:
            return "Green"
        else:
            return ""

    def print_pixel_info(self):
        print ("X: {}, Y: {}, Color: ({}, {}, {}) {}".format(self._x,self._y,self._red,self._green,self._blue, self.getmissing()))

def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

main()
"""

class BigThing:
    def __init__(self, item):
        self._item = item

    def size(self):
        if type(self._item) == list or type(self._item) == dict or type(self._item) == str:
            return len(self._item)
        return self._item

class BigCat(BigThing):
    def __init__(self, item, weight):
        BigThing.__init__(self, item)
        self._weight = weight

    def size(self):
        BigThing.size(self)
        if self._weight > 20:
            return ("Very Fat")
        elif self._weight <= 20 and self._weight > 15:
            return ("Fat")
        else:
            return ("OK")


def main():
    #my_thing = BigThing("eldad")
    #print(my_thing.size())

    cutie = BigCat("mitzy", 22)
    print(cutie.size())

main()
