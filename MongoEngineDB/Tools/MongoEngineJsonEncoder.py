from flask.json import JSONEncoder
from bson import json_util, ObjectId
from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet


class MongoEngineJSONEncoder(JSONEncoder):
    """
    Forked from: https://gist.github.com/corydolphin/11005158
    """

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, BaseDocument):
            return json_util._json_convert(obj.to_mongo())
        elif isinstance(obj, BaseQuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return JSONEncoder.default(self, obj)
