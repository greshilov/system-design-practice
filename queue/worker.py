import time
import random
import secrets

from schema import Job, Status, redis_client, QUEUE_KEY_NAME


def worker(worker_id: str):
    pass


if __name__ == "__main__":
    try:
        worker(worker_id=secrets.token_hex(nbytes=8))
    except KeyboardInterrupt:
        pass
