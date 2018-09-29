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


class PMUPocket(PMPocket):

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'U'

    def __init__(self, pockets_settings, magnets_settings, magnet_type='rectangular'):
        PMPocket.__init__(self, pockets_settings)
        self.extension1 = pockets_settings['Pe1']
        self.extension2 = pockets_settings['Pe2']
        self.length = pockets_settings['Pl']
        self.flux_barrier_length = pockets_settings['FBl']
        self.bridge_length = pockets_settings['Bl']
        self.pocket_angle = pockets_settings['Ua'] * DEG2RAD
        if magnet_type == 'rectangular':
            self.magnet_length = magnets_settings['Ml']
            self.magnet_width = magnets_settings['Mw']
            self.magnet_radius = magnets_settings['Mr']
        self.type = self.type + 'U'

    def get_pocket_geometry(self, outer_radius):
        points = []
        lines = []
        radius_at_bridge = np.sqrt((outer_radius - self.bridge_length)**2 + (0.5*self.flux_barrier_length)**2)
        delta_beta_at_bridge = np.arctan2(self.flux_barrier_length, 2 * (outer_radius - self.bridge_length))
        points.append({
            '900': [self.magnet_radius + 0.5*self.magnet_length, -0.5*self.magnet_width, 0],
            '901': [self.magnet_radius + 0.5 * self.length, -(0.5 * self.magnet_width + self.extension1), 0],
            '902': [radius_at_bridge * np.cos(-0.5*self.pocket_angle + delta_beta_at_bridge),
                   radius_at_bridge * np.sin(-0.5*self.pocket_angle + delta_beta_at_bridge), 0],
            '903': [radius_at_bridge * np.cos(-0.5 * self.pocket_angle - delta_beta_at_bridge),
                   radius_at_bridge * np.sin(-0.5 * self.pocket_angle - delta_beta_at_bridge), 0],
            '904': [self.magnet_radius - 0.5 * self.length, -(0.5 * self.magnet_width + self.extension1 + self.extension2), 0],
            '905': [self.magnet_radius - 0.5 * self.length, -(0.5 * self.magnet_width + self.extension1), 0],
            '906': [self.magnet_radius - 0.5*self.magnet_length, -0.5*self.magnet_width, 0]
        })
        lines.append({
            '900': [900, 901],
            '901': [901, 902],
            '902': [902, 903],
            '903': [903, 904],
            '904': [904, 905],
            '905': [905, 906],
            '906': [906, 900]
        })
        return points, lines

