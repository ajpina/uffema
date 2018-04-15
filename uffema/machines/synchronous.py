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
    Base class for synchronous motors.
"""

# ==========================================================================
# Program:   synchronous.py
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

from abc import abstractmethod

from uffema.machines import RotatingMachine


class Synchronous(RotatingMachine):

    @property
    @abstractmethod
    def stator(self):
        return 'Should never see this'

    @stator.setter
    @abstractmethod
    def stator(self, new_stator):
        return

    @property
    @abstractmethod
    def rotor(self):
        return 'Should never see this'

    @rotor.setter
    @abstractmethod
    def rotor(self, new_rotor):
        return

    @property
    @abstractmethod
    def flux(self):
        return 'Should never see this'

    @flux.setter
    @abstractmethod
    def flux(self, new_flux):
        return

    @property
    @abstractmethod
    def mode(self):
        return 'Should never see this'

    @mode.setter
    @abstractmethod
    def mode(self, new_mode):
        return

    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Synchronous'

    def __init__(self, machine_settings):
        super(Synchronous, self).__init__(machine_settings)
        self.type = self.type + 'Synchronous::'



