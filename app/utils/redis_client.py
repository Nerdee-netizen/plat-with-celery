import json

import redis

from app.utils.config import EnvSettings


class RedisClient:
    def __init__(self, env: EnvSettings) -> None:
        self.redis_client = redis.Redis(
            host=env.REDIS_HOST,
            port=env.REDIS_PORT,
            username=env.REDIS_USERNAME,
            password=env.REDIS_PASSWORD,
        )

    def publish(self, routing_key: str, data: dict) -> None:
        self.redis_client.publish(routing_key, json.dumps(data))