"""
Utilização schemas

Validar dados de entrada, Converter objetos SQLAlchemy para JSON.

"""
from pydantic import BaseModel, Field
from pydantic import field_validator
from typing import Optional
import re


class VeiculoBase(BaseModel):      # schema base
    marca: str = Field(..., min_length=2, max_length=50)
    modelo: str = Field(..., min_length=1, max_length=50)
    ano: int = Field(..., ge=1886, le=2100)
    placa: str = Field(..., min_length=7, max_length=8)

    @field_validator('placa')    # Mantém a placa no formato ABC-1234
    def placa_formatada(cls, v):
        padrao = r'^[A-Z]{3}-\d{4}$'  # exemplo: ABC-1234
        if not re.match(padrao, v):
            raise ValueError('Placa deve estar no formato ABC-1234')
        return v

    class Config:
        from_attributes = True     #Integração com SQLAlchemy


class VeiculoCreate(VeiculoBase):  # Schema para criar veículo (todos campos obrigatórios)
    pass


# Schema para atualizar veículo (todos campos opcionais)
class VeiculoUpdate(BaseModel):
    marca:   Optional[str] = Field(None, min_length=2, max_length=50)
    modelo:  Optional[str] = Field(None, min_length=1, max_length=50)
    ano:     Optional[int] = Field(None, ge=1886, le=2100)
    placa:   Optional[str] = Field(None, min_length=7, max_length=8)

    @field_validator('placa')   # Mantém a placa no formato ABC-1234
    def placa_formatada(cls, v):
        if v is None:
            return v
        padrao = r'^[A-Z]{3}-\d{4}$' # exemplo: ABC-1234
        if not re.match(padrao, v):
            raise ValueError('Placa deve estar no formato ABC-1234')
        return v


class Veiculo(VeiculoBase): # Schema para retornar veículo (todos campos obrigatórios)
    id: int
