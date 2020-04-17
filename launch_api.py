import sys
import os


def launch():
    # entry point for wsgi server, returns flask app
    from FlaskMongo.MongoEngine import app
    return app


if __name__ == '__main__':
    # This is true if not launched by wsgi server (gunicorn), thus app is launched in debug mode

    os.environ["ENV_FILE_LOCATION"] = ".env"

    if 'pym' in sys.argv:
        # Run from pymongo
        from FlaskMongo.PyMongo import *
        print(f'--- flask pymongo -- ENV: {os.getenv("ENV_FILE_LOCATION")}')
    else:
        # run from mongoengine
        print(f'--- flask mongo-engine -- ENV: {os.getenv("ENV_FILE_LOCATION")}')
        from FlaskMongo.MongoEngine import *

    app.run(debug=True)
