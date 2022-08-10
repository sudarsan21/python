with open('file1.txt','w')as f:
    n=int(input('enter the number of lines of data:'))
    for i in range(n):
        data=input('enter the next line of data:')
        f.write(data+'\n')
with open('file1.txt','r')as f:
   with open ('file2.txt','w')as s:
       for i in f:
            s.write(i)
   with open('file2.txt','r')as s:
        print('the content of file2 is:\n',s.read())
   with open('file1.txt','r')as f:
       d=f.read()
       l=d.split()
       count=0
for i in l:
          count=count+1
print('number of words copied from file1 to file2 is:',count)
