import pyodbc
import pandas as pd
import random
import sys
from datetime import datetime, timedelta
import threading
import time
from time import sleep

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


# function which looks for latest sample data
def update_first_sample(status):

    # printing loop status
    print(status)

    # getting system starttime
    now = datetime.now()

    # creating connections with sql server
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=STEELDNA;'
                          'Database=DeS;'
                          'UID=sa;'
                          'PWD=admin@123;'
                          'Trusted_Connection=no;')

    cursor = conn.cursor()


    # reading the table which has information regarding sample chemistry
    sample_chemistry_data= pd.read_sql("SELECT TOP(100) * FROM heat_analysis order by SAMPLE_TIME desc", conn)

    # keeping only data points from the last 3 hours
    # window selected based on analysis
    sample_chemistry_data = sample_chemistry_data[sample_chemistry_data['SAMPLE_TIME']>= now - timedelta(minutes = 180)]

    # first we remove all records of LF5, as we are not predicting for that LF
    sample_chemistry_data = sample_chemistry_data[sample_chemistry_data['AGGREGATE'] != 'LF5']

    # for this, first we have to find the heats which have the latest sample information as first sample
    sample_latest = sample_chemistry_data.groupby('HEAT_NUMBER').agg({'SAMPLE_CODE':'max'})
    sample_latest = sample_latest[sample_latest['SAMPLE_CODE'] == '25101']
    sample_latest.reset_index(inplace = True)


    ######################################################################################################################
    # this is a temporary testing logic
    # to just see if we can push to the output table regularly
    # without having repeats in the heat number
    # this is the step where the actual regression equations would run
    # and the output would be stored in the master output table


    # getting the latest heat numbers from master_output_table
    # we've already predicted the outputs for this heat, so we don't need to predict again
    heat_numbers = pd.read_sql("SELECT TOP(50) HEAT_NUMBER FROM dbo.master_output_table_test ORDER BY SAMPLE_TIME desc",conn)
    heat_numbers = list(heat_numbers['HEAT_NUMBER'])
    heat_numbers = [str(x) for x in heat_numbers]

    # test logic
    # to be replaced
    op_table = sample_latest.copy()
    op_table = op_table[~op_table['HEAT_NUMBER'].isin(heat_numbers)]
    op_table['NODE'] = [random.randint(1,16) for x in range(len(op_table))]
    op_table['INSERT_DATETIME'] = now
    op_table = op_table.merge(sample_chemistry_data, on = 'HEAT_NUMBER', how = 'left')
    # keeping only required columns for now
    op_table = op_table[['HEAT_NUMBER','SAMPLE_TIME','INSERT_DATETIME','NODE']]

    # writing to output_test_table
    for index, row in op_table.iterrows():
        cursor.execute("INSERT into dbo.master_output_table_test (HEAT_NUMBER,SAMPLE_TIME,INSERT_DATETIME,NODE) values(?,?,?,?)", row['HEAT_NUMBER'], row['SAMPLE_TIME'], row['INSERT_DATETIME'], row['NODE'])

    # closing cursor
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    print("starting...")
    # args for RepeatedTimer initialization are -> interval, function, *args
    rt = RepeatedTimer(5, update_first_sample,"Started")
    try:
        sleep(5)
        print("success")
    finally:
        #rt.stop() # better in a try/finally block to make sure the program ends
        print("failed")
