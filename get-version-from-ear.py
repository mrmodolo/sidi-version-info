#!/bin/env python2
# -*- coding: utf-8 -*-

import zipfile
import sys


def argparse():
    if len(sys.argv) < 2:
        print "Uso: get-version-from-ear.py EAR"
        sys.exit(1)

def get_ear_filename():
    return sys.argv[1]

def temp():
    zf = zipfile.ZipFile('sidi.ear', 'r')
    for filename in zf.namelist():
        if 'war' in filename:
            try:
                data = zf.read(filename)
                print type(data)
                if 'versao' in data:
                    print 'versao'
            except KeyError:
                print 'ERROR: Did not find %s in zip file' % filename
            else:
                print 'OK'
            print

def main():
    argparse()
    print get_ear_filename()

if __name__ == "__main__":
        main()

