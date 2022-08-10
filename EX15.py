with open('file.txt','w')as f:
    n=int(input('Enter the number of lines of data:'))
    for i in range(n):
        data=input('Enter the next line of data:')
        f.write(data+'\n')
    with open('file.txt','r')as f:
      with open('files.txt','w')as s:
        for i in f:
            s.write(i)
            with open('files.txt','r')as s:
                print('The content of  file 2 is:\n',s.read())
            with open('file1'
                      '.txt','r')as f:
                d=f.read()
            l=d.split()
            count=0
            for i in l:
                cout=count+l
            print("Number  of words  copied from file1 to file2 is:",count)
