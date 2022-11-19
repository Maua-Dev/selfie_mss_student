# selfie_mss_student


### Criar ambiente virtual do Python (Windows):
    python -m venv venv

### Ativar ambiente virtual 
    venv\Scripts\activate

### Baixar pacotes requiridos
    pip install -r requirements-dev.txt
### Rodar o pytest
    pytest  --ignore=tests/external/dynamo --cov=./src/

😎

---

## Configurar dynamo local 

### Subir o container (ir para pasta iac/local)
    docker-compose up -d

## Configurar dynamo local (ir para pasta root)
    python -m src.shared.infra.repositories.load_student_mock_to_dynamo