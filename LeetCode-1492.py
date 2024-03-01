class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        tempArray = []
        if n == 1:
            tempArray.append(n)
        for val in range(int(n/2)):
            factor = val+1
            if (n % (factor) == 0):
                tempArray.append(factor)
        print(tempArray)
        tempArray.append(n)
        if (k > len(tempArray)):
            return -1
        else:
            return tempArray[k-1]
