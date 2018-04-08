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

from uffema.magnets import Magnet
from uffema.misc.constants import *


class ArcMagnet(Magnet):
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def pole_shaping(self):
        return self._pole_shaping

    @pole_shaping.setter
    def pole_shaping(self, value):
        self._pole_shaping = value

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
    def inner_arc_angle(self):
        return self._inner_arc_angle

    @inner_arc_angle.setter
    def inner_arc_angle(self, value):
        self._inner_arc_angle = value

    @property
    def outer_arc_angle(self):
        return self._outer_arc_angle

    @outer_arc_angle.setter
    def outer_arc_angle(self, value):
        self._outer_arc_angle = value

    @property
    def mean_arc_angle(self):
        return self._mean_arc_angle

    @mean_arc_angle.setter
    def mean_arc_angle(self, value):
        self._mean_arc_angle = value

    @property
    def deviation(self):
        return self._deviation

    @deviation.setter
    def deviation(self, value):
        self._deviation = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def __init__(self, magnets_settings, magnetisation, material):
        super(ArcMagnet, self).__init__(magnets_settings, magnetisation, material)
        self.length = magnets_settings['Ml']
        self.width = magnets_settings['Mw']
        self.pole_shaping = magnets_settings['Mps']
        self.inner_radius = magnets_settings['iMr']
        self.outer_radius = self.inner_radius + self.pole_shaping * self.length
        #self.inner_arc_angle = (P/PI)*np.arcsin(self.width/(2.0*self.inner_radius))
        #self.outer_arc_angle = (P/PI)*np.arcsin(self.width/(2.0*self.outer_radius))
        # TODO:
        # IT MUST BE MULTIPLIED BY POLE NUMBER
        self.inner_arc_angle = (1.0 / PI) * np.arcsin(self.width / (2.0 * self.inner_radius))
        self.outer_arc_angle = (1.0 / PI) * np.arcsin(self.width / (2.0 * self.outer_radius))
        self.mean_arc_angle = ((self.inner_arc_angle+self.outer_arc_angle)/2.0)
        self.deviation = magnets_settings['delta']*DEG2RAD
        #self._mat = mat
        #self._M = (mat._Br/MU0)
        #self._magType = magType
        self.type = self.type + 'Arc'