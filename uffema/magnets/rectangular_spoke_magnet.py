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

from uffema.magnets import Magnet


class RectangularSpokeMagnet(Magnet):
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def mag_angle(self):
        return self._mag_angle

    @mag_angle.setter
    def mag_angle(self, value):
        self._mag_angle = value

    @property
    def magnets_per_pole(self):
        return self._magnets_per_pole

    @magnets_per_pole.setter
    def magnets_per_pole(self, value):
        self._magnets_per_pole = value

    def get_type(self):
        return 'RectangularSpoke'

    def __init__(self, magnets_settings, magnetisation, material):
        Magnet.__init__(self, magnets_settings, "perpendicular", material)
        self.length = magnets_settings['Ml']
        self.width = magnets_settings['Mw']
        self.magnet_radius = magnets_settings['Mr']
        self.magnets_per_pole = 1
        self.mag_angle = [90]
        self.type = self.type + 'RectangularSpoke'

    def get_magnet_geometry(self):

        points = {
            '700': [self.magnet_radius, 0, 0],
            '701': [self.magnet_radius + self.length, 0, 0],
            '702': [self.magnet_radius + self.length, -0.5*self.width, 0],
            '703': [self.magnet_radius, -0.5*self.width, 0]
        }
        lines = {
            '700': [700, 701],
            '701': [701, 702],
            '702': [702, 703],
            '703': [703, 700]
        }
        return points, lines

