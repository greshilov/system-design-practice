import datetime
import enum

import redis
from peewee import Model, PostgresqlDatabase, AutoField, CharField, DateTimeField


db = PostgresqlDatabase(
    "postgres",
    host="localhost",
    port=5432,
    user="postgres",
    password="postgres",
)
redis_client = redis.Redis()

QUEUE_KEY_NAME = "queue"


class Status(enum.Enum):
    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    ERROR = "ERROR"
    READY = "READY"


class Job(Model):
    id = AutoField(primary_key=True)
    worker = CharField(null=True)
    sha = CharField(unique=True)
    status = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


if __name__ == "__main__":
    with db:
        db.create_tables([Job])
    print("Tables created!")
