import os
import time
import threading
import pingdb


MIN_INTERVAL = 1
MAX_INTERVAL = 180

class PingService(threading.Thread):    
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.address = args[0]
        self.interval = int(args[1])
        self.dbh = pingdb.DatabaseHandler()
        if (self.interval < MIN_INTERVAL or self.interval > MAX_INTERVAL or\
            not isinstance(self.interval, int)):     
            self.interval = MIN_INTERVAL

    def run(self):
        while(True):
            time.sleep(self.interval)
            s_out = os.popen('ping %s -c 1 | grep -o \'[[:digit:]]'
                             '\{1,4\}\.[[:digit:]]\{1,3\} ms$\''
                             % self.address)\
                             .readline().replace(' ms\n', '')
            self.dbh.insert_value(float(s_out), time.time())
        
        