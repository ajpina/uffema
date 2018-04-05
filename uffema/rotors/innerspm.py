#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# ==========================================================================
## Copyright (C) 2016 Dr. Alejandro Pina Ortega
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
# ==========================================================================

__author__ = 'ajpina'

from emanpy.rotors import Rotor
from emanpy.src.constants import *

from emanpy.magnets import Magnet


class InnerRotorSPM(Rotor):

    def __init__(self, pp = 4, magnets = [], iRr = 6.0e-3, oRr = 19.45e-3,
                 Rl = 30e-3, init_pos = 0.0):
        Rotor.__init__(self, pp, iRr, oRr, Rl)
        if not magnets:
            self._magnets = []
            for i in range(0, 2*pp):
                self._magnets.insert(i, Magnet())
        else:
            self._magnets = magnets
        self._init_pos = init_pos * DEG2RAD