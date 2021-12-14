# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import os
import distutils.util
from typing import Callable, Dict, List, Optional, Set  # noqa: F401
from app.models.user import User

from flask import Flask  # noqa: F401

from app.tests.test_utils import get_test_user


class MatchRuleObject:
    def __init__(self,
                 schema_regex=None,  # type: str
                 table_name_regex=None,   # type: str
                 ) -> None:
        self.schema_regex = schema_regex
        self.table_name_regex = table_name_regex


class Config:
    LOG_FORMAT = '%(asctime)s.%(msecs)03d [%(levelname)s] %(module)s.%(funcName)s:%(lineno)d (%(process)d:' \
                 + '%(threadName)s) - %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
    LOG_LEVEL = 'INFO'

    # Path to the logging configuration file to be used by `fileConfig()` method
    # https://docs.python.org/3.7/library/logging.config.html#logging.config.fileConfig
    # LOG_CONFIG_FILE = 'app/logging.conf'
    LOG_CONFIG_FILE = None

    COLUMN_STAT_ORDER = None  # type: Dict[str, int]

    UNEDITABLE_SCHEMAS = set()  # type: Set[str]

    UNEDITABLE_TABLE_DESCRIPTION_MATCH_RULES = []  # type: List[MatchRuleObject]

    # Number of popular tables to be displayed on the index/search page
    POPULAR_TABLE_COUNT = 4  # type: int

    # Request Timeout Configurations in Seconds
    REQUEST_SESSION_TIMEOUT_SEC = 3

    # Frontend Application
    FRONTEND_BASE = ''

    # Mail Client Features
    MAIL_CLIENT = None
    NOTIFICATIONS_ENABLED = False

    # Initialize custom routes
    INIT_CUSTOM_ROUTES = None  # type: Callable[[Flask], None]

    # Settings for Issue tracker integration
    ISSUE_LABELS = []  # type: List[str]
    ISSUE_TRACKER_API_TOKEN = None  # type: str
    ISSUE_TRACKER_URL = None  # type: str
    ISSUE_TRACKER_USER = None  # type: str
    ISSUE_TRACKER_PASSWORD = None  # type: str
    ISSUE_TRACKER_PROJECT_ID = None  # type: int
    # Maps to a class path and name
    ISSUE_TRACKER_CLIENT = None  # type: str
    ISSUE_TRACKER_CLIENT_ENABLED = False  # type: bool
    # Max issues to display at a time
    ISSUE_TRACKER_MAX_RESULTS = None  # type: int

    # Programmatic Description configuration. Please see docs/flask_config.md
    PROGRAMMATIC_DISPLAY = None  # type: Optional[Dict]

    # If specified, will be used to generate headers for service-to-service communication
    # Please note that if specified, this will ignore following config properties:
    # 1. METADATASERVICE_REQUEST_HEADERS
    # 2. SEARCHSERVICE_REQUEST_HEADERS
    REQUEST_HEADERS_METHOD: Optional[Callable[[Flask], Optional[Dict]]] = None

    AUTH_USER_METHOD: Optional[Callable[[Flask], User]] = None
    GET_PROFILE_URL = None

    CREDENTIALS_MODE_ADMIN_TOKEN = os.getenv('CREDENTIALS_MODE_ADMIN_TOKEN', None)
    CREDENTIALS_MODE_ADMIN_PASSWORD = os.getenv('CREDENTIALS_MODE_ADMIN_PASSWORD', None)
    MODE_ORGANIZATION = None
    MODE_REPORT_URL_TEMPLATE = None
    # Add Preview class name below to enable ACL, assuming it is supported by the Preview class
    # e.g: ACL_ENABLED_DASHBOARD_PREVIEW = {'ModePreview'}
    ACL_ENABLED_DASHBOARD_PREVIEW = set()  # type: Set[Optional[str]]

    MTLS_CLIENT_CERT = os.getenv('MTLS_CLIENT_CERT')
    """
    Optional.
    The path to a PEM formatted certificate to present when calling the metadata and search services.
    MTLS_CLIENT_KEY must also be set.
    """

    MTLS_CLIENT_KEY = os.getenv('MTLS_CLIENT_KEY')
    """Optional. The path to a PEM formatted key to use with the MTLS_CLIENT_CERT. MTLS_CLIENT_CERT must also be set."""


class LocalConfig(Config):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'DEBUG'

    FRONTEND_PORT = '1919'

    # If installing using the Docker bootstrap, this should be modified to the docker host ip.
    LOCAL_HOST = '0.0.0.0'

    FRONTEND_BASE = os.environ.get('FRONTEND_BASE',
                                   'http://{LOCAL_HOST}:{PORT}'.format(
                                       LOCAL_HOST=LOCAL_HOST,
                                       PORT=FRONTEND_PORT))
