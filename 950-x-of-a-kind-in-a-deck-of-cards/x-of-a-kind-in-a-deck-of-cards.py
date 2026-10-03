class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        freq={}
        for i in deck:
            freq[i]=freq.get(i,0)+1
        val=freq[deck[0]]
        mini=min(freq.values())
        while mini>=2:
            check=True
            for val in freq.values():
                if val%mini!=0:
                    check=False
                    break
            if check:
                return True
            mini-=1
        return False