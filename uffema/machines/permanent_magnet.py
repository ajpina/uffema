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
    Base class for permanent magnet synchronous machines
"""

# ==========================================================================
# Program:   permanent_magnet.py
# Author:    ajpina
# Date:      12/23/16
# Version:   0.1.1
#
# Revision History:
#      Date     Version    Author      Description
#  - 12/23/16:  0.1.1      ajpina      Defines mandatory methods and properties
#
# ==========================================================================

__author__ = 'ajpina'

import abc

from uffema.machines import Synchronous


class PermanentMagnet(Synchronous):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def stator(self):
        return 'Should never see this'

    @stator.setter
    def stator(self, new_stator):
        return

    @abc.abstractproperty
    def rotor(self):
        return 'Should never see this'

    @rotor.setter
    def rotor(self, new_rotor):
        return

    @abc.abstractproperty
    def flux(self):
        return 'Should never see this'

    @flux.setter
    def flux(self, new_flux):
        return

    @abc.abstractproperty
    def mode(self):
        return 'Should never see this'

    @mode.setter
    def mode(self, new_mode):
        return

    @abc.abstractproperty
    def type(self):
        return 'Should never see this'

    @type.setter
    def type(self, new_type):
        return

    def get_type(self):
        return 'PermanentMagnet'

    def __init__(self, machine_settings):
        super(PermanentMagnet, self).__init__(machine_settings)
        self.type = self.type + 'PermanentMagnet::'




