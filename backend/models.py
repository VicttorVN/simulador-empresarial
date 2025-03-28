
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    rodada_atual = Column(Integer, default=1)
    participantes = relationship("Participante", back_populates="empresa")

class Participante(Base):
    __tablename__ = "participantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    empresa = relationship("Empresa", back_populates="participantes")

class Rodada(Base):
    __tablename__ = "rodadas"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer)
    status = Column(String)

class Decisao(Base):
    __tablename__ = "decisoes"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    rodada_id = Column(Integer, ForeignKey("rodadas.id"))
    comercial = Column(JSON)
    rh = Column(JSON)
    producao = Column(JSON)
    financas = Column(JSON)

class ResultadoFinanceiro(Base):
    __tablename__ = "resultados"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer)
    rodada_id = Column(Integer)
    balanco = Column(Float)
    dre = Column(Float)
    ranking = Column(Integer)
