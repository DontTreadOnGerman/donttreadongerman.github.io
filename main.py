import logging
import yaml
import os
import objectfile
from flask_frozen import Freezer
from flask import Flask

# Configs
app = Flask(__name__)
logging.basicConfig(format="[%(asctime)s %(name)s %(levelname)s] %(message)s", level=logging.INFO)
config = yaml.safe_load(open("config.yml"))
freezer = Freezer(app)
if __name__ == '__main__':
    freezer.freeze()


@app.route('/')
def hello():
    return 'Hello, World!'
