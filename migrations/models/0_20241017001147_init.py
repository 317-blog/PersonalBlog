from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_email" VARCHAR(64) NOT NULL UNIQUE,
    "name" VARCHAR(32) NOT NULL,
    "password" VARCHAR(32) NOT NULL
);
COMMENT ON COLUMN "user"."created_at" IS '创建时间';
COMMENT ON COLUMN "user"."modified_at" IS '修改时间';
COMMENT ON COLUMN "user"."user_email" IS '注册邮箱';
COMMENT ON COLUMN "user"."name" IS '用户名称';
COMMENT ON COLUMN "user"."password" IS '<PASSWORD>';
CREATE TABLE IF NOT EXISTS "article" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "title" VARCHAR(16) NOT NULL,
    "content" TEXT NOT NULL,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE SET DEFAULT
);
COMMENT ON COLUMN "article"."created_at" IS '创建时间';
COMMENT ON COLUMN "article"."modified_at" IS '修改时间';
COMMENT ON COLUMN "article"."title" IS '文章标题';
COMMENT ON COLUMN "article"."content" IS '内容';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
