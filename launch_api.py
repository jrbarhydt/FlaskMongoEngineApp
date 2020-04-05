import sys
if __name__ == '__main__':
    if 'me' in sys.argv:
        print('--- flask mongo-engine --')
        from FlaskMongo.MongoEngine import *
    else:

        print("--- flask pymongo ---")
        from FlaskMongo.PyMongo import *
    app.run(debug=True)
