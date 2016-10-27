__author__ = 'doshest'
import threading
import time
# Our thread class
class MyThread (threading.Thread):

    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)

    def run (self):
         while(True):
          time.sleep(5)
          print( str(self.__x))



# Start 10 threads.
for x in range(10):
    MyThread(x).start()