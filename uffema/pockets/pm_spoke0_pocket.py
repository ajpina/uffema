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


class PMSpoke0Pocket(PMPocket):

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'SPOKE0'

    def __init__(self, pockets_settings, magnets_settings, magnet_type='rectangular'):
        PMPocket.__init__(self, pockets_settings)
        self.pocket_width1 = pockets_settings['Pw1']
        self.pocket_width2 = pockets_settings['Pw2']
        self.bridge_length = pockets_settings['Bl']
        self.hub_radius = pockets_settings['Hr']
        if magnet_type == 'spoke':
            self.magnet_length = magnets_settings['Ml']
            self.magnet_width = magnets_settings['Mw']
            self.magnet_radius = magnets_settings['Mr']
        self.type = self.type + 'SPOKE0'

    def get_pocket_geometry(self, outer_radius):
        points = []
        lines = []
        points.append({
            '900': [self.hub_radius, 0, 0],
            '901': [self.hub_radius, -(0.5 * self.pocket_width1), 0]
        })
        lines.append({
            '900': [900, 700],
            '-703': [0],
            '901': [703, 901],
            '902': [901, 900]
        })
        points.append({
            '902': [outer_radius - self.bridge_length, 0, 0],
            '903': [outer_radius - self.bridge_length, -(0.5 * self.pocket_width2), 0]
        })
        lines.append({
            '903': [701, 902],
            '904': [902, 903],
            '905': [903, 702],
            '-701': [0]
        })
        return points, lines

