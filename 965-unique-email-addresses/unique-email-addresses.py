class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        s=set()
        for email in emails:
            i=0
            s1=''
            plus=False
            while i<len(email):
                if email[i]=='@':
                    s1+=email[i]
                    break
                if not plus:
                    if email[i]=='.':
                        i+=1
                        continue
                    elif email[i]=='+':
                        plus=True
                    else:
                        s1+=email[i]
                i+=1
            s1+=email[i+1:len(email)]
            s.add(s1)
        return len(s)        