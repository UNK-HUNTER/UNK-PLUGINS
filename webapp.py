from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "UNK UserBot Started Successfully"

os.system("python3 -m TelethonHell")
app.run(port=5000)
