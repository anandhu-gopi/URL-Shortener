import os
from modules.url_shortner import URLShortner
from errors import OriginalURLNotFoundError, ShortURLAlreadyExistError
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]


@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST":
        url = request.form["url"]
        if not url:
            flash("The URL is required!")
            return redirect(url_for("index"))
        url_shortner = URLShortner(url)
        try:
            url_shortner.create_short_url()
        except ShortURLAlreadyExistError:
            flash("Short URL already exist !")
        return render_template("index.html", short_url=url_shortner.get_short_url())
    return render_template("index.html")


@app.route("/<id>")
def url_redirect(id):
    url_shortner = URLShortner()
    try:
        org_url = url_shortner.get_original_url_from_short_url_id(id)
        return redirect(org_url)
    except OriginalURLNotFoundError:
        flash("Invalid URL,Please check the short URL again")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
