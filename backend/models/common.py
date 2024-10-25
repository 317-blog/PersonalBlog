from tortoise.models import Model
from tortoise import fields


class CommonModel(Model):
    """
    Common model for all models
    """
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间", null=False)
    modified_at = fields.DatetimeField(auto_now=True, description="修改时间", null=False)

    class Meta:
        abstract = True
        ordering = ["-created"]
