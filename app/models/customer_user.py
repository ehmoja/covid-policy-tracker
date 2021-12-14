# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Optional

import attr
from marshmallow import ValidationError
from marshmallow_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class CustomerUser:
    # ToDo (Verdan): Make user_id a required field.
    #  In case if there is only email, id could be email.
    #  All the transactions and communication will be handled by ID
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    role_name: Optional[str] = None
    start_date: Optional[str] = None
    expiry_date: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    customer_id: Optional[int] = None
    other_key_values: Optional[Dict[str, str]] = attr.ib(factory=dict)  # type: ignore
    # TODO: Add frequent_used, bookmarked, & owned resources


class CustomerUserSchema(AttrsSchema):
    class Meta:
        target = CustomerUser
        register_as_scheme = True

    # noinspection PyMethodMayBeStatic
    def _str_no_value(self, s: Optional[str]) -> bool:
        # Returns True if the given string is None or empty
        if not s:
            return True
        if len(s.strip()) == 0:
            return True
        return False


def load_customer_user(user_data: Dict) -> CustomerUser:
    try:
        schema = CustomerUserSchema()
        data, errors = schema.load(user_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_user(user: CustomerUser) -> Dict:
    schema = CustomerUserSchema()
    try:
        data, errors = schema.dump(user)
        return data
    except ValidationError as err:
        return err.messages
