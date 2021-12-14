# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Optional, Set, Any
import attr
from marshmallow import ValidationError, pre_load
from marshmallow_annotations.ext.attrs import AttrsSchema
from app.models.base import BaseModel, CustomSchemaMethods


@attr.s(auto_attribs=True, kw_only=True)
class Prospect(BaseModel):
    id: str = attr.ib()
    first_name: Optional[str] = attr.ib()
    last_name: Optional[str] = attr.ib()
    name: Optional[str] = attr.ib()
    linkedin_url: str = attr.ib()
    twitter_username: Optional[str] = attr.ib()
    headline: Optional[str] = attr.ib()
    job_title: Optional[str] = attr.ib()
    company_id: str = attr.ib()
    company_name: Optional[str] = attr.ib()
    industry_id: Optional[str] = attr.ib()
    industry_name: Optional[str] = attr.ib()
    location: Optional[str] = attr.ib()
    starred: bool = attr.ib(default=False)

    @classmethod
    def get_attrs(cls) -> Set:
        return {
            'id',
            'name',
            'linkedin_url',
            'twitter_username',
            'headline',
            'job_title',
            'company_id',
            'company_name',
            'industry_id',
            'industry_name',
            'location',
            'starred',
        }

    @classmethod
    def add_form_args(cls) -> Set:
        return {
            'first_name',
            'last_name',
            'linkedin_url',
            'job_title',
            'company_id',
        }


class ProspectSchema(AttrsSchema, CustomSchemaMethods):
    class Meta:
        target = Prospect
        register_as_scheme = True

    @pre_load
    def preprocess_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        self.preprocess_id(data)
        self.preprocess_names(data)
        self.preprocess_linkedin_url(data)
        self.nullify_empty_strings(data)
        return data


def load_prospect(prospect_data: Dict) -> Prospect:
    try:
        schema = ProspectSchema()
        data, errors = schema.load(prospect_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_prospect(prospect: Prospect) -> Dict:
    schema = ProspectSchema()
    try:
        data, errors = schema.dump(prospect)
        return data
    except ValidationError as err:
        return err.messages
