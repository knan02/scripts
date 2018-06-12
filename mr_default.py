import time, sys, shlex

def exec_job():
  print ('started executing emr job with following args: ')
  print sys.argv
  time.sleep(20)
  print ('finished executing emr job')

if __name__ == "__main__":
  exec_job()
