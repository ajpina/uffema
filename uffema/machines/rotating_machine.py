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
    Abstract base class for rotating motors.
"""

# ==========================================================================
# Program:   rotating_machine.py
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

from abc import ABCMeta, abstractmethod

from uffema.stators import Stator
from uffema.rotors import Rotor
from uffema.misc.constants import *

class RotatingMachine(metaclass=ABCMeta):

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


    def get_machine_type(self):
        return 'RotatingMachine'


    def __init__(self, machine_settings, machine_type):
        self.type = 'RotatingMachine::'
        stator_settings = machine_settings['stator']
        self.stator = Stator.create(stator_settings, machine_type)
        rotor_settings = machine_settings['rotor']
        self.rotor = Rotor.create(rotor_settings, machine_type)

    @staticmethod
    def create(machine_settings):
        machine_type = machine_settings['type']
        if machine_type == 'spm':
            from uffema.machines import SurfacePermanentMagnet
            machine_instance = SurfacePermanentMagnet(machine_settings)
        elif machine_type == 'ipm':
            from uffema.machines import InteriorPermanentMagnet
            machine_instance = InteriorPermanentMagnet(machine_settings)
        elif machine_type == 'spm_linear':
            from uffema.machines import SurfacePermanentMagnetLinear
            machine_instance = SurfacePermanentMagnetLinear(machine_settings)
        else:
            from uffema.machines import SurfacePermanentMagnet
            machine_instance = SurfacePermanentMagnet(machine_settings)

        return machine_instance

    def __str__(self):
        output = "This is a Rotating Machine powered by UFFEMA Version {0}\n".format(UFFEMA_VERSION__)
        output = output + str("UFFEMA is Licensed under the Apache License,\n"
                              "Version 2.0\n\n")
        return output
