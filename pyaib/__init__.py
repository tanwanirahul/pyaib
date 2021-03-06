#!/usr/bin/env python
#
# Copyright 2013 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from collections import namedtuple

# a namedtuple like that given by sys.version_info
__version_info__ = namedtuple(
    'version_info',
    'major minor micro releaselevel serial')(major=1,
                                             minor=0,
                                             micro=4,
                                             releaselevel='final',
                                             serial=0)

__version__ = '{v.major}.{v.minor}.{v.micro}'.format(v=__version_info__)
