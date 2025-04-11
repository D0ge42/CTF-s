from os import environ
from http import HTTPStatus
from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/server-records")
def server_records():
    try:
        id = request.args["id"]
    except KeyError:
        return Response("Missing query parameter 'id'", mimetype="text/plain", status=HTTPStatus.BAD_REQUEST)
    if id.casefold() == "flag":
        return Response(environ["FLAG"], mimetype="text/plain", status=HTTPStatus.OK)
    else:
        return Response(f"Record '{id}' not found", mimetype="text/plain", status=HTTPStatus.NOT_FOUND)

def get_Request():
    payload = {'id':'flag'}
    r = requests.get("web-02.challs.olicyber.it/server-records",payload)
    print(r.text)

if __name__ == "__main__":
    app.run(host="web-02.challs.olicyber.it/server-records", debug=True)
