import time
import random
import secrets

from schema import Job, Status, redis_client, QUEUE_KEY_NAME


def worker(worker_id: str):
    print(f"Starting worker {worker_id}")
    while True:
        print("Waiting for the next job available")
        _, job_id = redis_client.blpop(QUEUE_KEY_NAME)

        # Get job from db and update status
        job = Job.get(Job.id == int(job_id))
        job.worker = worker_id
        job.status = Status.PROCESSING.value
        job.save()

        print(f"Performing a long computation with job {job.id}")
        time.sleep(random.randint(5, 10))
        print(f"Job {job.id} is ready")

        job.worker = None
        job.status = Status.READY.value
        job.save()


if __name__ == "__main__":
    try:
        worker(worker_id=secrets.token_hex(nbytes=8))
    except KeyboardInterrupt:
        pass
