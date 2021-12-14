# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import logging

from flask.blueprints import Blueprint
LOGGER = logging.getLogger(__name__)

blueprint = Blueprint('main', __name__, url_prefix='/api')
