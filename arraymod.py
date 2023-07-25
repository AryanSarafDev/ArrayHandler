import os
import json

class player:

    def __init__(self):
        self._position = list()
        self.send = list()

    @property
    def array(self):
        return self._position


    @array.setter
    def array(self, newPosition):
        self._position = newPosition
        print(self._position)
        self.send.append(self._position)


    @property
    def insert(self):
        return self._position

    @insert.setter
    def insert(self, newPosition):
        self._position.insert(newPosition[0],newPosition[1])
        print(self._position)
        self.send.append(self._position)

    @property
    def change(self):
        return self._position

    @change.setter
    def change(self, newPosition):
        self._position[newPosition[0]]=newPosition[1]
        print(self._position)
        b=list()
        for x in self._position:
            b.append(x)
        self.send.append(b)

    @property
    def removeElement(self):
        return self._position


    @removeElement.setter
    def removeElement(self, newPosition):
        self._position.remove(newPosition)
        print(self._position)
        self.send.append(self._position)

    @property
    def getArray(self):
        return self.send