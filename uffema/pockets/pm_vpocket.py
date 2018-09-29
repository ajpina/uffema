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

from uffema.pockets import PMPocket
from uffema.misc.constants import *


class PMVPocket(PMPocket):

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'V'

    def __init__(self, pockets_settings, magnets_settings, magnet_type='rectangular'):
        PMPocket.__init__(self, pockets_settings)
        self.extension = pockets_settings['Pe']
        self.slit_gap = pockets_settings['Sg']
        self.inner_slit_angle_0 = pockets_settings['iSa0']
        self.inner_slit_angle_1 = pockets_settings['iSa1']
        self.inner_slit_length = pockets_settings['iSl']
        self.inner_slit_width = pockets_settings['iSw']
        self.outer_slit_length = pockets_settings['oSl']
        self.outer_slit_width = pockets_settings['oSw']
        self.flux_barrier_length = pockets_settings['Bl']
        self.flux_barrier_width = pockets_settings['Bw']
        self.bridge_length = pockets_settings['Bl']
        self.pocket_angle = pockets_settings['Va']
        self.magnet_length = None
        self.magnet_width = None
        self.magnet_radius = None
        self.magnet_v_angle = None
        self.rotor_outer_radius = None
        self.type = self.type + 'V'

    def add_parameters(self, rotor_settings):
        self.magnet_length = rotor_settings['magnets']['dimension'][0]['Ml']
        self.magnet_width = rotor_settings['magnets']['dimension'][0]['Mw']
        self.magnet_radius = rotor_settings['magnets']['dimension'][0]['Mr']
        self.magnet_v_angle = rotor_settings['magnets']['dimension'][0]['MVa']
        self.rotor_outer_radius = rotor_settings['oRr']

    def get_pocket_geometry(self, outer_radius):
        points = []
        lines = []
        beta_m1 = - self.magnet_v_angle / 2.0
        m1 = np.tan(beta_m1 * DEG2RAD)
        m2 = np.tan(-(180.0 - beta_m1 - self.inner_slit_angle_0) * DEG2RAD)
        m3 = np.tan( - (self.inner_slit_angle_1 - beta_m1) * DEG2RAD)
        r_900 = np.sqrt((self.magnet_radius) ** 2 + (0.5 * self.slit_gap) ** 2)
        angle_900 = -np.arctan2(self.slit_gap, 2 * (self.magnet_radius))
        Ix = r_900 * np.cos(angle_900)
        Iy = r_900 * np.sin(angle_900)
        Ax = Ix + self.inner_slit_width * np.sin((90 + beta_m1)*DEG2RAD)
        Ay = Iy - self.inner_slit_width * np.cos((90 + beta_m1)*DEG2RAD)
        x902 = Ax + 0.5 * self.inner_slit_length * np.cos((90 + beta_m1) * DEG2RAD)
        y902 = Ay + 0.5 * self.inner_slit_length * np.sin((90 + beta_m1) * DEG2RAD)
        x903 = Ax - 0.5 * self.inner_slit_length * np.cos((90 + beta_m1) * DEG2RAD)
        y903 = Ay - 0.5 * self.inner_slit_length * np.sin((90 + beta_m1) * DEG2RAD)
        y901 = (-m1*Iy + m1*m3*Ix - m1*m3*x902 + m3*y902)/(m3 - m1)
        x901 = (y901 - Iy)/m3 + Ix
        y904 = (-m1*Iy + m1*m2*Ix - m1*m2*x903 + m2*y903)/(m2 - m1)
        x904 = (y904 - Iy)/m2 + Ix
        Dx = Ix + (self.inner_slit_width+2.0*self.extension+self.magnet_width) * np.sin((90 + beta_m1) * DEG2RAD)
        Dy = Iy - (self.inner_slit_width+2.9*self.extension+self.magnet_width) * np.cos((90 + beta_m1) * DEG2RAD)
        x905 = Dx + 0.5 * self.outer_slit_length * np.cos((90 + beta_m1) * DEG2RAD)
        y905 = Dy + 0.5 * self.outer_slit_length * np.sin((90 + beta_m1) * DEG2RAD)
        x910 = Dx - 0.5 * self.outer_slit_length * np.cos((90 + beta_m1) * DEG2RAD)
        y910 = Dy - 0.5 * self.outer_slit_length * np.sin((90 + beta_m1) * DEG2RAD)
        x906 = x905 + self.outer_slit_width * np.cos((beta_m1) * DEG2RAD)
        y906 = y905 + self.outer_slit_width * np.sin((beta_m1) * DEG2RAD)
        x909 = x910 + self.outer_slit_width * np.cos((beta_m1) * DEG2RAD)
        y909 = y910 + self.outer_slit_width * np.sin((beta_m1) * DEG2RAD)

        r_907 = np.sqrt((self.rotor_outer_radius - self.bridge_length) ** 2 + (0.5*self.flux_barrier_length) ** 2)
        angle_mid_bridge = np.arctan2(self.flux_barrier_length, 2*(self.rotor_outer_radius - self.bridge_length))
        angle_907 = -0.5 * self.pocket_angle * DEG2RAD + angle_mid_bridge
        angle_908 = -0.5 * self.pocket_angle * DEG2RAD - angle_mid_bridge


        points.append({
            '900': [r_900 * np.cos(angle_900), r_900 * np.sin(angle_900), 0],
            '901': [x901, y901, 0],
            '902': [x902, y902, 0],
            '903': [x903, y903, 0],
            '904': [x904, y904, 0]
        })
        lines.append({
            '900': [900, 901],
            '901': [901, 902],
            '902': [902, 700],
            '-703': [0],
            '903': [703, 903],
            '904': [903, 904],
            '905': [904, 900]
        })
        points.append({
            '905': [x905, y905, 0],
            '906': [x906, y906, 0],
            '907': [r_907 * np.cos(angle_907), r_907 * np.sin(angle_907), 0],
            '908': [r_907 * np.cos(angle_908), r_907 * np.sin(angle_908), 0],
            '909': [x909, y909, 0],
            '910': [x910, y910, 0]
        })
        lines.append({
            '906': [701, 905],
            '907': [905, 906],
            '908': [906, 907],
            '909': [907, 908],
            '910': [908, 909],
            '911': [909, 910],
            '912': [910, 702],
            '-701': [0]
        })
        return points, lines

