from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_dump


class RegionSchema(Schema):
    class Meta:
        ordered = True

    name = fields.String(required=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
