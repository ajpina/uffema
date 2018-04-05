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

from uffema.slots import Slot

class Type0(Slot):

    def __init__(self, h0 = 1.5e-3, h1 = 1.5e-3, h2= 12e-3, h3= 1e-3,
                 w0 = 2.3e-3, w1 = 17.9e-3, w2 = 17.9e-3, SOp = 0, Sp = 0):
        self._h0 = h0
        self._h1 = h1
        self._h2 = h2
        self._h3 = h3
        self._w0 = w0
        self._w1 = w1
        self._w2 = w2
        self._SOp = SOp
        self._Sp = Sp
        # It is assumed an insulation liner of 0.5mm thickness
        self._lt = 0.5e-3

    def get_slot_center(self):
        return self._h0 + self._h1 + (2.0/3.0)*self._h2

    def get_slot_type(self):
        return 0

    def get_slot_total_height(self):
        return self._h0 + self._h1 + self._h2 + self._h3
