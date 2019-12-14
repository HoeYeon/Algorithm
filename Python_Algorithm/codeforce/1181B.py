l = int(input());
s = input()
j = l//2
i = j+1
while j>0 and s[j]=='0':j-=1
while i<l and s[i]=='0':i+=1
print(min(int(s[0 if i>=l else i:])+int(s[:i]), int(s[j:])+int(s[: l if j==0 else j])))
