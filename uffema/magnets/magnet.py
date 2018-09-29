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

from abc import ABCMeta, abstractmethod

from uffema.materials import Material
from uffema.misc.constants import *


class Magnet(metaclass=ABCMeta):

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

    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Magnet'

    def __init__(self, magnets_settings, magnetisation, material_settings):
        self.material = Material.create(material_settings)
        self.magnetisation = magnetisation
        self.type = 'Magnet::'

    @staticmethod
    def create(magnets_settings, magnet_type='arc', magnetisation='paralell', material_settings=None ):
        if magnet_type == 'arc':
            from uffema.magnets import ArcMagnet
            magnet_instance = ArcMagnet(magnets_settings, magnetisation, material_settings)
        elif magnet_type == 'rectangular':
            from uffema.magnets import RectangularMagnet
            magnet_instance = RectangularMagnet(magnets_settings, magnetisation, material_settings)
        elif magnet_type == 'breadloaf':
            from uffema.magnets import BreadLoafMagnet
            magnet_instance = BreadLoafMagnet(magnets_settings, magnetisation, material_settings)
        elif magnet_type == 'v':
            from uffema.magnets import VRectangularMagnet
            magnet_instance = VRectangularMagnet(magnets_settings, magnetisation, material_settings)
        else:
            from uffema.magnets import ArcMagnet
            magnet_instance = ArcMagnet(magnets_settings, magnetisation, material_settings)
        return magnet_instance

