import time
import random

def exec_job():
  time.sleep(random.randint(5, 20))
  print "success"

if __name__ == "__main__":
  exec_job()
