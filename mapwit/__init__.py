from flask import Flask, render_template
from . import plot


def create_app():

    app = Flask(__name__)

    # a simple page that prints the map
    @app.route("/")
    def index():
        map = plot.create_datapoints_map()
        return render_template("base.html", map=map)

    # a simple page that prints the demo map
    @app.route("/demo")
    def demo():
        map = plot.create_demo_map()
        return render_template("base.html", map=map)

    return app
