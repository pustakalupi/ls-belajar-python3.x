'''
done
'''
import threading
import time

class PenampungThreading(threading.Thread):
    def __init__(self, nama, delay, berapaKali):
        threading.Thread.__init__(self)
        self.nama = nama
        self.delay = delay
        self.berapaKali = berapaKali

    def run(self):
        print ("Thread Dimulai: " + self.nama)
        while self.berapaKali:
            time.sleep(self.delay)
            print ("%s: %s" % ( self.nama, str(self.berapaKali) ))
            self.berapaKali -= 1
        print ("Thread Selesai: " + self.nama)

th1 = PenampungThreading("Thread-1", 2, 5)
th2 = PenampungThreading("Thread-2", 1, 6)

th1.start()
th2.start()

th1.join()
th2.join()

print ("Keluar dari Main Thread....")