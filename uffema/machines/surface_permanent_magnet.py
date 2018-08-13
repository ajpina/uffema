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
    Class for permanent magnet synchronous motors of the type
    surface-mounted permanent magnets
"""

# ==========================================================================
# Program:   surface_permanent_magnet.py
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


from uffema.machines import PermanentMagnet


class SurfacePermanentMagnet(PermanentMagnet):

    @property
    def stator(self):
        return self._stator

    @stator.setter
    def stator(self, value):
        self._stator = value

    @property
    def rotor(self):
        return self._rotor

    @rotor.setter
    def rotor(self, value):
        self._rotor = value

    @property
    def flux(self):
        return self._flux

    @flux.setter
    def flux(self, value):
        self._flux = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_machine_type(self):
        return 'SPM'


    def __init__(self, machine_settings):
        PermanentMagnet.__init__(self, machine_settings, 'spm')
        self.type = self.type + 'SurfacePermanentMagnet'
        self.mode = 'Motor'
        self.flux = 'Radial'









