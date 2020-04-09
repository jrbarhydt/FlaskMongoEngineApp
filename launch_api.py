import sys
import os

if __name__ == '__main__':
    os.environ["ENV_FILE_LOCATION"] = ".env"
    print(sys.argv)
    if 'me' in sys.argv:
        print(f'--- flask mongo-engine -- ENV: {os.getenv("ENV_FILE_LOCATION")}')
        from FlaskMongo.MongoEngine import *
    else:
        print("--- flask pymongo ---")
        from FlaskMongo.PyMongo import *

    if 'd' in sys.argv:
        debug = True
    else:
        debug = False

    app.run(debug=debug)
