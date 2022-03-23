from flask import Flask, render_template, request

from schema import Job, Status, db, redis_client, QUEUE_KEY_NAME


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST" and request.form.get("sha"):

        with db.atomic() as transaction:
            pass

    # Get all jobs
    jobs = Job.select().order_by(Job.created_at)
    return render_template("main.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)
