import time, sys, shleix, random

def exec_job():
  print random.randint(0,10)
  time.sleep(random.randint(0, 10))
  print "success"

if __name__ == "__main__":
  exec_job()
