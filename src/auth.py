from fastapi import Header, HTTPException

API_KEY = "123456"

def verify_api_key(x_api_key: str = Header(...)):   # função usada para autenticar, Header(...) diz ser obrigatório
    if x_api_key != API_KEY:                        # verifica se a senha está correta
        raise HTTPException(status_code=401, detail="API Key inválida") # caso a senha esteja incorreta recebemos um raise HTTPException
