from time import sleep,ctime

def movie(loop,func):
    for i in range(loop):
        print("I was at the %s! %s" %(func , ctime()))
        sleep(2)
def music(loop,func):
    for i in range(loop):
        print("I was listen to %s! %s" %(func, ctime()))
        sleep(5)
        
if __name__ == "__main__":
    movie(2,"愛情")
    music(2,'夜貓組')
    print('end to %s' %ctime())