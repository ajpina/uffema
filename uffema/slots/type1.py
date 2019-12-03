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
    Class for slots of type 1
"""

# ==========================================================================
# Program:   type1.py
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

import numpy as np

from uffema.slots import Slot
from uffema.misc.constants import *


class Type1(Slot):
    @property
    def h0(self):
        return self._h0

    @h0.setter
    def h0(self, value):
        self._h0 = value

    @property
    def h2(self):
        return self._h2

    @h2.setter
    def h2(self, value):
        self._h2 = value

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

    def __init__(self, slot_settings, stator_mode):
        super(Type1, self).__init__(slot_settings)
        self.h0 = slot_settings['h0']
        self.h2 = slot_settings['h2']
        self.w0 = slot_settings['w0']
        self.w1 = slot_settings['w1']
        self.w2 = slot_settings['w2']
        self.so_position = slot_settings['SOpos']
        self.s_position = slot_settings['Spos']
        # It is assumed an insulation liner of 0.5mm thickness
        self.liner_thickness = 0.5e-3
        self.type = self.type + 'Type1'

    def get_slot_center(self):
        return self.h0 + (2.0/5.0)*self.h2

    def get_type(self):
        return 'Type1'

    def get_area(self):
        return 0

    def get_slot_total_height(self):
        return self.h0 + self.h2

    def get_conductor_area_width(self):
        return (self.w1 + self.w2) / 2.0

    def get_conductor_area_height(self):
        return self.h2

    def get_coil_area_base_point(self, inner_radius):
        return inner_radius + self.h0

    def get_slot_opening_geometry(self, inner_radius):
        angle_slot_opening_bottom = np.arcsin(-(self.w0/2.0)/ inner_radius + self.h0 )
        angle_slot_opening_top = np.arcsin(-(self.w0 / 2.0) / inner_radius )
        points = {
            '2': [inner_radius, 0, 0],
            '3': [inner_radius + self.h0, 0, 0],
            '4': [(inner_radius + self.h0)*np.cos(angle_slot_opening_bottom), (inner_radius + self.h0)*np.sin(angle_slot_opening_bottom) , 0],
            '5': [(inner_radius)*np.cos(angle_slot_opening_bottom), (inner_radius)*np.sin(angle_slot_opening_bottom) , 0]
        }
        lines = {
            '1': [2, 3],
            '2': [3, 4],
            '3': [4, 5],
            '4': [5, 2]
        }
        return points, lines


    def get_slot_wedge_geometry(self, inner_radius):
        points = None
        lines = None
        return points, lines


    def get_backiron_geometry(self, inner_radius, outer_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        angle_slot_base = np.arcsin(-(self.w2 / 2.0) / (inner_radius + self.h2))
        points = {
            '6': [inner_radius + self.h2, 0, 0],
            '7': [outer_radius, 0, 0],
            '8': [outer_radius * np.cos( -slot_pitch/2.0 ), outer_radius * np.sin( -slot_pitch/2.0 ), 0],
            '9': [(inner_radius + self.h0 + self.h2) * np.cos( -slot_pitch/2.0 ),
                   (inner_radius + self.h0 + self.h2) * np.sin( -slot_pitch/2.0 ) , 0],
            '10': [(inner_radius + self.h2) * np.cos(angle_slot_base),
                  (inner_radius + self.h2) * np.sin(angle_slot_base), 0]
        }
        lines = {
            '5': [6, 7],
            '6': [7, 1, 8],
            '7': [8, 9],
            '8': [9, 10],
            '9': [10, 1, 6]
        }
        return points, lines

    def get_tooth_geometry(self, inner_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        angle_slot_top = np.arcsin(-(self.w1 / 2.0) / (inner_radius + self.h0))
        points = {
            '11': [(inner_radius + self.h0 ) * np.cos( -slot_pitch/2.0 ),
                   (inner_radius + self.h0 ) * np.sin( -slot_pitch/2.0 ) , 0],
            '12': [(inner_radius + self.h0) * np.cos(angle_slot_top), (inner_radius + self.h0) * np.sin(angle_slot_top),
                  0]

        }
        lines = {
            '10': [9, 11],
            '11': [11, 1, 12],
            '12': [12, 10],
            '-8': [0]
        }
        return points, lines


    def get_coil_area_geometry(self, inner_radius):
        points = None
        lines = {
            '13': [12, 1, 4],
            '-2': [0],
            '14': [3, 6],
            '-9': [0],
            '-12': [0]
        }
        return points, lines

    def get_toothtip_geometry(self, inner_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        points = {
            '14': [inner_radius * np.cos( -slot_pitch/2.0 ), inner_radius * np.sin( -slot_pitch/2.0 ) , 0]
        }
        lines = {
            '15': [11, 14],
            '16': [14, 1, 5],
            '-3': [0],
            '-13': [0],
            '-11': [0]
        }
        return points, lines


    def get_stator_airgap_geometry(self, airgap_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        points = {
            '15': [airgap_radius * np.cos( -slot_pitch/2.0 ), airgap_radius * np.sin( -slot_pitch/2.0 ) , 0],
            '16': [airgap_radius, 0, 0]
        }
        lines = {
            '17': [14, 15],
            '18': [15, 1, 16],
            '19': [16, 2],
            '-4': [0],
            '-16': [0]
        }
        return points, lines

    def get_stator_airgap_boundary(self):
        return {'18': [15, 1, 16]}

    def get_outer_stator_boundary(self):
        return [6]

    def get_master_boundary(self):
        return [7, 10, 15, 17]
