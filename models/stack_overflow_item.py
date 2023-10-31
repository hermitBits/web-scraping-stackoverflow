
from models.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class StackOverflowNewest(Base):
    __tablename__ = 'stack_overflwo_newest'

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    description: Mapped[str]