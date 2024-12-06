from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='pizorno', email='pizorno@gmail.com', password='senha'
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'pizorno@gmail.com')
    )
    assert result.username == 'pizorno'
