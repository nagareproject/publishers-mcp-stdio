# --
# Copyright (c) 2008-2025 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import sys

from webob.request import Request
from webob.response import Response

from nagare.server import publisher


class Publisher(publisher.Publisher):
    def _serve(self, app, services_service, **params):
        try:
            for line in sys.stdin:
                response = services_service(
                    self.start_handle_request,
                    app,
                    response=Response(content_type='application/json'),
                    request=Request(
                        {}, headers={'accept': 'application/json'}, method='POST', path_info='', text=line.rstrip()
                    ),
                )

                if response.body:
                    sys.stdout.buffer.write(response.body)
                    sys.stdout.buffer.write(b'\n')
                    sys.stdout.buffer.flush()
        except KeyboardInterrupt:
            return 0
