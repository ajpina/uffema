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


class PMStandardInnerRotor(Rotor):

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

    def __init__(self, rotor_settings):
        super(PMStandardInnerRotor, self).__init__(rotor_settings)
        self.magnets = []
        for i, magnet_settings in  enumerate(rotor_settings['magnets']['dimension']):
            self.magnets.insert(i, Magnet.create(magnet_settings, rotor_settings['magnets']['type'],
                                                 rotor_settings['magnets']['magnetisation'],
                                                 rotor_settings['magnets']['material']))
        self.pockets = []
        if 'pockets' in rotor_settings:
            for i, pocket_settings in  enumerate(rotor_settings['pockets']['dimension']):
                self.pockets.insert(i, PMPocket.create(pocket_settings, rotor_settings['pockets']['type']))

        self.initial_position = rotor_settings['init_pos'] * DEG2RAD
        self.type = self.type + 'PMStandardInner'

