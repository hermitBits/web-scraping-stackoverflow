
from sqlalchemy import select

from models.stack_overflow_item import StackOverflowNewest


def test_create_user(session):
    new_item = StackOverflowNewest(url='aaa', description='bbb')
    session.add(new_item)
    session.commit()

    item = session.scalar(select(StackOverflowNewest).where(StackOverflowNewest.url == 'aaa'))

    assert item.url == 'aaa'