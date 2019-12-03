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
    Class for standard inner stator
"""

# ==========================================================================
# Program:   standard_inner.py
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

from uffema.stators import Stator
from uffema.misc.constants import *


class StandardInnerStator(Stator):
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'StandardInner'

    def __init__(self, stator_settings):
        super(StandardInnerStator, self).__init__(stator_settings)
        self.type = self.type + 'StandardInner'
        self.sliding_airgap_arc = []
        self.airgap_arc = []

    def get_slot_opening_geometry(self):
        return self.slots[0].get_slot_opening_geometry(self.outer_radius)

    def get_slot_wedge_geometry(self):
        return self.slots[0].get_slot_wedge_geometry(self.outer_radius)

    def get_conductors_geometry(self):
        w = self.slots[0].get_conductor_area_width()
        h = self.slots[0].get_conductor_area_height()
        p = self.slots[0].get_coil_area_base_point(self.outer_radius)
        return self.winding.get_conductors_geometry(w, h, p)

    def get_coil_area_geometry(self):
        points, lines = self.slots[0].get_coil_area_geometry(self.outer_radius)
        return self.winding.get_air_around_conductors(points, lines)

    def get_backiron_geometry(self):
        return self.slots[0].get_backiron_geometry(self.inner_radius, self.outer_radius, self.slots_number)

    def get_tooth_geometry(self):
        return self.slots[0].get_tooth_geometry(self.outer_radius, self.slots_number)

    def get_toothtip_geometry(self):
        return self.slots[0].get_toothtip_geometry(self.outer_radius, self.slots_number)

    def get_stator_airgap_geometry(self, airgap_radius):
        return self.slots[0].get_stator_airgap_geometry(airgap_radius, self.slots_number)

    def get_stator_airgap_boundary(self):
        line = self.slots[0].get_stator_airgap_boundary()
        line_number = list(line.keys())
        line_points = list(line.values())
        return line_number

    def get_outer_stator_boundary(self):
        return self.slots[0].get_outer_stator_boundary()

    def get_master_boundary(self):
        master_boundary = self.slots[0].get_master_boundary()
        master_boundary.append(int(self.sliding_airgap_arc[0])-1)
        return master_boundary

    def get_sliding_airgap_geometry(self, airgap_radius):
        slot_pitch = 360 * DEG2RAD / self.slots_number
        line = self.slots[0].get_stator_airgap_boundary()
        line_number = list(line.keys())
        line_points = list(line.values())
        p0 = line_points[0][0]
        p1 = line_points[0][2]
        points = {
            str(p1+1): [airgap_radius * np.cos(-slot_pitch / 2.0), airgap_radius * np.sin(-slot_pitch / 2.0), 0],
            str(p1+2): [airgap_radius, 0, 0]
        }
        lines = {
            str(int(line_number[0])+2): [p0, p1+1],
            str(int(line_number[0])+3): [p1+1, 1, p1+2],
            str(int(line_number[0])+4): [p1+2, p1],
            str(-int(line_number[0])): [0]
        }
        self.airgap_arc.append(str(int(line_number[0])))
        self.sliding_airgap_arc.append(str(int(line_number[0])+3))
        return points, lines

    def get_sliding_boundary(self):
        return self.sliding_airgap_arc

    def get_airgap_arc(self):
        return self.airgap_arc

    def __str__(self):
        return Stator.__str__(self)