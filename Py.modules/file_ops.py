
## open a new file
try:
    f = open('myfile.txt', 'r')
    print(f.read())
    #print(f.readline())
    #print(f.readlines())
finally:
    f.close()

##  open a new file2
try:
     f = open('myfile2.txt', 'r')
     line = f.readline()
     while line:
         print(line)
         line = f.readline()
    #print(f.readlines())
finally:
 f.close()


 ## with option
print('**using with option**')
with open('myfile3.txt', 'r') as f:
    print(f.readline())
    list2 = f.read().split("\n")
    print(list2)


print('**using with option2**')
with open('myfile3.txt', 'r') as f:
    #print(f.readline())
    #list2 = f.read().split("\n")
    #print(list2)
    for line in f:
        print(line.strip())