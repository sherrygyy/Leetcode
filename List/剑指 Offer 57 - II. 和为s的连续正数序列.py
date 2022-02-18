class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = []
        res = []
        for i in range(1, target + 1):
            l.append(i)
        i = 0
        j = 1
        while i < j and j <= target/2:
            if sum(l[i:j+1]) == target:
                res.extend([l[i:j+1]])
                j = j + 1
            else:
                if sum(l[i:j+1]) < target:
                    j = j + 1
                else:
                    i = i + 1
        return res