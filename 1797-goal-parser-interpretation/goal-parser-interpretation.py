class Solution:
    def interpret(self, command: str) -> str:
        i=0
        s=''
        while i<len(command):
            if command[i]=='a':
                s+='al'
                i+=2
            elif command[i]==')':
                s+='o'
            elif command[i]=='G':
                s+='G'
            i+=1
        return s