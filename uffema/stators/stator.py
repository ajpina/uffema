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
    Base class for stators.
"""

# ==========================================================================
# Program:   stator.py
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

from uffema.misc import *
from uffema.slots import Slot
from uffema.windings import Winding
from uffema.materials import Material


class Stator(metaclass=ABCMeta):

    @property
    def slots_number(self):
        return self._slots_number

    @slots_number.setter
    def slots_number(self, value):
        self._slots_number = value

    @property
    def inner_radius(self):
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value):
        self._inner_radius = value

    @property
    def outer_radius(self):
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, value):
        self._outer_radius = value

    @property
    def stack_length(self):
        return self._stack_length

    @stack_length.setter
    def stack_length(self, value):
        self._stack_length = value

    @property
    def slots(self):
        return self._slots

    @slots.setter
    def slots(self, value):
        self._slots = value

    @property
    def winding(self):
        return self._winding

    @winding.setter
    def winding(self, value):
        self._winding = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Stator'

    def __init__(self, stator_settings):
        self.slots_number = stator_settings['Ns']
        self.inner_radius = stator_settings['iSr']
        self.outer_radius = stator_settings['oSr']
        self.stack_length = stator_settings['Sl']
        if stator_settings['type'] == 'standardouter':
            self.mode = 'outer'
        else:
            self.mode = 'inner'
        self.slots = []
        for i, slot_settings in enumerate(stator_settings['slots']['dimension']):
            self.slots.insert(i, Slot.create(slot_settings, stator_settings['slots']['type'], self.mode))
        winding_settings = stator_settings['winding']
        self.winding = Winding.create(winding_settings, self.slots_number)
        self.winding.set_active_length(self.stack_length)
        slotCenter = self.slots[0].get_slot_center()
        self.winding.set_end_winding_length(self.slots_number, self.inner_radius, slotCenter)
        material_settings = stator_settings['material']
        self.material = Material.create(material_settings)
        self.type = 'Stator::'

    @staticmethod
    def create(stator_settings, machine_type):
        stator_type = stator_settings['type']
        if stator_type == 'standardouter':
            from uffema.stators import StandardOuterStator
            stator_instance = StandardOuterStator(stator_settings)
        elif stator_type == 'standardinner':
            from uffema.stators import StandardInnerStator
            stator_instance = StandardInnerStator(stator_settings)
        elif stator_type == 'standardinnerlinear':
            from uffema.stators import StandardInnerStatorLinear
            stator_instance = StandardInnerStatorLinear(stator_settings)
        else:
            from uffema.stators import StandardOuterStator
            stator_instance = StandardOuterStator(stator_settings)
        return stator_instance

    def get_resistances(self):
        Clength = 2*(self._winding._SWl + self._winding._EWl)
        Carea = PI * (self._winding._CondDiam / 2.0) ** 2
        Cresistance = ( self._winding._Cturns * self._winding._mat._rho *
                        Clength / (self._winding._wih * Carea))
        Phresistance = ( self._winding._Cseries * Cresistance /
                         self._winding._Cparallel )
        return Cresistance, Phresistance

    def __str__(self):
        output = "\tStator Characteristics:\n"
        output = output + "\t\t" + self.type + "\n"
        output = output + "\t\tSlots= " + str(self.slots_number) + "\n"
        output = output + self.slots[0].__str__()
        output = output + self.winding.__str__()

        return output
