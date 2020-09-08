#s= input("Enter any String ...")
s = '11221133444'
count=1
output=''
outputFormat= '({},{})'#format the out put
if len(s)>1:#loop through  the string and count the occurance of each item
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


