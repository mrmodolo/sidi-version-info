#!/bin/env python2
# -*- coding: utf-8 -*-

import zipfile
import sys
import StringIO
import re


def argparse():
    if len(sys.argv) < 2:
        print "Uso: get-version-from-ear.py EAR"
        sys.exit(1)

def get_ear_filename():
    return sys.argv[1]

def get_version_content_from_ear(ear_filename):
    ear = get_ear_filename()
    try:
        with zipfile.ZipFile(ear, 'r') as ear_zf:
            filename = [f for f in ear_zf.namelist() if 'war' in f]
            if filename:
                memory_war = StringIO.StringIO()
                memory_war.write(ear_zf.open(filename[0]).read())
                with zipfile.ZipFile(memory_war) as war_zf:
                    filename = [f for f in war_zf.namelist() if 'versao.xml' in f]
                    if filename:
                        return war_zf.read(filename[0])
    except IOError:
        print 'Não foi possível abrir o arquivo %s' % ear
        sys.exit(1)
    except KeyError:
        print 'Não foi possível encontrar o arquivo  %s no pacote' % filename
        sys.exit(1)

def get_version(content, pattern):
    v = re.search(pattern, content)
    return v.group(0)

def main():
    argparse()
    ear_filename = get_ear_filename()
    versao_xml = get_version_content_from_ear(ear_filename)
    # var version = '1.6.4';
    print get_version(versao_xml, '([0-9]*\.[0-9]*\.[0-9]*)')
    sys.exit(0)

if __name__ == "__main__":
        main()

