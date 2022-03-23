from flask import Flask, render_template, request

from schema import Job, Status, db, redis_client, QUEUE_KEY_NAME


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST" and request.form.get("sha"):

        with db.atomic() as transaction:
            job = Job.create(
                sha=request.form["sha"],
                status=Status.QUEUED.value,
            )
        # commit performed -> we can write it in redis
        redis_client.rpush(QUEUE_KEY_NAME, job.id)
        app.logger.info("scheduled a job with id %s", job.id)

    # Get all jobs
    jobs = Job.select().order_by(Job.created_at)
    return render_template("main.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)
