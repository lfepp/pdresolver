#
#  __init__.py
#
#  For details and documentation:
#  https://github.com/inkling/pdresolver
#
#  Copyright 2013 Inkling Systems, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
__all__ = [m[:-3] for m in os.listdir(os.path.dirname(__file__))
           if not m.startswith('__') and m[-3:] == '.py']
[__import__(module, locals(), globals()) for module in __all__]
