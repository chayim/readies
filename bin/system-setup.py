#!/bin/sh
''''[ ! -z $VIRTUAL_ENV ] && exec python -u -- "$0" ${1+"$@"}; command -v python3 > /dev/null && exec python3 -u -- "$0" ${1+"$@"}; exec python2 -u -- "$0" ${1+"$@"} # '''

import sys
import os
import argparse

HERE=os.path.join(os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, ".."))
import paella

#----------------------------------------------------------------------------------------------

class SystemSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        # self.install("")
        # self.group_install("")
        # self.setup_pip()
        # self.pip_install("")
        pass

    def debian_compat(self):
        pass

    def redhat_compat(self):
        pass

    def fedora(self):
        pass

    def macosx(self):
        pass

    def common_last(self):
        pass

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
# parser.add_argument('--bool', action="store_true", help="flag")
# parser.add_argument('--int', type=int, default=1, help='number')
# parser.add_argument('--str', type=str, default='str', help='string')
args = parser.parse_args()

SystemSetup(nop = args.nop).setup()
