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

import abc
import numpy as np

from uffema.misc import *


class Winding(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, winding_settings, Ns):
        self._phases = winding_settings['NoPhases']
        self._layers = winding_settings['Layers']
        self._conn = winding_settings['Conn']
        self._C = np.zeros((self._phases * self._layers, Ns), dtype=int)
        row = 0
        for la in range(0, self._layers):
            for ph in range(0, self._phases):
                for ns in  range(0, Ns):
                    self._C[row, ns] = winding_settings['CM'][LAYERS[la]][ns][PHASES[ph]]
                row += 1
        #self._mat = mat
        self._Cseries = winding_settings['Cseries']
        self._Cparallel = winding_settings['Cparallel']
        self._Cturns = winding_settings['Cturns']
        self._wih = winding_settings['wih']
        self._CondDiam = winding_settings['condDiam']
        self._Cpitch = winding_settings['Cpitch']
        self._SWl = 0
        self._EWl = 0

    @abc.abstractmethod
    def set_active_length(self, lsw):
        self._SWl = lsw

    @abc.abstractmethod
    def set_end_winding_length(self, Ns, iSr, slotCenter):
        pass

    @staticmethod
    def create(winding_settings, Ns):
        winding_type = winding_settings['type']
        if winding_type == 'concentrated':
            from uffema.windings import Concentrated
            winding_instance = Concentrated(winding_settings, Ns)
        elif winding_type == 'distributed':
            from uffema.windings import Concentrated
            winding_instance = Concentrated(winding_settings, Ns)
        else:
            from uffema.windings import Concentrated
            winding_instance = Concentrated(winding_settings, Ns)
        return winding_instance
