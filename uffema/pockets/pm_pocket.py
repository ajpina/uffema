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

class PMPocket(metaclass=ABCMeta):
    @property
    @abstractmethod
    def type(self):
        return 'Should never see this'

    @type.setter
    @abstractmethod
    def type(self, new_type):
        return

    def get_type(self):
        return 'Pocket'

    def __init__(self, pockets_settings):
        self.type = 'Pocket::'

    @staticmethod
    def create(pockets_settings, pocket_type='u', magnet_settings=None, magnet_type='rectangular'):
        if pocket_type == 'u':
            from uffema.pockets import PMUPocket
            pocket_instance = PMUPocket(pockets_settings, magnet_settings, magnet_type)
        elif pocket_type == 'v':
            from uffema.pockets import PMVPocket
            pocket_instance = PMVPocket(pockets_settings, magnet_settings, magnet_type)
        elif pocket_type == 'spoke':
            from uffema.pockets import PMSpoke0Pocket
            pocket_instance = PMSpoke0Pocket(pockets_settings, magnet_settings, magnet_type)
        else:
            from uffema.pockets import PMUPocket
            pocket_instance = PMUPocket(pockets_settings, magnet_settings, magnet_type)
        return pocket_instance
