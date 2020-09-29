from time import sleep,ctime
import threading

def super_player(file,time):
    for i in range(2):
        print("Start playing: %s %s"%(file , ctime()))
        sleep(time)
        
lists = {'愛情買賣.mp3':3 ,'阿凡達.mp4':5 ,'我和妳.mp3':4}

thread = []
files = range(len(lists))

for file,time in lists.items():
    t = threading.Thread(target=super_player,args=(file,time))
    thread.append(t)
    
if __name__ == '__main__':
    for t in files:
        thread[t].start()
    
    for t in files:
        thread[t].join()
        
    print('end: %s' %ctime())