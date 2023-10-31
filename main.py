from sqlalchemy import select

from models.stack_overflow_item import StackOverflowNewest
from database.sqlite.db import session

new_item = StackOverflowNewest(url='aaa', description='bbb')
session.add(new_item)
session.commit()


item = session.scalar(select(StackOverflowNewest).where(StackOverflowNewest.url == 'aaa'))


from ipdb import set_trace; set_trace()
print(item)