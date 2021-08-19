from flask_app import app

from flask_app.controllers import home
# import the controller file


if __name__ == "__main__":
    app.run(debug = True)