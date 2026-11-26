class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]!=0:
                for j in range(i+1,len(batteryPercentages)):
                    if batteryPercentages[j]==0:
                        continue
                    batteryPercentages[j]-=1
        return sum(1 for i in batteryPercentages if i!=0)