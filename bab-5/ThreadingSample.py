'''
done
'''
import threading
import time

class PenampungThreading(threading.Thread):
    def __init__(self, threadID, name, delay, berapaKali):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.berapaKali = berapaKali

    def run(self):
        print ("Thread Dimulai: " + self.name)
        while self.berapaKali:
            time.sleep(self.delay)
            print ("%s: %s" % ( self.name, str(self.berapaKali) ))
            self.berapaKali -= 1
        print ("Thread Selesai: " + self.name)

th1 = PenampungThreading(1, "Thread-1", 2, 5)
th2 = PenampungThreading(2, "Thread-2", 1, 6)

th1.start()
th2.start()

th1.join()
th2.join()

print ("Keluar dari Main Thread....")