# Instalar pyngrok
#!pip install pyngrok

# Importar a biblioteca necessária
from pyngrok import ngrok

# Autenticar com seu token ngrok
ngrok.set_auth_token("2hWGAfhVoe3ugbTsv1x9AqtUzu8_su4P94Gsvkc7PQ7de8iR")

# Código para iniciar o servidor Flask
#!python app.py &

# Criar o túnel ngrok para a porta 5000
public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")

# Agora o servidor Flask estará acessível pela URL pública fornecida
