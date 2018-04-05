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

from uffema.materials import Material

from uffema.constants import *


class Magnet:
    def __init__(self, Ml = 2.75e-3, Mw = 12e-3, Mps = 1.0,
                 P = 8, iMr = 19.45e-3, mat = Material(), magType = 0,
                 delta = 0.0):
        self._Ml = Ml
        self._Mw = Mw
        self._Mps = Mps
        self._iMr = iMr
        self._oMr = iMr + Mps*Ml
        self._Miaa = (P/PI)*np.arcsin(Mw/(2.0*self._iMr))
        self._Moaa = (P/PI)*np.arcsin(Mw/(2.0*self._oMr))
        self._alpha_p_v = ((self._Miaa+self._Moaa)/2.0)
        self._delta_v = delta*DEG2RAD
        self._mat = mat
        self._M = (mat._Br/MU0)
        self._magType = magType

