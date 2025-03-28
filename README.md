
# Simulador Empresarial – Implantação

## Executar local

pip3 install -r requirements.txt  
uvicorn backend.main:app --reload  

## Frontend (opcional)

cd frontend  
python3 -m http.server  

## Deploy (Render)

Start command:
uvicorn backend.main:app --host 0.0.0.0 --port 10000  

Variáveis:
PORT=10000  

Acesse a API:
https://seu-projeto.onrender.com/docs
