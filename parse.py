#!/usr/bin/env python
from lxml import etree
from sys import argv, stdout
from glob import glob
import csv

cw = csv.writer(stdout, dialect='excel')
for infilename in glob('./*.html'):
    with open(infilename, 'r') as infile:
        tree = etree.HTML(infile.read())
        rows = tree.xpath('//tr[@bgcolor and count(td)=7]')
        print '%d rows' % len(rows)
        for row in rows:
            cw.writerow([str(td[0].text) for td in row])
