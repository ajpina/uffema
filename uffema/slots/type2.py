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
    Class for slots of type 2
"""

# ==========================================================================
# Program:   type2.py
# Author:    ajpina
# Date:      08/30/18
# Version:   0.1.1
#
# Revision History:
#      Date     Version    Author      Description
#  - 08/30/18:  0.1.1      ajpina      Defines mandatory methods and properties
#
# ==========================================================================

__author__ = 'ajpina'

import numpy as np

from uffema.slots import Slot
from uffema.misc.constants import *


class Type2(Slot):
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
        super(Type2, self).__init__(slot_settings)
        self.h0 = slot_settings['h0']
        self.h1 = slot_settings['h1']
        self.h2 = slot_settings['h2']
        self.w0 = slot_settings['w0']
        self.w1 = slot_settings['w1']
        self.w2 = slot_settings['w2']
        self.so_position = slot_settings['SOpos']
        self.s_position = slot_settings['Spos']
        # It is assumed an insulation liner of 0.5mm thickness
        self.liner_thickness = 0.5e-3
        self.type = self.type + 'Type2'

    def get_slot_center(self):
        return self.h0 + self.h1 + (2.0/3.0)*self.h2

    def get_type(self):
        return 'Type2'

    def get_area(self):
        return 0

    def get_slot_total_height(self):
        return self.h0 + self.h1 + self.h2

    def get_conductor_area_width(self):
        return self.w2

    def get_conductor_area_height(self):
        return self.h2

    def get_coil_area_base_point(self, inner_radius):
        return inner_radius + self.h0 + self.h1

    def get_slot_opening_geometry(self, inner_radius):
        delta_5 = np.arctan2(-self.w0/2.0,inner_radius)
        delta_4 = np.arctan2(-self.w0/2.0,inner_radius + self.h0)
        #r_5 = np.sqrt(inner_radius**2 + (self.w0 / 2.0)**2)
        r_4 = np.sqrt((inner_radius + self.h0)**2 + (self.w0 / 2.0)**2)
        r_5 = inner_radius
        points = {
            '2': [inner_radius, 0, 0],
            '3': [inner_radius + self.h0, 0, 0],
            '4': [r_4*np.cos(delta_4), r_4*np.sin(delta_4) , 0],
            '5': [r_5*np.cos(delta_5), r_5*np.sin(delta_5) , 0]
        }
        lines = {
            '1': [2, 3],
            '2': [3, 4],
            '3': [4, 5],
            '4': [5, 2]
        }
        return points, lines


    def get_slot_wedge_geometry(self, inner_radius):
        delta_7 = np.arctan2(-self.w2/2.0,inner_radius + self.h0 + self.h1)
        delta_8 = np.arctan2(-self.w1/2.0,inner_radius + self.h0 + self.h1)
        r_7 = np.sqrt((inner_radius + self.h0 + self.h1)**2 + (self.w2 / 2.0)**2)
        r_8 = np.sqrt((inner_radius + self.h0 + self.h1)**2 + (self.w1 / 2.0)**2)
        points = {
            '6': [inner_radius + self.h0 + self.h1, 0, 0],
            '7': [r_7*np.cos(delta_7), r_7*np.sin(delta_7) , 0],
            '8': [r_8*np.cos(delta_8), r_8*np.sin(delta_8) , 0]
        }
        lines = {
            '5': [3, 6],
            '6': [6, 7],
            '7': [7, 8],
            '8': [8, 4],
            '-2': [0]
        }
        return points, lines


    def get_backiron_geometry(self, inner_radius, outer_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        delta_10 = np.arctan2(-self.w2 / 2.0, inner_radius + self.h0 + self.h1 + self.h2)
        r_10 = np.sqrt((inner_radius + self.h0 + self.h1 + self.h2) ** 2 + (self.w2 / 2.0) ** 2)
        points = {
            '9': [inner_radius + self.h0 + self.h1 + self.h2, 0, 0],
            '10': [r_10 * np.cos(delta_10), r_10* np.sin(delta_10), 0],
            '11': [outer_radius, 0, 0],
            '12': [outer_radius * np.cos( -slot_pitch/2.0 ), outer_radius * np.sin( -slot_pitch/2.0 ), 0],
            '13': [(inner_radius + self.h0 + self.h1 + self.h2) * np.cos( -slot_pitch/2.0 ),
                   (inner_radius + self.h0 + self.h1 + self.h2) * np.sin( -slot_pitch/2.0 ) , 0]
            }
        lines = {
            '9': [9, 11],
            '10': [11, 1, 12],
            '11': [12, 13],
            '12': [13, 10],
            '13': [10, 9]
        }
        return points, lines

    def get_tooth_geometry(self, inner_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        points = {
            '14': [(inner_radius + self.h0 + self.h1) * np.cos( -slot_pitch/2.0 ),
                   (inner_radius + self.h0 + self.h1) * np.sin( -slot_pitch/2.0 ) , 0]
        }
        lines = {
            '14': [7, 10],
            '-12': [0],
            '15': [13, 14],
            '16': [14, 8],
            '-7': [0]
        }
        return points, lines


    def get_coil_area_geometry(self, inner_radius):
        points = None
        lines = {
            '17': [6, 9],
            '-13': [0],
            '-14': [0],
            '-6': [0]
        }
        return points, lines

    def get_toothtip_geometry(self, inner_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        points = {
            '15': [inner_radius * np.cos( -slot_pitch/2.0 ), inner_radius * np.sin( -slot_pitch/2.0 ) , 0]
        }
        lines = {
            '18': [14, 15],
            '19': [15, 1, 5],
            '-3': [0],
            '-8': [0],
            '-16': [0]
        }
        return points, lines


    def get_stator_airgap_geometry(self, airgap_radius, slot_number):
        slot_pitch = 360 * DEG2RAD / slot_number
        points = {
            '16': [airgap_radius * np.cos( -slot_pitch/2.0 ), airgap_radius * np.sin( -slot_pitch/2.0 ) , 0],
            '17': [airgap_radius, 0, 0]
        }
        lines = {
            '20': [15, 16],
            '21': [16, 1, 17],
            '22': [17, 2],
            '-4': [0],
            '-19': [0]
        }
        return points, lines

    def get_stator_airgap_boundary(self):
        return {'21': [16, 1, 17]}

    def get_outer_stator_boundary(self):
        return [10]

    def get_master_boundary(self):
        return [11, 15, 18, 20]
