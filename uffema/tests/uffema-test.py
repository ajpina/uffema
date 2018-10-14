#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# ==========================================================================
# Copyright (C) 2016 Dr. Alejandro Pina Ortega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==========================================================================

"""
    Test for uffema objects.
"""

# ==========================================================================
# Program:   uffema-test.py
# Author:    ajpina
# Date:      12/23/16
# Version:   0.1.1
#
# Revision History:
#      Date     Version    Author      Description
#  - 12/23/16:  0.1.1      ajpina      Defines mandatory methods and properties
#
# ==========================================================================

import sys
import getopt
import json

from uffema.machines import *
from uffema.misc.constants import *


class Usage(Exception):
    def __init__(self, msg):
        self.msg = "[Error]: %s" % ( msg )


def main(argv=None):
    filename = None
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hvf:", ["help", "version", "file"])
        except getopt.GetoptError as msg:
            raise Usage(msg)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("This is UFFEMA Version {0}".format(UFFEMA_VERSION__))
                print("Usage: uffema-test.py [options] [filename]")
                print("Options:")
                print("-f, --file <filename>")
                sys.exit()
            elif opt in ("-v", "--version"):
                print("This is UFFEMA Version {0}".format(UFFEMA_VERSION__))
                sys.exit()
            elif opt in ("-f", "--file"):
                filename = arg

    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("for help use --help", file=sys.stderr)
        return 2

    if filename is None:
        raise Usage("algo")

    with open(filename) as msf:
        machine_settings = json.load(msf)
    spm = RotatingMachine.create(machine_settings['machine'])
    print(spm)
    return 1


if __name__ == '__main__':
    sys.exit(main())
