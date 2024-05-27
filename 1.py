number=[1,2,5,9,7,6]
max_number=max(number)
print("max",max_number)

def find_max(list1):
    return max(list1)
a = find_max([1,6,4,8,5,3])
print("Max:", a)

class Number:
    def __init__(self, San):
        self.San = San
        self.max_San = max(San)
        print("Max san:", self.max_San)
San = (3, 5, 7, 2, 9, 10)
number = Number(San)