import os, traceback
#import system
#removed 'system' dependency because of circular import. yikes.

def ls():
    return os.listdir()

def cd(newDir):
    os.chdir(newDir) #TODO: limit cd so that it only can go inside the root directory (unless otherwise specified to be a root action)

def cwd():
    return os.getcwd()

def rF(file):
  try:
    return open(file).read()
  except IOError:
    return -1

def wF(file, data):
  open(file, '+w').write(data)

def aF(file, data):
  open(file, '+a').write(data)

#def dumpError(data):
#  overwriteFile(system.LROM.readTab('dumpfile'), str(data) + '\n' + str(traceback.extract_tb(data[2])))

def remF(path):
  if os.path.exists(path):
    os.remove(path)
    return True
  else:
    return False
