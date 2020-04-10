import sys
import os


def launch_me():
    from FlaskMongo.MongoEngine import *
    print(f'--- flask mongo-engine -- ENV: {os.getenv("ENV_FILE_LOCATION")}')
    return app


def launch_pymongo():
    from FlaskMongo.PyMongo import *
    print("--- flask pymongo ---")

