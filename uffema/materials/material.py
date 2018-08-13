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

import numpy as np


class Material:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def Br(self):
        return self._Br

    @Br.setter
    def Br(self, value):
        self._Br = value

    @property
    def mur(self):
        return self._mur

    @mur.setter
    def mur(self, value):
        self._mur = value

    @property
    def resistivity(self):
        return self._resistivity

    @resistivity.setter
    def resistivity(self, value):
        self._resistivity = value

    @property
    def BH(self):
        return self._BH

    @BH.setter
    def BH(self, value):
        self._BH = value

    def __init__(self, material_settings):
        self.name = material_settings.get('name', 'NoName')
        self.Br = material_settings.get('Br', None)
        self.mur = material_settings.get('mur', None)
        self.resistivity = material_settings.get('resistivity', 1.0)
        BH_list = material_settings.get('BHcurve', None)
        if BH_list is not None:
            Bs = [each['B'] for each in BH_list]
            Hs = [each['H'] for each in BH_list]
            self.BH = np.array([Bs , Hs])
        else:
            self.BH = None

    @staticmethod
    def create(material_settings):
        material_instance = Material(material_settings)
        return material_instance