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

"""
    Abstract base class for slots.
"""

# ==========================================================================
# Program:   slot.py
# Author:    ajpina
# Date:      12/23/16
# Version:   0.1.1
#
# Revision History:
#      Date     Version    Author      Description
#  - 12/23/16:  0.1.1      ajpina      Defines mandatory methods and properties
#
# ==========================================================================

__author__ = 'ajpina'

from abc import ABCMeta, abstractmethod


class Slot(metaclass=ABCMeta):

    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Slot'

    def __init__(self, slot_settings):
        self.type = 'Slot::'

    @staticmethod
    def create(slots_settings, slot_type='type0'):
        if slot_type == 'type0':
            from uffema.slots import Type0
            slot_instance = Type0(slots_settings)
        elif slot_type == 'type1':
            from uffema.slots import Type1
            slot_instance = Type1(slots_settings)
        else:
            from uffema.slots import Type0
            slot_instance = Type0(slots_settings)
        return slot_instance


    @abstractmethod
    def get_area(self):
        return 'Should never see this'

    @abstractmethod
    def get_slot_center(self):
        return 'Should never see this'

