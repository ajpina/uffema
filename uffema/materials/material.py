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

class Material:
    def __init__(self, material_settings):
        self.Br = material_settings['Br']
        self.mur = material_settings['mur']
        self.resistivity = material_settings['resistivity']
        self.BH = material_settings['BHcurve']

    @staticmethod
    def create(material_settings):
        material_instance = Material(material_settings)
        return material_instance