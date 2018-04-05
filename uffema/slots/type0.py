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

    def __init__(self, slot_settings):
        self._h0 = slot_settings['h0']
        self._h1 = slot_settings['h1']
        self._h2 = slot_settings['h2']
        self._h3 = slot_settings['h3']
        self._w0 = slot_settings['w0']
        self._w1 = slot_settings['w1']
        self._w2 = slot_settings['w2']
        self._SOp = slot_settings['SOpos']
        self._Sp = slot_settings['Spos']
        # It is assumed an insulation liner of 0.5mm thickness
        self._lt = 0.5e-3

    def get_slot_center(self):
        return self._h0 + self._h1 + (2.0/3.0)*self._h2

    def get_type(self):
        return 0

    def get_area(self):
        return 0

    def get_slot_total_height(self):
        return self._h0 + self._h1 + self._h2 + self._h3
