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

__author__ = 'ajpina'

from uffema.misc import *
from uffema.slots import Slot
from uffema.windings import Winding


class Stator:

    def __init__(self, stator_settings):
        self._Ns = stator_settings['Ns']
        self._iSr = stator_settings['iSr']
        self._oSr = stator_settings['oSr']
        self._Sl = stator_settings['Sl']
        slots_settings = stator_settings['slots']
        self._slots = Slot.build_slots(slots_settings)
        winding_settings = stator_settings['winding']
        self._winding = Winding.build_winding(winding_settings)

    @staticmethod
    def build_stator(stator_settings):
        stator_type = stator_settings['type']
        if stator_type == 'StandardOuter':
            from uffema.stators import StandardOuterStator
            stator_instance = StandardOuterStator(stator_settings)
        elif stator_type == 'StandardInner':
            from uffema.stators import StandardOuterStator
            stator_instance = StandardOuterStator(stator_settings)
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
