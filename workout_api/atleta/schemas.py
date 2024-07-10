from typing import Annotated, Optional
from pydantic import BaseModel, Field
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta, CentroTreinamentoOut
from workout_api.contrib.schemas import BaseSchema, OutMixin
from datetime import datetime

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]

class AtletaCustomOut(BaseSchema):
    id: str
    created_at: datetime
    nome: str
    centro_treinamento: CentroTreinamentoOut
    categoria: CategoriaOut
