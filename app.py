from flask import Flask, send_from_directory, jsonify
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

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/')
def hello_world():
    return send_from_directory('static', 'index.html')

@app.route('/containers')
def container_info():
    return jsonify(containers = cli.containers())

@app.route('/info')
def docker_info():
    return jsonify(info = cli.info())


@app.route('/services')
def docker_services():
    return jsonify(services = cli.services())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)