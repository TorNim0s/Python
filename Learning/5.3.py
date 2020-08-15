class MusicNotes():
    def __init__(self):
        self._sounds = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 87.31, 98]
        self._counter = -1
        self._multiply = 1

    def getfreq(self, index):
        return self._sounds[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter >= len(self._sounds) - 1 and self._multiply >= 1* 2**4:
            raise StopIteration

        if self._counter == len(self._sounds) - 1:
            self._counter = -1
            self._multiply *= 2

        self._counter += 1
        return self.getfreq(self._counter) * self._multiply

sounds = iter(MusicNotes())

for item in sounds:
    print(item)