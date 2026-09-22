class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        window={}
        max_l=0
        left=0
        for right in range(len(fruits)):
            window[fruits[right]]=window.get(fruits[right],0)+1
            while len(window)>2:
                window[fruits[left]]-=1
                if window[fruits[left]]==0:
                    del window[fruits[left]]
                left+=1
            max_l=max(max_l,right-left+1)
        return max_l