# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Optional
import attr
from marshmallow import ValidationError
from marshmallow_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class Influencer:
    # ToDo (Verdan): Make user_id a required field.
    #  In case if there is only email, id could be email.
    #  All the transactions and communication will be handled by ID
    id: str = attr.ib()
    name: Optional[str] = attr.ib()
    linkedin_url: str = attr.ib()
    twitter_username: str = attr.ib()
    headline: Optional[str] = attr.ib()
    job_titles: List[str] = attr.ib(factory=list)
    company_names: List[str] = attr.ib(factory=list)
    location: str = attr.ib()


class InfluencerSchema(AttrsSchema):
    class Meta:
        target = Influencer
        register_as_scheme = True


def load_influencer(influencer_data: Dict) -> Influencer:
    try:
        schema = InfluencerSchema()
        data, errors = schema.load(influencer_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_influencer(user: Influencer) -> Dict:
    schema = InfluencerSchema()
    try:
        data, errors = schema.dump(user)
        return data
    except ValidationError as err:
        return err.messages
