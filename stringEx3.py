string=" 1,2, 3 ,4,5"
string = string.split(',')

j=0
for i in string:
    string[j] = i.replace(" ", "")
    j=j+1
print(string)