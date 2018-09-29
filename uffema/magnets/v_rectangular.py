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

from uffema.magnets import Magnet
from uffema.misc.constants import *


class VRectangularMagnet(Magnet):
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
        return 'VRectangular'

    def __init__(self, magnets_settings, magnetisation, material):
        Magnet.__init__(self, magnets_settings, "parallel", material)
        self.length = magnets_settings['Ml']
        self.width = magnets_settings['Mw']
        self.magnet_radius = magnets_settings['Mr']
        self.magnet_v_angle = magnets_settings['MVa']
        self.magnets_per_pole = 2
        self.mag_angle = []
        self.slit_gap = None
        self.inner_slit_angle_0 = None
        self.inner_slit_length = None
        self.inner_slit_width = None
        self.pocket_extension = None
        self.type = self.type + 'VRectangular'

    def add_parameters(self, rotor_settings):
        self.pocket_extension = rotor_settings['pockets']['dimension'][0]['Pe']
        self.slit_gap = rotor_settings['pockets']['dimension'][0]['Sg']
        self.inner_slit_angle_0 = rotor_settings['pockets']['dimension'][0]['iSa0']
        self.inner_slit_length = rotor_settings['pockets']['dimension'][0]['iSl']
        self.inner_slit_width = rotor_settings['pockets']['dimension'][0]['iSw']
        self._calc_mag_angle()

    def _calc_mag_angle(self):
        beta_m1 = - self.magnet_v_angle / 2.0
        angle = beta_m1 + 90.0
        self.mag_angle.append(angle)
        self.mag_angle.append(-angle)

    def get_magnet_geometry(self):
        points = []
        lines = []
        beta_m1 = - self.magnet_v_angle / 2.0
        r_900 = np.sqrt((self.magnet_radius) ** 2 + (0.5 * self.slit_gap) ** 2)
        angle_900 = -np.arctan2(self.slit_gap, 2 * (self.magnet_radius))
        Ix = r_900 * np.cos(angle_900)
        Iy = r_900 * np.sin(angle_900)
        Bx = Ix + (self.inner_slit_width + self.pocket_extension) * np.sin((90 + beta_m1) * DEG2RAD)
        By = Iy - (self.inner_slit_width + self.pocket_extension) * np.cos((90 + beta_m1) * DEG2RAD)
        x700 = Bx + 0.5 * self.length * np.cos((90 + beta_m1) * DEG2RAD)
        y700 = By + 0.5 * self.length * np.sin((90 + beta_m1) * DEG2RAD)
        x703 = Bx - 0.5 * self.length * np.cos((90 + beta_m1) * DEG2RAD)
        y703 = By - 0.5 * self.length * np.sin((90 + beta_m1) * DEG2RAD)
        x701 = x700 + self.width * np.cos(beta_m1 * DEG2RAD)
        y701 = y700 + self.width * np.sin(beta_m1 * DEG2RAD)
        x702 = x703 + self.width * np.cos(beta_m1 * DEG2RAD)
        y702 = y703 + self.width * np.sin(beta_m1 * DEG2RAD)

        points.append({
            '700': [x700, y700, 0],
            '701': [x701, y701, 0],
            '702': [x702, y702, 0],
            '703': [x703, y703, 0]
        })
        lines.append({
            '700': [700, 701],
            '701': [701, 702],
            '702': [702, 703],
            '703': [703, 700]
        })
        return points[0], lines[0]

