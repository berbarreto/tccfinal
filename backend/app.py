import base64

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from keras.models import load_model

from detection import set_model
from helper import image_to_base64
from logic.doctor import login_doctor, create_doctor
from logic.result import create_result, get_results_by_user, get_results_by_doctor, update_result, get_result_by_id
from logic.user import create_user, login_user
from database import new_session
import auth

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

session = new_session()

set_model()


def get_token(headers):
    return headers['Authorization']


@app.route('/loginUser', methods=['POST'])
@cross_origin()
def route_login_user():
    return jsonify(login_user(session, request.json))


@app.route('/loginDoctor', methods=['POST'])
@cross_origin()
def route_login_doctor():
    return jsonify(login_doctor(session, request.json))


@app.route('/createUser', methods=['POST'])
@cross_origin()
def route_create_user():
    return jsonify(create_user(session, request.json))


@app.route('/createDoctor', methods=['POST'])
@cross_origin()
def route_create_doctor():
    return jsonify(create_doctor(session, request.json))


@app.route('/createResult', methods=['POST'])
@cross_origin()
def route_create_results():
    uploaded_file = request.files['file']
    path = 'imgs/' + uploaded_file.filename

    if uploaded_file.filename != '':
        uploaded_file.save(path)

    token = get_token(request.headers)
    user = auth.get_user(token)

    return jsonify(create_result(session, user, path, request.json))


@app.route('/getResultsByUser', methods=['GET'])
@cross_origin()
def route_get_results_by_user():
    token = get_token(request.headers)
    user = auth.get_user(token)
    return jsonify(get_results_by_user(session, user))


@app.route('/getResultsByDoctor', methods=['GET'])
@cross_origin()
def route_get_results():
    token = get_token(request.headers)
    doctor = auth.get_doctor(token)
    return jsonify(get_results_by_doctor(session, doctor))


@app.route('/getResultById/<id>', methods=['GET'])
@cross_origin()
def route_get_result(id):
    return jsonify(get_result_by_id(session, id))


@app.route('/updateResult/', methods=['POST'])
@cross_origin()
def route_update_result():
    token = get_token(request.headers)
    doctor = auth.get_doctor(token)
    return jsonify(update_result(session, doctor, request.json))
