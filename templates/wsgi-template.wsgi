#!/usr/bin/python
import sys,os,re
sys.path.insert(1, "%WEB_ROOT%")
from %APP_NAME% import app as application
userenv = '/usr/local/osmosix/etc/userenv'
p = re.compile('^export (.*)="(.*)"$')
with open(userenv) as file:
        for line in file:
                match = re.match(p, line)
                os.environ[match.group(1)] = match.group(2)
