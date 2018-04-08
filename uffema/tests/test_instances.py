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
# Program:   test_instances.py
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
import json

from uffema.machines import *


def main():
    with open('uid_sid_aid_9s6p.msf') as msf:
        machine_settings = json.load(msf)
    spm = RotatingMachine.create(machine_settings['machine'])
    print spm.type
    print spm.stator.type
    print spm.stator.slots[0].type
    print spm.stator.winding.type
    print spm.rotor.type
    print spm.rotor.magnets[0].type
    return 1


if __name__ == '__main__':
    sys.exit(main())
