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
from uffema.misc.constants import *


class BreadLoafMagnet(Magnet):
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
    def pole_shaping(self):
        return self._pole_shaping

    @pole_shaping.setter
    def pole_shaping(self, value):
        self._pole_shaping = value

    @property
    def type(self):
        return self._type

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

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'BreadLoaf'

    def __init__(self, magnets_settings, magnetisation, material_settings):
        Magnet.__init__(self, magnets_settings, magnetisation, material_settings)
        self.length = magnets_settings['Ml']
        self.width = magnets_settings['Mw']
        self.pole_shaping = magnets_settings['Mps']
        self.magnet_radius = magnets_settings['Mr']
        self.outer_radius = self.magnet_radius + self.length
        self.deviation = magnets_settings['delta']*DEG2RAD
        self.magnets_per_pole = 1
        self.mag_angle = [0]
        self.type = self.type + 'BreadLoaf'


    def get_magnet_geometry(self, pp):

        beta = PI / pp
        r_701 = self.magnet_radius + self.length
        r_703 = np.sqrt( (self.magnet_radius + self.length * self.pole_shaping)**2 + (self.width/2.0)**2 )
        r_704 = np.sqrt( (self.magnet_radius)**2 + (self.width/2.0)**2 )
        alpha_703 = np.arctan2(-self.width/2.0, self.magnet_radius + self.length * self.pole_shaping)
        alpha_704 = np.arctan2(-self.width / 2.0, self.magnet_radius )
        a_delta = self.width / 2.0
        b_delta = self.length * (1 - self.pole_shaping)
        c_delta = np.sqrt(a_delta ** 2.0 + b_delta ** 2.0)
        beta_delta = np.arctan2(a_delta, b_delta)
        alpha_delta = PI - 2 * beta_delta
        Rps = c_delta * np.sin(beta_delta) / np.sin(alpha_delta)

        points = {
            '700': [self.magnet_radius, 0, 0],
            '701': [r_701, 0, 0],
            '702': [r_701 - Rps, 0, 0],
            '703': [r_703 * np.cos(alpha_703), r_703 * np.sin(alpha_703), 0],
            '704': [r_704 * np.cos(alpha_704), r_704 * np.sin(alpha_704), 0]
        }
        lines = {
            '700': [700, 701],
            '701': [701, 702, 703],
            '702': [703, 704],
            '703': [704, 700]
        }
        return points, lines

