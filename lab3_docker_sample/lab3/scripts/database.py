
from models.department import Department
from models.user import User
from api.engine import DBConn


def fill_db():
    with DBConn.get_session() as session:
        dep1 = Department(name='каф. МО ЕОМ')
        dep2 = Department(name='каф. ВТ')

        session.add(dep1)
        session.add(dep2)
        session.flush()

        user1 = User(name='Сергій Білясв', department_id=dep1.id)
        user2 = User(name='Дмитро Ліонський', department_id=dep2.id)
        user3 = User(name='Марк Заславський', department_id=dep1.id)

        session.add(user1)
        session.add(user2)
        session.add(user3)
        session.commit()
