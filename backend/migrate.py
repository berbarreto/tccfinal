import datetime

from database import migrate, new_session, Doctor, User, Result, Analyze


def seed():
    session = new_session()

    session.add(Doctor(name="Dr Hans Chucrute", crm="123", phone="4191231823812"))
    session.add(User(name="Bernardo ", cpf="123412123123", phone="419292939293"))
    session.add(Result(doctor_id=1, user_id=1, feedback="talvesz cancrr", created_at=datetime.datetime.now(), diameter=0.13, symmetry=0.97, ai_detection=0.03, image="data:image/jpeg;base64,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"))
    session.add(Analyze(type="FODAS", result_id=1, image="data:image/jpeg;base64,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"))
    session.commit()


migrate()
seed()
