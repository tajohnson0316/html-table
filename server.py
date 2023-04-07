from flask import Flask, render_template

application = Flask(__name__)

users = [
    {"first_name": "Michael", "last_name": "Choi"},
    {"first_name": "John", "last_name": "Supsupin"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]


@application.route("/")
def landing():
    return render_template("index.html", list_of_users=users)


if __name__ == "__main__":
    application.run(debug=True, port=5000)
