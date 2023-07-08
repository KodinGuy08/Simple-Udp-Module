import sys
import threading

class Thread (threading.Thread):
   args = ()

   def __init__(self, name, func, verbose=0):
      threading.Thread.__init__(self)
      self.name = name
      self.func = func
      self.status = False
      self.verbose = verbose
      
   def run(self):
      if self.verbose == 1:
          print ("Starting " + self.name)
      self.status = True
      
      self.func(*self.args)
      
      if self.verbose == 1:
          print ("Exiting " + self.name)
      self.status = False
