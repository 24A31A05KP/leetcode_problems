class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sentence=text.split(" ")
        words=0
        for i in sentence:
            check=False
            for j in brokenLetters:
                if j in i:
                    check=True
                    break
            if not check:
                words+=1
        return words