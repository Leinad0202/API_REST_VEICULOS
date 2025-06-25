"""""

from fastapi.testclient import TestClient
from main import app, get_db, verify_api_key
from unittest.mock import MagicMock
import crud

# MOCK do banco (Session)   MOCK serve pra simular um teste sem interferir no app
class FakeDB:
    def __init__(self):
        self.data = []

    def add(self, obj): self.data.append(obj)
    def commit(self): pass
    def refresh(self, obj): pass

fake_db = FakeDB()

def override_get_db():
    yield fake_db

# Sobrescreve as dependências para o teste, ex: arquivos falsos substituindo o banco de dados real
app.dependency_overrides = {
    get_db: override_get_db,
    verify_api_key: lambda: None  # ignora autenticação no teste
}

client = TestClient(app)

def test_create_veiculo():      # Teste de criação de veículo
    payload = {
        "marca": "Honda",
        "modelo": "Civic",
        "ano": 2022,
        "placa": "XYZ-1234"
    }

    crud.create_veiculo = MagicMock(return_value=payload) # Mock da função de criação de veículo
    # Simula a chamada da rota POST /veiculos com o payload

    response = client.post("/veiculos", json=payload)

    print("Status:", response.status_code) # Debugging
    assert response.status_code == 200  # Verifica se o status é 200 OK
    print("Resposta:", response.json())

    assert response.status_code == 200


def test_listar_veiculos(): # Teste de listagem de veículos
    # Mock da função que retorna lista de veículos
    crud.get_veiculos = MagicMock(return_value=[
        {"marca": "Honda", "modelo": "Civic", "ano": 2022, "placa": "XYZ-1234"},
        {"marca": "Ford", "modelo": "Fiesta", "ano": 2020, "placa": "ABC-5678"}
    ])

    response = client.get("/veiculos")

    assert response.status_code == 200 # Verifica se o status é 200 OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["marca"] == "Honda"
    
    
def test_filtrar_veiculos(): # Teste de filtragem de veículos
    # Mock que retorna veículos filtrados
    crud.filtrar_veiculos = MagicMock(return_value=[
        {"marca": "Honda", "modelo": "Civic", "ano": 2022, "placa": "XYZ-1234"},
    ])
    
    response = client.get("/veiculos/filtro?marca=Honda")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(v["marca"] == "Honda" for v in data)
    
    
    def test_atualizar_veiculo(): # Teste de atualização de veículo
        # Mock que simula a atualização de um veículo
        veiculo_id = 1
        payload = {
            "marca": "Honda",
            "modelo": "Accord",
            "ano": 2023,
            "placa": "XYZ-9999"
        }
    
        crud.update_veiculo = MagicMock(return_value=payload) # Mock da função de atualização de veículo
    
        response = client.put(f"/veiculos/{veiculo_id}", json=payload)
    
        assert response.status_code == 200
        data = response.json()
        assert data["modelo"] == "Accord"
    
    
    def test_deletar_veiculo(): # Teste de deleção de veículo
        # Mock que simula a deleção de um veículo
        veiculo_id = 1
        crud.delete_veiculo = MagicMock(return_value={"msg": "Veículo deletado com sucesso"})
    
        response = client.delete(f"/veiculos/{veiculo_id}")
    
        assert response.status_code == 200
        data = response.json()
        # Pode checar que retornou um dicionário ou a mensagem
        assert "msg" in data

        """""