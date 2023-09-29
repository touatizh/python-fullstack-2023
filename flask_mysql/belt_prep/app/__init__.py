from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt(app)
app.bcrypt = bcrypt

app.secret_key = "bc62bf81147cd3594d5400414e3f6161"
