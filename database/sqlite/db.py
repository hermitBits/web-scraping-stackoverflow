from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import BaseConfig

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()

# Exemplo de uso:
# from mymodels import MyModel  # Importe seus modelos personalizados aqui, se aplicável.
# novo_objeto = MyModel(nome="Exemplo", descricao="Isso é um exemplo")
# session.add(novo_objeto)
# session.commit()
