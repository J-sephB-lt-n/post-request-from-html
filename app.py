"""
TODO
"""

import json

import flask

app = flask.Flask(__name__)


@app.route("/test", methods=["POST"])
def test():
    input_json = flask.request.get_json()
    return flask.Response("you sent me\n" + json.dumps(input_json, indent=4), status=200)


@app.after_request
def after_request(response):
    """Code which runs immediately before sending the response to the client"""

    # Deal with CORS to allow the browser to save the sessionID cookie #
    response.headers.add(
        "Access-Control-Allow-Origin",
        flask.request.origin,  # this allows any origin (DO NOT USE IN PRODUCTION)
    )

    response.headers.add(
        "Access-Control-Allow-Headers",
        "Accept, Authorization, Cookie, Content-Type, Origin, WWW-Authenticate, X-Requested-With, X-Prospekt",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    response.headers.add("Access-Control-Allow-Credentials", "true")

    return response
