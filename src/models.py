from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): # aqui é a raiz pra criar as tabelas
    pass

class Veiculo(Base):
    __tablename__ = "veiculos"  # nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)  # id automático e indexado para consultas rápidas
    marca = Column(String, index=True)                  # marca do veículo, index para filtros
    modelo = Column(String)                         # apenas string para o modelo
    ano = Column(Integer, index=True)                    # ano do veículo
    placa = Column(String, unique=True, index=True)      # placa única, também indexada
