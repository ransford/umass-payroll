#!/usr/bin/env python

import random
from time import sleep
from os.path import getsize
import httplib
import urllib2

firstpage = 1
lastpage = 902

for pageno in range(firstpage, lastpage+1):
    URL = "http://www.bostonherald.com/projects/payroll/massachusetts/" + \
           "last_name.ASC/UMS//%d/" % pageno
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9')
        req.add_header('Accept-encoding', 'gzip')

        ofname = '%d.html.gz' % pageno
        with open(ofname, 'w') as ofile:
            ofile.write(urllib2.urlopen(req, timeout=10).read())

        sz = getsize(ofname)
        print "Got %s, %d bytes" % (ofname, sz)
        if not sz:
            raise Exception('%s is empty!' % ofname)
    except Exception, e:
        print e.reason
        break

    sleep(3.0 + random.random() * 3.0)
