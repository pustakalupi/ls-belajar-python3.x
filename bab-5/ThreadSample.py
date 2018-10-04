'''
done
'''
import _thread
import time

class PenampungThread:
    def __init__(self, threadName):
        self.name = threadName

    def run(self, delay):
        ctr = 0
        while 1:
            time.sleep(delay)
            print ("%s: %s" % (self.name, str(ctr)))
            ctr+=1

th1 = PenampungThread("thread-pisang")
th2 = PenampungThread("thread-mangga")

try:
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
except:
      print ("Error: tidak bisa memulai thread")

while 1:
      pass