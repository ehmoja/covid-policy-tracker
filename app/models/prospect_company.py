# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Optional, Set, Any
import attr
from marshmallow import ValidationError, pre_load
from marshmallow_annotations.ext.attrs import AttrsSchema
from app.models.base import BaseModel, CustomSchemaMethods


@attr.s(auto_attribs=True, kw_only=True)
class ProspectCompany(BaseModel):
    # ToDo (Verdan): Make user_id a required field.
    #  In case if there is only email, id could be email.
    #  All the transactions and communication will be handled by ID
    id: str = attr.ib()
    name: str = attr.ib()
    business_id_fi: Optional[str] = attr.ib()
    business_id: Optional[str] = attr.ib()
    linkedin_url: Optional[str] = attr.ib()
    website: Optional[str] = attr.ib()
    street_address: Optional[str] = attr.ib()
    zip: Optional[str] = attr.ib()
    city: Optional[str] = attr.ib()
    state: Optional[str] = attr.ib()
    country: Optional[str] = attr.ib()
    customer_id: str = attr.ib()
    # TODO: Add frequent_used, bookmarked, & owned resources

    @classmethod
    def get_attrs(cls) -> Set:
        return {
            'id',
            'name',
            'business_id',
            'business_id_fi',
            'linkedin_url',
            'website',
            'street_address',
            'zip',
            'city',
            'state',
            'country',
            'customer_id',
        }

    @classmethod
    def add_form_args(cls) -> Set:
        return {
            'name',
            'business_id',
            'linkedin_url',
            'website',
            'street_address',
            'zip',
            'city',
            'state',
            'country',
        }


class ProspectCompanySchema(AttrsSchema, CustomSchemaMethods):
    class Meta:
        target = ProspectCompany
        register_as_scheme = True

    # noinspection PyMethodMayBeStatic
    def _str_no_value(self, s: Optional[str]) -> bool:
        # Returns True if the given string is None or empty
        if not s:
            return True
        if len(s.strip()) == 0:
            return True
        return False

    @pre_load
    def preprocess_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        self.preprocess_id(data)
        self.preprocess_linkedin_url(data)
        self.nullify_empty_strings(data)

        if isinstance(data.get("website"), str):
            data["website"] = data["website"].lower()

        if isinstance(data.get('business_id'), str):
            if data['business_id'][0:2] == "FI":
                data['business_id_fi'] = data['business_id'][2:9] + "-" + data['business_id'][-1]

        return data


def load_prospect_company(prospect_company_data: Dict) -> ProspectCompany:
    try:
        schema = ProspectCompanySchema()
        data, errors = schema.load(prospect_company_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_prospect_company(prospect_company: ProspectCompany) -> Dict:
    schema = ProspectCompanySchema()
    try:
        data, errors = schema.dump(prospect_company)
        return data
    except ValidationError as err:
        return err.messages
