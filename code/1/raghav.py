#!/usr/bin/python

# Test Program by Raghav Potluri
# Group i

import traceback

def testResults(f):
  try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
  except Exception,e:
      print(traceback.format_exc()) 
  return f

@testResults
def _groupi():
    dictionary = {
      "smart" : "1+2"
    }
    assert dictionary['smart'] == 3

@testResults
def _groupi_valid():
    assert "String" == "String"