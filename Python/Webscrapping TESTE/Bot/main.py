import requests
import pandas as pd
import locale

class MegaSenaAPI:
    def __init__(self):
        # Configurações de localidade
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        
        # URL da API
        self.url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"
        
        # Cabeçalhos da requisição
        self.headers = {
            "cookie": "__uzma=1d86fd8b-3af9-478d-b8b6-b626f21c2536; __uzmb=1732043739; __uzme=6047; __uzmc=199681639970; __uzmd=1732045794",
            "accept": "application/json, text/plain, */*",
            "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "origin": "https://loterias.caixa.gov.br",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
        
    def get_proximo_concurso(self):
        """
        Faz a requisição para obter as informações do próximo concurso.
        Retorna os dados extraídos ou None em caso de erro.
        """
        try:
            # Realizando a requisição GET
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Levanta erro para status de resposta ruim (ex.: 404, 500)
            
            # Tentando extrair o valor estimado e data do próximo concurso
            json_res = response.json()
            valor_estimado = json_res['valorEstimadoProximoConcurso']
            data_proximo_concurso = json_res['dataProximoConcurso']
            
            # Formatar o valor estimado
            valor_formatado = locale.format_string('%.2f', valor_estimado, grouping=True)
            
            return data_proximo_concurso, valor_formatado
        
        except (ValueError, KeyError) as e:
            print(f"Erro ao acessar os dados: {e}")
            return None, None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição HTTP: {e}")
            return None, None

    def salvar_em_csv(self, data_proximo_concurso, valor_estimado):
        """
        Salva os dados do próximo concurso em um arquivo CSV.
        """
        if data_proximo_concurso and valor_estimado:
            df = pd.DataFrame({
                'Data do Proximo Concurso': [data_proximo_concurso],
                'Valor Estimado Proximo Concurso R$': [valor_estimado]
            })
            df.to_csv('valor_estimado_proximo_concurso.csv', encoding='utf-8', index=False, sep=';', decimal=',')
            print("Dados salvos em 'valor_estimado_proximo_concurso.csv'")
        else:
            print("Não foi possível salvar os dados, pois houve erro na requisição.")