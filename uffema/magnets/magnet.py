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

from uffema.materials import Material
from uffema.misc.constants import *


class Magnet(object):
    __metaclass__ = abc.ABCMeta

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    @property
    def magnetisation(self):
        return self._magnetisation

    @magnetisation.setter
    def magnetisation(self, value):
        self._magnetisation = value

    @abc.abstractproperty
    def type(self):
        return 'Should never see this'

    @type.setter
    def type(self, new_type):
        return

    def __init__(self, magnets_settings, magnetisation, material):
        self.material = material
        self.magnetisation = magnetisation
        self.type = 'Magnet::'

    @staticmethod
    def create(magnets_settings, magnet_type='Arc', magnetisation='Paralell', material=None ):
        if magnet_type == 'Arc':
            from uffema.magnets import ArcMagnet
            magnet_instance = ArcMagnet(magnets_settings, magnetisation, material)
        elif magnet_type == 'Rectangular':
            from uffema.magnets import RectangularMagnet
            magnet_instance = RectangularMagnet(magnets_settings, magnetisation, material)
        else:
            from uffema.magnets import ArcMagnet
            magnet_instance = ArcMagnet(magnets_settings, magnetisation, material)
        return magnet_instance

