import os.path

from flask import Flask, Response
app = Flask(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/myaso/')
def Myaso():
    content = get_file('sosa.html')
    return Response(content, mimetype="text/html")

@app.route('/')
def MainSlash():
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route('/generator.js')
def Generator():
    contentcontent = get_file('generator.js')
    return Response(content, mimetype="text/javascript")

