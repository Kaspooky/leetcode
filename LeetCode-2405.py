class Solution:
    def partitionString(self, s: str) -> int:
        partitions = []
        currPartition = []
        for char in s:
            if char not in currPartition:
                currPartition.append(char)
            else:
                partitions.append(currPartition)
                currPartition.clear()
                currPartition.append(char)
        partitions.append(currPartition)
        return len(partitions)
