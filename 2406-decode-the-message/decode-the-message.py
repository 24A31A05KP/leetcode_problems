class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        map={}
        s=set()
        j=0
        for i in key:
            if i!=" ":
                if i not in s:
                    map[i]=chr(97+j)
                    j+=1
                    s.add(i)
        result=[]
        for i in message:
            result.append(map.get(i,' '))
        return "".join(result)