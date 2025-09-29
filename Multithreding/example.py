import threading
import time

def func(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)


# normal code
# func(4)
# func(3)
# func(2)


# threads using

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[2])

t1.start()
t2.start()
t3.start()