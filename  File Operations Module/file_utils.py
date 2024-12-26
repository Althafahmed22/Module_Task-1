def read_file(file):
    f=open(file,'r')
    print(f.readline())
def write_file(file, content):
    f=open('file','w')
    f.write(content)
def append_to_file(file, content):
    f=open('file','a')
    f.write(content)


