from flask import jsonify


def invalid_route(e):
    output = {"error":
              {"message": "404 error: This route is currently not supported. See API documentation."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp
