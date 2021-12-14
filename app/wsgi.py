# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from app import create_app

application = create_app('app.config.LocalConfig')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=1919)
