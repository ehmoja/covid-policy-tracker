# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Set

import attr
from marshmallow import ValidationError
from marshmallow_annotations.ext.attrs import AttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class Workspace:
    id: int = attr.ib()
    uuid: str = attr.ib()
    name: str = attr.ib()

    @classmethod
    def get_attrs(cls) -> Set:
        return {
            'id',
            'uuid',
            'name',
        }


class WorkspaceSchema(AttrsSchema):
    class Meta:
        target = Workspace
        register_as_scheme = True


def load_workspace(workspace_data: Dict) -> Workspace:
    try:
        schema = WorkspaceSchema()
        data, errors = schema.load(workspace_data)
        return data
    except ValidationError as err:
        return err.messages


def dump_workspace(workspace: Workspace) -> Dict:
    schema = WorkspaceSchema()
    try:
        data, errors = schema.dump(workspace)
        return data
    except ValidationError as err:
        return err.messages
