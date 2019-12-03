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

from uffema.rotors import Rotor
from uffema.misc.constants import *

from uffema.magnets import Magnet
from uffema.pockets import PMPocket


class SPOKE0(Rotor):

    @property
    def magnets(self):
        return self._magnets

    @magnets.setter
    def magnets(self, value):
        self._magnets = value

    @property
    def pockets(self):
        return self._pockets

    @pockets.setter
    def pockets(self, value):
        self._pockets = value

    @property
    def initial_position(self):
        return self._initial_position

    @initial_position.setter
    def initial_position(self, value):
        self._initial_position = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def get_type(self):
        return 'SPOKE0'

    def __init__(self, rotor_settings):
        Rotor.__init__(self, rotor_settings, 'inner')
        self.magnets = []
        for i, magnet_settings in enumerate(rotor_settings['magnets']['dimension']):
            self.magnets.insert(i, Magnet.create(magnet_settings, rotor_settings['magnets']['type'],
                                                 rotor_settings['magnets']['magnetisation'],
                                                 rotor_settings['magnets']['material'],'inner'))
        self.pockets = []
        if 'pockets' in rotor_settings:
            for i, pocket_settings in enumerate(rotor_settings['pockets']['dimension']):
                self.pockets.insert(i, PMPocket.create(pocket_settings, rotor_settings['pockets']['type'], magnet_settings, rotor_settings['magnets']['type']))

        self.initial_position = rotor_settings['init_pos'] * DEG2RAD
        self.type = self.type + 'SPOKE0'


    def get_shaft_geometry(self):
        pole_pitch = PI / self.pp
        points = {
            '1': [0, 0, 0],
            '500': [self.inner_radius, 0, 0],
            '501': [self.inner_radius * np.cos (-pole_pitch/2.0), self.inner_radius * np.sin(-pole_pitch/2.0), 0]
        }
        lines = {
            '500': [1, 500],
            '501': [500, 1, 501],
            '502': [501, 1]
        }
        return points, lines

    def get_magnet_geometry(self):
        return self.magnets[0].get_magnet_geometry()

    def get_core_geometry(self):
        magnet_points, magnet_lines = self.magnets[0].get_magnet_geometry()
        mkeys = list(magnet_points.keys())
        #p700 = mkeys[0]
        #p701 = mkeys[1]
        pocket_points, pocket_lines = self.pockets[0].get_pocket_geometry(self.outer_radius)
        pkeys0 = list(pocket_points[0].keys())
        #p900 = pkeys0[0]
        #p903 = pkeys0[3]
        pkeys1 = list(pocket_points[1].keys())
        #p905 = pkeys1[1]
        pole_pitch = PI / self.pp
        points = {
            '502': [self.outer_radius, 0, 0],
            '503': [self.outer_radius * np.cos (-pole_pitch/2.0), self.outer_radius * np.sin(-pole_pitch/2.0), 0]
        }
        lines = {
            '503': [500, 900],
            '-902': [0],
            '-901': [0],
            '-702': [0],
            '-905': [0],
            '-904': [0],
            '504': [902, 502],
            '505': [502, 1, 503],
            '506': [503, 501],
            '-501': [0]
        }

        return points, lines

    def get_pocket_geometry(self):
        return self.pockets[0].get_pocket_geometry(self.outer_radius)

    def get_rotor_airgap_geometry(self, airgap_radius):
        pole_pitch = PI / self.pp
        points = {
            '504': [airgap_radius, 0, 0],
            '505': [airgap_radius * np.cos(-pole_pitch / 2.0), airgap_radius * np.sin(-pole_pitch / 2.0), 0]
        }
        lines = {
            '507': [502, 504],
            '508': [504, 1, 505],
            '509': [505, 503],
            '-505': [0]
        }
        return points, lines


    def get_master_boundary(self):
        return [509, 506, 502]

    def get_sliding_boundary(self):
        return [508]