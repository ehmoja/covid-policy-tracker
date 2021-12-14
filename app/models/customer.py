# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Optional

import attr
from marshmallow import ValidationError
from marshmallow_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class Customer:
    # ToDo (Verdan): Make user_id a required field.
    #  In case if there is only email, id could be email.
    #  All the transactions and communication will be handled by ID
    id: Optional[int] = 0
    name: Optional[str] = None
    business_id_fi: Optional[str] = None
    business_id: Optional[str] = None
    website: Optional[str] = None
    street_address: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    other_key_values: Optional[Dict[str, str]] = attr.ib(factory=dict)  # type: ignore
    # TODO: Add frequent_used, bookmarked, & owned resources


class CustomerSchema(AttrsSchema):
    class Meta:
        target = Customer
        register_as_scheme = True

    # noinspection PyMethodMayBeStatic
    def _str_no_value(self, s: Optional[str]) -> bool:
        # Returns True if the given string is None or empty
        if not s:
            return True
        if len(s.strip()) == 0:
            return True
        return False


def _str_no_value(s: Optional[str]) -> bool:
    # Returns True if the given string is None or empty
    if not s:
        return True
    if len(s.strip()) == 0:
        return True
    return False


def load_customer(customer_data: Dict) -> Customer:
    try:
        schema = CustomerSchema()
        data, errors = schema.load(customer_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_user(user: Customer) -> Dict:
    schema = CustomerSchema()
    try:
        data, errors = schema.dump(user)
        return data
    except ValidationError as err:
        return err.messages
