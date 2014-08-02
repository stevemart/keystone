# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystone.common import wsgi
from keystone.contrib.simple_cert import controllers


class SimpleCertExtension(wsgi.V3ExtensionRouter):

    PREFIX = 'OS-SIMPLE-CERT'

    def add_routes(self, mapper):
        controller = controllers.SimpleCert()

        self._add_resource(
            mapper, controller,
            path='/%s/ca' % self.PREFIX,
            get_action='get_ca_certificate')
        self._add_resource(
            mapper, controller,
            path='/%s/certificates' % self.PREFIX,
            get_action='list_certificates')
