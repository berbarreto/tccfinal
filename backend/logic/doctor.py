from database import Doctor
import auth


def create_doctor(session, json):
    name = json['name']
    crm = json['crm']
    phone = json['phone']

    new_doctor = Doctor(name=name, crm=crm, phone=phone)
    session.add(new_doctor)
    session.commit()

    return {'message': "Doctor created", 'success': True, 'data': new_doctor.serialize}


def login_doctor(session, json):
    phone = json['phone']

    doctor = session.query(Doctor).filter_by(phone=phone).first()

    auth.login_doctor('', doctor)
    print('fix me login_doctor ')

    return {'message': "Doctor logged", 'success': True, 'data': doctor.serialize}
