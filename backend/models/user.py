from tortoise import fields
from common import CommonModel


class User(CommonModel):
    user_email = fields.CharField(null=False, unique=True, description='注册邮箱', max_length=64)
    name = fields.CharField(max_length=32, unique=False, description='用户名称')
    password = fields.CharField(max_length=32, description='<PASSWORD>')
    articles: fields.ReverseRelation["Article"]

    class Meta:
        table = 'user'
        table_description = '用户表'

