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

import abc

class Rotor(object):
    __metaclass__ = abc.ABCMeta

    @property
    def inner_radius(self):
        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, value):
        self._inner_radius = value

    @property
    def outer_radius(self):
        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, value):
        self._outer_radius = value

    @property
    def stack_length(self):
        return self._stack_length

    @stack_length.setter
    def stack_length(self, value):
        self._stack_length = value

    @property
    def pp(self):
        return self._pp

    @pp.setter
    def pp(self, value):
        self._pp = value

    @abc.abstractproperty
    def type(self):
        return 'Should never see this'

    @type.setter
    def type(self, new_type):
        return

    def get_type(self):
        return 'Rotor'

    def __init__(self, rotor_settings):
        self.pp = rotor_settings['pp']
        self.inner_radius = rotor_settings['iRr']
        self.outer_radius = rotor_settings['oRr']
        self.stack_length = rotor_settings['Rl']
        self.type = 'Rotor::'

    @staticmethod
    def create(rotor_settings):
        stator_type = rotor_settings['type']
        if stator_type == 'standardinner':
            from uffema.rotors import PMStandardInnerRotor
            rotor_instance = PMStandardInnerRotor(rotor_settings)
        elif stator_type == 'standardouter':
            from uffema.rotors import PMStandardInnerRotor
            rotor_instance = PMStandardInnerRotor(rotor_settings)
        else:
            from uffema.rotors import PMStandardInnerRotor
            rotor_instance = PMStandardInnerRotor(rotor_settings)
        return rotor_instance
