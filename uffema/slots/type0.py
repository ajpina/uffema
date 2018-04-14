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
    Class for slots of type 0
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

from uffema.slots import Slot


class Type0(Slot):
    @property
    def h0(self):
        return self._h0

    @h0.setter
    def h0(self, value):
        self._h0 = value

    @property
    def h1(self):
        return self._h1

    @h1.setter
    def h1(self, value):
        self._h1 = value

    @property
    def h2(self):
        return self._h2

    @h2.setter
    def h2(self, value):
        self._h2 = value

    @property
    def h3(self):
        return self._h3

    @h3.setter
    def h3(self, value):
        self._h3 = value

    @property
    def w0(self):
        return self._w0

    @w0.setter
    def w0(self, value):
        self._w0 = value

    @property
    def w1(self):
        return self._w1

    @w1.setter
    def w1(self, value):
        self._w1 = value

    @property
    def w2(self):
        return self._w2

    @w2.setter
    def w2(self, value):
        self._w2 = value

    @property
    def so_position(self):
        return self._so_position

    @so_position.setter
    def so_position(self, value):
        self._so_position = value

    @property
    def s_position(self):
        return self._s_position

    @s_position.setter
    def s_position(self, value):
        self._s_position = value

    @property
    def liner_thickness(self):
        return self._liner_thickness

    @liner_thickness.setter
    def liner_thickness(self, value):
        self._liner_thickness = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def __init__(self, slot_settings):
        super(Type0, self).__init__(slot_settings)
        self.h0 = slot_settings['h0']
        self.h1 = slot_settings['h1']
        self.h2 = slot_settings['h2']
        self.h3 = slot_settings['h3']
        self.w0 = slot_settings['w0']
        self.w1 = slot_settings['w1']
        self.w2 = slot_settings['w2']
        self.so_position = slot_settings['SOpos']
        self.s_position = slot_settings['Spos']
        # It is assumed an insulation liner of 0.5mm thickness
        self.liner_thickness = 0.5e-3
        self.type = self.type + 'Type0'

    def get_slot_center(self):
        return self.h0 + self.h1 + (2.0/3.0)*self.h2

    def get_type(self):
        return 'Type0'

    def get_area(self):
        return 0

    def get_slot_total_height(self):
        return self.h0 + self.h1 + self.h2 + self.h3
