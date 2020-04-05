import sys
import os

if __name__ == '__main__':
    os.environ["ENV_FILE_LOCATION"] = ".env"
    if 'me' in sys.argv:
        print(f'--- flask mongo-engine -- ENV: {os.getenv("ENV_FILE_LOCATION")}')
        from FlaskMongo.MongoEngine import *
    else:

        print("--- flask pymongo ---")
        from FlaskMongo.PyMongo import *
    app.run(debug=True)
