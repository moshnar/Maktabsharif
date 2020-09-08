#s= input("Enter any String ...")
s = '11221133444'
count=1
output=''
outputFormat= '({},{})'
if len(s)>1:
    for i in range(1,len(s)):
       if s[i-1]==s[i]:
          count+=1
       else :
           output += outputFormat.format(count,s[i-1])
           count=1
    output += outputFormat.format(count,s[i])
else:

    output = "the string is empty"


print (output)


