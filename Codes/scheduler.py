import pyodbc
import pandas as pd
import random
import sys
from datetime import datetime, timedelta
import threading
import time
from time import sleep
from al_prediction import main


# repeated timer runs the function at an interval specified by user
class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


if __name__ == '__main__':

    print("starting...")
    # args for RepeatedTimer initialization are -> interval, function, *args
    # "main" is the main function from the al_prediction script
    start = datetime.now()
    end = start + timedelta(minutes = 1)
    rt = RepeatedTimer(5, main)
    while datetime.now().second <= 55:
        sleep(5)

    print("ending time:", datetime.now())
    rt.stop()


    # deprecated
    # print("starting...")
    # # args for RepeatedTimer initialization are -> interval, function, *args
    # rt = RepeatedTimer(5, main)
    # try:
    #     sleep(5)
    #     print("starting")
    # finally:
    #     #rt.stop() # better in a try/finally block to make sure the program ends
    #     print("end")
