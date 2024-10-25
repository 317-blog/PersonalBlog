pg_config = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'fastapi',
                'password': 'fastapi',
                'database': 'PersonalBlog',
            }
        },
    },
    'apps': {
        'backend': {
            'models': ['pg_models', 'aerich.pg_models'],  # models的具体路径
            'default_connection': 'default',
        }
    }
}
