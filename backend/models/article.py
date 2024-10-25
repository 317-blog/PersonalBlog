from tortoise import fields
from tortoise.fields import OnDelete

from common import CommonModel


class Article(CommonModel):
    title = fields.CharField(max_length=16, unique=False, null=False, description='文章标题')
    content = fields.TextField(null=False, description='内容')
    author = fields.ForeignKeyField(model_name="pg_models.user", related_name="articles", on_delete=OnDelete.SET_DEFAULT)
