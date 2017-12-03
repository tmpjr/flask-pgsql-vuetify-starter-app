import os
from flask import Flask, jsonify, redirect
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join('APP_ROOT', '.env')
load_dotenv(dotenv_path)

app = Flask(__name__, static_folder=os.getenv('STATIC_FOLDER'), static_url_path="")

@app.route('/')
def index():
    return redirect('index.html')


@app.route('/api/data')
def names():
    data = {"names": ["Elizabeth", "Kimberly", "Tom", "Annaiah", "John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))
