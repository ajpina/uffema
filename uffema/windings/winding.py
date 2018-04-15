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

from abc import ABCMeta, abstractmethod
import numpy as np

from uffema.misc import *


class Winding(metaclass=ABCMeta):

    @property
    def phases(self):
        return self._phases

    @phases.setter
    def phases(self, value):
        self._phases = value

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, value):
        self._layers = value

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, value):
        self._conn = value

    @property
    def conn_matrix(self):
        return self._conn_matrix

    @conn_matrix.setter
    def conn_matrix(self, value):
        self._conn_matrix = value

    @property
    def coil_series(self):
        return self._coil_series

    @coil_series.setter
    def coil_series(self, value):
        self._coil_series = value

    @property
    def coil_parallel(self):
        return self._coil_parallel

    @coil_parallel.setter
    def coil_parallel(self, value):
        self._coil_parallel = value

    @property
    def turns_coil(self):
        return self._turns_coil

    @turns_coil.setter
    def turns_coil(self, value):
        self._turns_coil = value

    @property
    def wires_in_hand(self):
        return self._wires_in_hand

    @wires_in_hand.setter
    def wires_in_hand(self, value):
        self._wires_in_hand = value

    @property
    def conductor_diameter(self):
        return self._conductor_diameter

    @conductor_diameter.setter
    def conductor_diameter(self, value):
        self._conductor_diameter = value

    @property
    def coil_pitch(self):
        return self._coil_pitch

    @coil_pitch.setter
    def coil_pitch(self, value):
        self._coil_pitch = value

    @property
    def slot_winding_length(self):
        return self._slot_winding_length

    @slot_winding_length.setter
    def slot_winding_length(self, value):
        self._slot_winding_length = value

    @property
    def end_winding_length(self):
        return self._end_winding_length

    @end_winding_length.setter
    def end_winding_length(self, value):
        self._end_winding_length = value

    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Winding'

    def __init__(self, winding_settings, Ns):
        self.phases = winding_settings['NoPhases']
        self.layers = winding_settings['Layers']
        self.conn = winding_settings['Conn']
        self.conn_matrix = np.zeros((self.phases * self.layers, Ns), dtype=int)
        row = 0
        for la in range(0, self.layers):
            for ph in range(0, self.phases):
                for ns in  range(0, Ns):
                    self.conn_matrix[row, ns] = winding_settings['CM'][LAYERS[la]][ns][PHASES[ph]]
                row += 1
        #self._mat = mat
        self.coil_series = winding_settings['Cseries']
        self.coil_parallel = winding_settings['Cparallel']
        self.turns_coil = winding_settings['Cturns']
        self.wires_in_hand = winding_settings['wih']
        self.conductor_diameter = winding_settings['condDiam']
        self.coil_pitch = winding_settings['Cpitch']
        self.slot_winding_length = 0
        self.end_winding_length = 0
        self.type = 'Winding::'

    @abstractmethod
    def set_active_length(self, lsw):
        self.slot_winding_length = lsw

    @abstractmethod
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
