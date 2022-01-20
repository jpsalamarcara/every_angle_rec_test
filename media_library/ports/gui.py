from flask import Flask, request, render_template, redirect
import os

from media_library.core.datasources.item_datasource import ItemDataSource
from media_library.core.domain.item import Item
from media_library.ports.dependencies import default_injector

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
service = default_injector.get(ItemDataSource)


@app.errorhandler(Exception)
def handle_errors(exception):
    message = 'internal server error'
    error_type = "Error!"
    if isinstance(exception, AssertionError):
        message = str(exception)
        error_type = "Validation"
    return render_template("error.html", error_message=message, error_type=error_type)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", items=service.get())


@app.route("/library/add/", methods=["POST"])
def post_item():
    data = request.form
    item = Item(name=data.get('name'), media_type=data.get('media_type'), location=data.get('location'))
    service.save(item)
    return redirect("/", code=302)


@app.route("/library/modify/<uid>", methods=["POST"])
def update(uid):
    data = request.form
    item = Item(uid=uid, name=data.get('name'), media_type=data.get('media_type'), location=data.get('location'))
    service.save(item)
    return redirect("/", code=302)


@app.route("/library/delete/<uid>", methods=["POST"])
def delete_item(uid):
    service.delete(uid)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
