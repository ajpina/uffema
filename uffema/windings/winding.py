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
from uffema.materials import Material
from .conductors_disposition import ConductorsArea


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
    def conductor_type(self):
        return self._conductor_type

    @conductor_type.setter
    def conductor_type(self, value):
        self._conductor_type = value

    @property
    def conductor_diameter(self):
        return self._conductor_diameter

    @conductor_diameter.setter
    def conductor_diameter(self, value):
        self._conductor_diameter = value

    @property
    def conductor_height(self):
        return self._conductor_height

    @conductor_height.setter
    def conductor_height(self, value):
        self._conductor_height = value

    @property
    def conductor_width(self):
        return self._conductor_width

    @conductor_width.setter
    def conductor_width(self, value):
        self._conductor_width = value

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
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

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
        self.layers_type = winding_settings['LayersType']
        self.conn = winding_settings['Conn']
        self.turns_coil = winding_settings['Cturns']
        self.conn_matrix = np.zeros((self.phases * self.layers, Ns), dtype=int)
        row = 0
        a_plus_found = False
        for la in range(0, self.layers):
            for ph in range(0, self.phases):
                for ns in  range(0, Ns):
                    self.conn_matrix[row, ns] = self.turns_coil * winding_settings['CM'][LAYERS[la]][ns][PHASES[ph]]
                    if  not a_plus_found and winding_settings['CM'][LAYERS[la]][ns]['A'] == 1:
                        a_plus_slot = ns + 1
                        a_plus_found = True
                row += 1
        #self._mat = mat
        self.coil_series = winding_settings['Cseries']
        self.coil_parallel = winding_settings['Cparallel']
        self.wires_in_hand = winding_settings['wih']
        self.conductor_type = winding_settings.get('CondType','round')
        self.conductor_diameter = winding_settings.get('CondDiam', 0.0)
        self.conductor_height = winding_settings.get('CondHeight', 0.0)
        self.conductor_width = winding_settings.get('CondWidth', 0.0)
        self.coil_pitch = winding_settings['Cpitch']
        self.slot_winding_length = 0
        self.end_winding_length = 0
        self.conductors = ConductorsArea(self.layers, self.layers_type,
                                         self.conductor_type, self.conductor_diameter,
                                         self.conductor_height, self.conductor_width)
        material_settings = winding_settings['material']
        self.material = Material.create(material_settings)
        self.type = 'Winding::'
        slot_pitch = 360.0 / Ns
        self.armature_a_axis = slot_pitch * ( a_plus_slot + (self.coil_pitch / 2.0) - 1)
        self.coilside_conductor_area = self.wires_in_hand * self.turns_coil * PI * (self.conductor_diameter / 2.0)**2



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

    def get_conductors_geometry(self, width, height, base_point):
        return self.conductors.get_conductors_geometry( width, height, base_point)

    def get_air_around_conductors(self, points, lines):
        return self.conductors.get_air_around_conductors(points, lines)

    def get_armature_a_axis(self):
        return self.armature_a_axis

    def get_coilside_conductor_area(self):
        return self.coilside_conductor_area

    def __str__(self):
        output = "\t\t" + self.type + "\n"
        output = output + "\t\tWinding Phases= " + str(self.phases) + "\n"
        output = output + "\t\tWinding Layers= " + str(self.layers) + "\n"
        return output