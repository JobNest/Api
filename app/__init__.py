from app import search
from app import login
import yaml
from flask import Flask

app = Flask(__name__)
conf = yaml.load(open('./conf/global.yml'))
app.config.update(conf)
