class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        maximum = 0
        for i in self.__elements:
            for j in self.__elements:
                diff = abs(i-j)
                if diff > maximum:
                    maximum = diff
        self.maximumDifference = maximum

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
