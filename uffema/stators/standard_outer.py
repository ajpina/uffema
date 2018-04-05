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

import numpy as np
from uffema.slots import Type0
from uffema.windings import Concentrated

from uffema.stators import Stator


class StandardOuterStator(Stator):

    def __init__(self, stator_settings):
        Ns = 12
        slots = []
        iSr = 22.95e-3
        oSr = 50.0e-3
        Sl = 30e-3
        winding = Concentrated()
        if not slots:
            for i in range(0, Ns):
                slots.insert(i, Type0())
                slots[i]._SOp = (2*np.pi/Ns)*i + np.pi/Ns
                slots[i]._Sp = (2*np.pi/Ns)*i + np.pi/Ns

        Stator.__init__(self, stator_settings)


