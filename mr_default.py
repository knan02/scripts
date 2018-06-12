import time, sys, shleix, random

def exec_job():
  time.sleep(random.randint(0, 10))
  print "success"

if __name__ == "__main__":
  exec_job()
