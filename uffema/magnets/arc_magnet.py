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

    @property
    def mag_angle(self):
        return self._mag_angle

    @mag_angle.setter
    def mag_angle(self, value):
        self._mag_angle = value

    @property
    def magnets_per_pole(self):
        return self._magnets_per_pole

    @magnets_per_pole.setter
    def magnets_per_pole(self, value):
        self._magnets_per_pole = value

    def get_type(self):
        return 'Arc'

    def __init__(self, magnets_settings, magnetisation, material_settings, mode):
        Magnet.__init__(self, magnets_settings, magnetisation, material_settings, mode)
        self.length = magnets_settings['Ml']
        self.width = magnets_settings['Mw']
        self.pole_shaping = magnets_settings['Mps']
        self.inner_radius = magnets_settings['iMr']
        self.outer_radius = self.inner_radius + self.length
        RM0 = self.inner_radius + self.length * self.pole_shaping
        #self.inner_arc_angle = (P/PI)*np.arcsin(self.width/(2.0*self.inner_radius))
        #self.outer_arc_angle = (P/PI)*np.arcsin(self.width/(2.0*self.outer_radius))
        # TODO:
        # IT MUST BE MULTIPLIED BY POLE NUMBER
        self.inner_arc_angle = (1.0 / PI) * np.arcsin(self.width / (2.0 * self.inner_radius))
        self.outer_arc_angle = (1.0 / PI) * np.arcsin(self.width / (2.0 * RM0))
        self.mean_arc_angle = ((self.inner_arc_angle+self.outer_arc_angle)/2.0)
        self.deviation = magnets_settings['delta']*DEG2RAD
        self.magnets_per_pole = 1
        self.mag_angle = [0]
        self.type = self.type + 'Arc'


    def get_magnet_geometry(self, pp):
        if self.mode == 'inner':
            beta = PI / pp
            RM0 = self.inner_radius + self.length * self.pole_shaping
            RM1 = self.outer_radius
            Miaa = 2 * pp * self.inner_arc_angle
            Moaa = 2 * pp * self.outer_arc_angle
            a_delta = RM0 * np.sin(beta * Moaa / 2.0)
            b_delta = RM1 - RM0 * np.cos(beta * Moaa / 2.0)
            c_delta = np.sqrt( a_delta**2.0 + b_delta**2.0 )
            beta_delta = np.arctan2( a_delta, b_delta)
            alpha_delta = PI - 2 * beta_delta
            Rps = c_delta * np.sin( beta_delta ) / np.sin( alpha_delta)

            points = {
                '700': [self.inner_radius, 0, 0],
                '701': [self.outer_radius, 0, 0],
                '702': [RM1 - Rps, 0, 0],
                '703': [RM0 * np.cos(-beta * Moaa / 2.0), RM0 * np.sin(-beta * Moaa / 2.0), 0],
                '704': [self.inner_radius * np.cos(-beta * Miaa / 2.0), self.inner_radius * np.sin(-beta * Miaa / 2.0),
                        0]
            }
            lines = {
                '700': [700, 701],
                '701': [701, 702, 703],
                '702': [703, 704],
                '703': [704, 1, 700]
            }
        else:
            beta = self.mean_arc_angle * 2 * pp

            points = {
                '1': [0, 0, 0],
                '700': [self.outer_radius, 0, 0],
                '701': [self.inner_radius, 0, 0],
                '702': [0, 0, 0],
                '703': [self.inner_radius * np.cos(-beta / 2.0), self.inner_radius * np.sin(-beta / 2.0), 0],
                '704': [self.outer_radius * np.cos(-beta / 2.0), self.outer_radius * np.sin(-beta / 2.0), 0]
            }
            lines = {
                '700': [700, 701],
                '701': [701, 1, 703],
                '702': [703, 704],
                '703': [704, 1, 700]
            }

        return points, lines

    def __str__(self):
        return Magnet.__str__(self)