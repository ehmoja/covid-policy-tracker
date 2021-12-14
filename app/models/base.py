# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional, Set
import uuid

import attr


@attr.s(auto_attribs=True, kw_only=True)
class BaseModel:

    @classmethod
    def get_attrs(cls) -> Set:
        raise NotImplementedError

    @classmethod
    def add_form_args(cls) -> Set:
        raise NotImplementedError


class CustomSchemaMethods:

    # noinspection PyMethodMayBeStatic
    def _str_no_value(self, s: Optional[str]) -> bool:
        # Returns True if the given string is None or empty
        if not s:
            return True
        if len(s.strip()) == 0:
            return True
        return False

    def preprocess_names(self, data):
        if data.get('first_name'):
            data['first_name'] = data['first_name'].capitalize()
            data['name'] = data['first_name']

        if data.get('last_name'):
            data['last_name'] = data['last_name'].capitalize()
            data['name'] = data['last_name']

        if data.get('first_name') and data.get('last_name'):
            data['name'] = data['first_name'] + " " + data['last_name']
        return data

    def preprocess_linkedin_url(self, data):
        if isinstance(data.get('linkedin_url'), str):
            data['linkedin_url'] = data['linkedin_url'].rstrip('/').lower()
            if data['linkedin_url'].startswith('www.'):
                data['linkedin_url'] = 'https://' + data['linkedin_url']
        return data

    def preprocess_id(self, data):
        if self._str_no_value(data.get('id')):
            data['id'] = str(uuid.uuid4())
        return data

    def nullify_empty_strings(self, data):
        for key, val in data.items():
            if val == "":
                data[key] = None
        return data
