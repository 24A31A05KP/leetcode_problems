class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=b=0
        i,j=0,len(s)-1
        while i<j:
            if s[i].lower() in {'a','e','i','o','u'}:
                a+=1
            if s[j].lower() in {'a','e','i','o','u'}:
                b+=1
            i+=1
            j-=1
        return a==b