class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        ops = []
        for i in operations:
            if i=="D":
                double = 2*ops[-1]
                ops.append(double)
                sum+=double
            elif i=="+":
                add=ops[-1]+ops[-2]
                ops.append(add)
                sum+=int(add)
            elif i=="C":
                remove=ops.pop()
                sum-=remove
            else:
                score=int(i)
                ops.append(score)
                sum+=score
        return sum