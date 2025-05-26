# --
# Copyright (c) 2008-2025 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import sys

from nagare.server import publisher


class Publisher(publisher.Publisher):
    def _serve(self, app, services_service, **params):
        try:
            for line in sys.stdin:
                services_service(self.start_handle_request, app, stdin=line.rstrip())
        except KeyboardInterrupt:
            return 0
