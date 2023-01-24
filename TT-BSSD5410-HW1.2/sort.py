#############################################
# Selection sort code taking from:
# url: https://big-o.io/algorithms/comparison/selection-sort/
# on: 01/19/2023
#############################################

def selection_sort(array):
    currentIndex = 0
    while currentIndex < len(array) - 1:
        minIndex = currentIndex
        i = currentIndex + 1
        while i < len(array):
            if (array[minIndex] > array[i]):
                minIndex = i
            i += 1
        if (minIndex != currentIndex):
            temp = array[minIndex]
            array[minIndex] = array[currentIndex]
            array[currentIndex] = temp
        currentIndex += 1

# end def selection_sort(array):
