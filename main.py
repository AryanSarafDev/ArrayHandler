import os


class player:
    def __init__(self):
        self._position = list()

    @property
    def array(self):
        return self._position

    @array.setter
    def array(self, newPosition):
        self._position = newPosition
        print(self._position)


    @property
    def insert(self):
        return self._position

    @insert.setter
    def insert(self, newPosition):
        self._position.insert(newPosition[0],newPosition[1])
        print(self._position)

    @property
    def change(self):
        return self._position

    @change.setter
    def change(self, newPosition):
        self._position[newPosition[0]]=newPosition[1]
        print(self._position)

    @property
    def removeElement(self):
        return self._position

    @removeElement.setter
    def removeElement(self, newPosition):
        self._position.remove(newPosition)
        print(self._position)

    @property
    def getArray(self):
        print(self._position)
        return self._position





def bubbleSort(arr):
    p = player()
    p.array = arr
    n = len(p.array)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if p.array[j] > p.array[j + 1]:
                swapped = True
                temp=(p.array[j])
                p.change= ( j,(p.array[j+1]),)
                p.change= (j+1,temp)

        if not swapped:

            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
