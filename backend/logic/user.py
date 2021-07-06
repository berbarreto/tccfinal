from database import User
import auth


def create_user(session, json):
    name = json['name']
    cpf = json['cpf']
    email = json['email']
    birth_date = json['birth_date']
    phone = json['phone']

    new_user = User(name=name, cpf=cpf, email=email, birth_date=birth_date, phone=phone)
    session.add(new_user)
    session.commit()

    return {'message': "User created", 'success': True, 'data': new_user}


def login_user(session, json):
    phone = json['phone']
    user = session.query(User).filter_by(phone=phone).first()

    auth.login_user('', user)

    print('fix me login_user ')

    return {'message': "User logged", 'success': True, 'data': user}
