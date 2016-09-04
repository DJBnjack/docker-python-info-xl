from flask import Flask
import os, sys, json

if len(sys.argv) >= 2:
    port = int(sys.argv[1])
else:
    port = 5000

if len(sys.argv) >= 3:
    message = sys.argv[2]
else:
    message = "world"

app = Flask(__name__)

from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')

@app.route('/')
def hello_world():
    ret = "<html>\n"
    ret += "<body>\n"
    ret += "  <h1>Hello, " + message + "!</h1>\n"
    ret += "  <h3>This is my environment:</h3>\n"
    ret += "  <table>\n"
    ret += "    <tr><th>Key</th><th>Value</th></tr>\n"

    keys = list(os.environ.keys())
    keys.sort()
    for k in keys:
        ret += "    <tr><td>" + k + "</td><td>" + os.environ[k] + "</td></tr>\n"

    ret += "  </table>\n"
    ret += "  <h3>Containers</h3>\n"
    ret += "  <pre>" + json.dumps(cli.containers(), sort_keys=True, indent=4) + "</pre>\n"
    ret += "  <h3>Info</h3>\n"
    ret += "  <pre>" + json.dumps(cli.info(), sort_keys=True, indent=4) + "</pre>\n"
    ret += "</body>\n"
    ret += "</html>\n"
    return ret

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)