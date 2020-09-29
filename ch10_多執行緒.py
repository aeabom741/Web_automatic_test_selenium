from time import sleep,ctime
import threading

def music(func,loop):
    for i in range(loop):
        print("I was listing %s %s" %(func , ctime()))
        sleep(2)
def movie(func,loop):
    for i in range(loop):
        print("I was at %s %s" %(func, ctime()))
        sleep(3)
threads = []

t1 = threading.Thread(target=music, args=('愛情買賣',3))
threads.append(t1)

t2 = threading.Thread(target=movie, args=('阿凡達',3))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
    print('all end %s' %ctime())