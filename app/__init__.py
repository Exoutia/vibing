import os

from flask import Flask, render_template  # type: ignore


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="secret-key",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/hello")
    def hello():
        return render_template("hello.html")

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    from . import todo

    app.register_blueprint(todo.bp)

    from . import meditation

    app.register_blueprint(meditation.bp)

    from . import posts

    app.register_blueprint(posts.bp)

    return app
