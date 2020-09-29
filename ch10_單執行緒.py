from time import sleep, ctime

def music():
    print("I was listening to music %s" %ctime())
    sleep(2)
def movie():
    print("I was at the movie %s" %ctime())
    sleep(5)
if __name__ == '__main__':
    music()
    movie()
print('All end in %s' %ctime())