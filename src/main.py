from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import verify_api_key
from database import get_db
import crud
from schemas import VeiculoCreate, VeiculoUpdate
from sqlalchemy import text
from typing import Optional

app = FastAPI(dependencies=[Depends(verify_api_key)]) # O FastAPI vai rodar o verify_api_key() antes de qualquer rota ser acessada.

# CREATE
@app.post("/veiculos", summary="Cria um novo veículo", description="Insere veículo com marca, modelo, ano e placa.")
def criar_veiculo(veiculo: VeiculoCreate, db: Session = Depends(get_db)): #criar um novo veículo
    return crud.create_veiculo(db, veiculo)

# READ
@app.get("/veiculos", summary="Lista todos os veículos", description=" Lista a quantidade de veículos cadastrados no sistema.")
def listar_veiculos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100): #adicionando parâmetros de paginação
    return crud.get_veiculos(db, skip=skip, limit=limit)

# READ com filtro
@app.get("/veiculos/filtro", summary="Filtra veículos", description="Filtra veículos por ID, marca, modelo, ano ou placa.")
def filtrar_veiculos( #adicionando parâmetros de filtro
    db: Session = Depends(get_db),
    id: Optional[int] = None,
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    ano: Optional[int] = None,
    placa: Optional[str] = None
):
    return crud.filtrar_veiculos(db, id=id, marca=marca, modelo=modelo, ano=ano, placa=placa)

# UPDATE
@app.put("/veiculos/{veiculo_id}" , summary="Atualiza um veículo", description="Atualiza os dados de um veículo existente.")
def atualizar_veiculo(veiculo_id: int, veiculo: VeiculoUpdate, db: Session = Depends(get_db)): #atualizar um veículo existente
    veiculo_atualizado = crud.update_veiculo(db, veiculo_id, veiculo)
    if veiculo_atualizado is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo_atualizado

# DELETE
@app.delete("/veiculos/{veiculo_id}" , summary="Deleta um veículo", description="Remove um veículo do sistema pelo ID.")
def deletar_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo_deletado = crud.delete_veiculo(db, veiculo_id) # deletar um veículo existente
    if veiculo_deletado is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo_deletado