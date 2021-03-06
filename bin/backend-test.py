#!/usr/bin/python
import sys, os
from subprocess import *
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))

# account for where we live
sys.path.append(scriptPath + '/..')
sys.path.append(scriptPath + '/../lib')

import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__ == '__main__':
   host = ''
   try:
      host = sys.argv[1]
   except:
      print "need a hostname to lookup";
      sys.exit()

   try:
      p = Popen("/opt/ogslb/bin/backend.py", shell=True, bufsize=256, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True) 
#      p = Popen("/opt/ogslb/bin/backend.py", shell=True, bufsize=256, stdin=PIPE, stdout=PIPE, close_fds=True) 
      (child_stdin, child_stdout) = (p.stdin, p.stdout)

      child_stdin.write('HELO\t1\n');
      child_stdin.flush()
      l = child_stdout.readline()
      print l
      child_stdin.write('Q\t%s\tIN\tANY\t-1\t127.0.0.1\n' % host);
      child_stdin.flush()
      l = child_stdout.readline()
      print l

      p.close()
   except:
      ''' '''
