import requests

def obtener_datos_nequi():
    url = "/-services-paymentservice-unregisteredpayment" 
    headers = {
        "Authorization": "https://docs.conecta.nequi.com.co/#!/Solicitud32de32token/post_token", 
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener datos de Nequi:", response.status_code)
        return None

def agregar_a_notion(datos):
    notion_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": "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", 
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"  
    }
    
    for dato in datos:  
        payload = {
            "parent": { "database_id": "test_database" },
            "properties": {
                "Nombre": {
                    "title": [
                        {
                            "text": {
                                "content": dato['nombre']  
                            }
                        }
                    ]
                },
                "Saldo": {
                    "number": dato['saldo']  
                }
            }
        }
        
        response = requests.post(notion_url, headers=headers, json=payload)
        if response.status_code != 200:
            print("Error al agregar datos a Notion:", response.status_code)

def main():
    datos_nequi = obtener_datos_nequi()
    if datos_nequi:
        agregar_a_notion(datos_nequi)

if __name__ == "__main__":
    main()
