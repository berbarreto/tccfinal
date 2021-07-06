from datetime import datetime

import cv2
from PIL.Image import Image
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
import uuid

from database import Result, User, Analyze
from detection.borderDetection import border_detection
from detection.colorDetection import color_detection
from detection.cropImage import crop_center
from detection.diameter_detection import detect_diameter
from detection.line_symmetry import symmetry_detection
from detection.simmetryDetection import symmetry_detection2
from detection.ia_detection import ia_detection
from helper import to_json, image_to_base64


def create_result(session, user, image_path, _json):
    code = uuid.uuid4()

    if user is None:
        return {'message': "Login inválido", 'success': False, 'data': None}

    user_id = user.id
    doctor_id = 1  # TODO: RANDOM?

    image = cv2.imread(image_path)

    cropped_image = crop_center(image)
    cropped_img_path = 'imgs/{0}-cropped.png'.format(code)
    cv2.imwrite(cropped_img_path, cropped_image)
    base64cropped, _ = image_to_base64(cropped_img_path)

    border_img = border_detection(cropped_image)
    border_img_path = 'imgs/{0}-border.png'.format(code)
    cv2.imwrite(border_img_path, border_img)
    base64border, _ = image_to_base64(border_img_path)

    color_img_path = color_detection(cropped_img_path, 'imgs/tmp-{0}.png'.format(code))
    # color_img_path = 'imgs/{0}-color.png'.format(code)
    # cv2.imwrite(color_img_path, color_img)
    base64color, _ = image_to_base64(color_img_path)

    symmetry_img_path = 'imgs/{0}-symmetry.png'.format(code)
    symmetry_detection(cropped_img_path, symmetry_img_path)
    base64symmetry, _ = image_to_base64(symmetry_img_path)

    # symmetry = "Conferir imagem"
    try:
        symmetry = symmetry_detection2(border_img_path)
    except Exception as _:
        symmetry = "Conferir imagem"

    diameter_img_path = 'imgs/{0}-diameter.png'.format(code)
    xdiameter, ydiameter = detect_diameter(border_img_path, diameter_img_path)
    base64diameter, _ = image_to_base64(diameter_img_path)

    detected = ia_detection(cropped_img_path)

    new_result = Result(
        user_id=user_id,
        image=base64cropped,
        doctor_id=doctor_id,
        created_at=datetime.now(),
        symmetry=symmetry,
        diameter='{0:.2f}cm {1:.2f}cm'.format(xdiameter, ydiameter),
        ai_detection="{:.2f}%".format(detected)
    )

    new_result.analysis.append(Analyze(type="DETECÇÃO BORDA", image=base64border))
    new_result.analysis.append(Analyze(type="DETECÇÃO SIMETRIA", image=base64symmetry))
    new_result.analysis.append(Analyze(type="DETECÇÃO COR", image=base64color))
    new_result.analysis.append(Analyze(type="DETECÇÃO DIÂMETRO", image=base64diameter))

    session.add(new_result)
    session.commit()

    # new_analysis =
    #
    # result_id = session.refresh(new_result)

    return {'message': "Result created", 'success': True, 'data': to_json(new_result)}


def update_result(session, doctor, json):
    if doctor is None:
        return {'message': "Login inválido", 'success': False, 'data': None}

    id = json['id']
    feedback = json['feedback']
    tag = json['tag']

    result = session.query(Result).filter_by(id=id).first()
    result.feedback = feedback
    result.tag = tag
    session.add(result)
    session.commit()

    return {'message': "Result updated", 'success': True, 'data': to_json(result)}


def get_results_by_user(session, user):
    if user is None:
        return {'message': "Login inválido", 'success': False, 'data': None}

    results = session.query(Result) \
        .filter_by(user_id=user.id) \
        .join(User) \
        .options(joinedload(Result.analysis)) \
        .order_by(desc(Result.id)) \
        .all()

    return {'message': "Got results", 'success': True, 'data': to_json(results)}


def get_results_by_doctor(session, doctor):
    if doctor is None:
        return {'message': "Login inválido", 'success': False, 'data': None}

    results = session.query(Result) \
        .filter_by(doctor_id=doctor.id) \
        .join(User) \
        .options(joinedload(Result.analysis)) \
        .order_by(desc(Result.id)) \
        .all()

    return {'message': "Got results", 'success': True, 'data': to_json(results)}


def get_result_by_id(session, id):
    result = session.query(Result).filter_by(id=id).join(User).options(joinedload(Result.analysis)).first()

    return {'message': "Got results", 'success': True, 'data': to_json(result)}
