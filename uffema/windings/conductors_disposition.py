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


class ConductorsArea:
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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return self._type

    def __init__(self, num_layers, layers_type, cond_type, cond_diam, cond_height, cond_width):
        if num_layers == 1:
            self.type = 'OneLayer'
        elif num_layers == 2:
            if layers_type == 'sidebyside':
                self.type = 'DualLayer_SideBySide'
            elif layers_type == 'topbottom':
                self.type = 'DualLayer_TopBottom'
            elif layers_type == 'hairpin':
                self.type = 'HairPin_2Cond'
            else:
                self.type = 'Unknown'
        elif num_layers == 3:
            self.type = 'TriLayer'
        elif num_layers == 4:
            if layers_type == 'sidebyside':
                self.type = 'FourLayer_SideBySide'
            elif layers_type == 'topbottom':
                self.type = 'FourLayer_TopBottom'
            elif layers_type == 'hairpin':
                self.type = 'HairPin_4Cond'
            else:
                self.type = 'Unknown'
        elif num_layers == 6:
            if layers_type == 'hairpin':
                self.type = 'HairPin_6Cond'
            else:
                self.type = 'Unknown'
        else:
            self.type = 'Unknown'

        self.conductor_type = cond_type
        self.conductor_diameter = cond_diam
        self.conductor_height = cond_height
        self.conductor_width = cond_width



    def get_conductors_geometry(self, slot_width, slot_height, coil_area_base_point):
        """Get Geometry

        Put some description

        Args:
            m:         Number of phases
            Ns:        Slot number
            psi:       Spatial position

        Returns:
            td:        something
        """
        geometry_list = []
        if self.type == 'OneLayer':
            points = {
                '300': [coil_area_base_point + slot_height / 4.0, 0, 0],
                '301': [coil_area_base_point + 3 * slot_height / 4.0, 0, 0],
                '302': [coil_area_base_point + 3 * slot_height / 4.0, -0.7 * slot_width / 2.0, 0],
                '303': [coil_area_base_point + slot_height / 4.0, -0.7 * slot_width / 2.0, 0]
            }
            lines = {
                '300': [300, 301],
                '301': [301, 302],
                '302': [302, 303],
                '303': [303, 300]
            }
            geometry_list.append((points, lines))
        elif self.type == 'DualLayer_SideBySide':
            points = {
                '300': [coil_area_base_point + slot_height / 4.0, -0.1 * slot_width / 2.0, 0],
                '301': [coil_area_base_point + 3 * slot_height / 4.0, -0.1 * slot_width / 2.0, 0],
                '302': [coil_area_base_point + 3 * slot_height / 4.0, -0.7 * slot_width / 2.0, 0],
                '303': [coil_area_base_point + slot_height / 4.0, -0.7 * slot_width / 2.0, 0]
            }
            lines = {
                '300': [300, 301],
                '301': [301, 302],
                '302': [302, 303],
                '303': [303, 300]
            }
            geometry_list.append((points, lines))
        elif self.type == 'DualLayer_TopBottom':
            points1 = {
                '300': [coil_area_base_point + slot_height / 5.0, 0, 0],
                '301': [coil_area_base_point + slot_height / 2.0 - slot_height / 20.0, 0, 0],
                '302': [coil_area_base_point + slot_height / 2.0 - slot_height / 20.0, -0.6 * slot_width / 2.0, 0],
                '303': [coil_area_base_point + slot_height / 5.0, -0.6 * slot_width / 2.0, 0]
            }
            lines1 = {
                '300': [300, 301],
                '301': [301, 302],
                '302': [302, 303],
                '303': [303, 300]
            }
            points2 = {
                '304': [coil_area_base_point + slot_height / 2.0 + slot_height / 20.0, 0, 0],
                '305': [coil_area_base_point + 4 * slot_height / 5.0, 0, 0],
                '306': [coil_area_base_point + 4 * slot_height / 5.0, -0.6 * slot_width / 2.0, 0],
                '307': [coil_area_base_point + slot_height / 2.0 + slot_height / 20.0, -0.6 * slot_width / 2.0, 0]
            }
            lines2 = {
                '304': [304, 305],
                '305': [305, 306],
                '306': [306, 307],
                '307': [307, 304]
            }
            geometry_list.append((points1, lines1))
            geometry_list.append((points2, lines2))
        elif self.type == 'HairPin_2Cond':
            center_x_cond_1 = coil_area_base_point + slot_height / 4.0
            center_x_cond_2 = coil_area_base_point + 3 * slot_height / 4.0
            points1 = {
                '300': [center_x_cond_1 - self.conductor_height / 2.0, 0, 0],
                '301': [center_x_cond_1 + self.conductor_height / 2.0, 0, 0],
                '302': [center_x_cond_1 + self.conductor_height / 2.0, -self.conductor_width / 2.0, 0],
                '303': [center_x_cond_1 - self.conductor_height / 2.0, -self.conductor_width / 2.0, 0]
            }
            lines1 = {
                '300': [300, 301],
                '301': [301, 302],
                '302': [302, 303],
                '303': [303, 300]
            }
            points2 = {
                '304': [center_x_cond_2 - self.conductor_height / 2.0, 0, 0],
                '305': [center_x_cond_2 + self.conductor_height / 2.0, 0, 0],
                '306': [center_x_cond_2 + self.conductor_height / 2.0, -self.conductor_width / 2.0, 0],
                '307': [center_x_cond_2 - self.conductor_height / 2.0, -self.conductor_width / 2.0, 0]
            }
            lines2 = {
                '304': [304, 305],
                '305': [305, 306],
                '306': [306, 307],
                '307': [307, 304]
            }
            geometry_list.append((points1, lines1))
            geometry_list.append((points2, lines2))
        else:
            return None

        return geometry_list

    def get_air_around_conductors(self, coil_area_points, coil_area_lines):
        points = None
        keys = list(coil_area_lines.keys())
        values = coil_area_lines[keys[0]]
        pWedge = values[0]
        pBackIron = values[1]
        if self.type == 'OneLayer':
            lines = {
                '200': [int(pWedge), 300],
                '201': [300, 301],
                '202': [301, int(pBackIron)]
            }
            skip = True
            for key, value in coil_area_lines.items():
                if skip:
                    skip = False
                else:
                    lines[key] = value
        elif self.type == 'DualLayer_SideBySide':
            lines = coil_area_lines
            skip = True
            for key, value in coil_area_lines.items():
                if skip:
                    skip = False
                else:
                    lines[key] = value
        elif self.type == 'DualLayer_TopBottom':
            lines = {
                '200': [int(pWedge), 300],
                '201': [300, 301],
                '202': [301, 304],
                '203': [304, 305],
                '204': [305, int(pBackIron)]
            }
            skip = True
            for key, value in coil_area_lines.items():
                if skip:
                    skip = False
                else:
                    lines[key] = value
        elif self.type == 'HairPin_2Cond':
            lines = {
                '200': [int(pWedge), 300],
                '201': [300, 301],
                '202': [301, 304],
                '203': [304, 305],
                '204': [305, int(pBackIron)]
            }
            skip = True
            for key, value in coil_area_lines.items():
                if skip:
                    skip = False
                else:
                    lines[key] = value
        else:
            lines = None
        return points, lines

