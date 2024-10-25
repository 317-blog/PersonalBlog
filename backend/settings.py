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
            },
            'max_size': 128,
        },
    },
    "apps": {
        "models": {
            'models': ["aerich.models", "backend.models"],  # models的具体路径
            'default_connection': 'default',
        },
    }
}
