from main import MegaSenaAPI
import requests

api = MegaSenaAPI()

data_proximo_concurso, valor_formatado = api.get_proximo_concurso()

print("Data do próximo concurso:", data_proximo_concurso)
print("Valor estimado do próximo concurso:", valor_formatado)