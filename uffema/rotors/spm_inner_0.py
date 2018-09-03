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


class SPM0(Rotor):

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
        return 'SPM0'

    def __init__(self, rotor_settings):
        super(SPM0, self).__init__(rotor_settings)
        self.magnets = []
        for i, magnet_settings in enumerate(rotor_settings['magnets']['dimension']):
            self.magnets.insert(i, Magnet.create(magnet_settings, rotor_settings['magnets']['type'],
                                                 rotor_settings['magnets']['magnetisation'],
                                                 rotor_settings['magnets']['material']))

        self.pockets = []
        if 'pockets' in rotor_settings:
            for i, pocket_settings in enumerate(rotor_settings['pockets']['dimension']):
                self.pockets.insert(i, PMPocket.create(pocket_settings, rotor_settings['pockets']['type'],
                                                       rotor_settings['magnets']['dimension'][0],
                                                       rotor_settings['magnets']['type'] ))

        self.initial_position = rotor_settings['init_pos'] * DEG2RAD
        self.type = self.type + 'SPM0'


    def get_shaft_geometry(self):
        pole_pitch =  PI / self.pp
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
        return self.magnets[0].get_magnet_geometry(self.pp)

    def get_core_geometry(self):
        # Needs to be modified if more than 4 points are used by magnets
        pole_pitch = PI / self.pp
        points = {
            '502': [self.outer_radius * np.cos (-pole_pitch/2.0), self.outer_radius * np.sin(-pole_pitch/2.0), 0]
        }
        lines = {
            '503': [500, 700],
            '-703': [0],
            '504': [704, 1, 502],
            '505': [502, 501],
            '-501': [0]
        }
        return points, lines

    def get_pocket_geometry(self):
        pass

    def get_rotor_airgap_geometry(self, airgap_radius):
        pole_pitch = PI / self.pp
        points = {
            '503': [airgap_radius, 0, 0],
            '504': [airgap_radius * np.cos(-pole_pitch / 2.0), airgap_radius * np.sin(-pole_pitch / 2.0), 0]
        }
        lines = {
            '506': [701, 503],
            '507': [503, 1, 504],
            '508': [504, 502],
            '-504': [0],
            '-702': [0],
            '-701': [0]
        }
        return points, lines


    def get_master_boundary(self):
        return [508, 505, 502]

    def get_sliding_boundary(self):
        return [507]