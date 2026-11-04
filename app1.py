import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m'

resposta = requests.get(URL)

dados = resposta.json()

print(resposta.status_code)

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)

clima = dados['current']
print(clima)

while True:
    print('\n============== MENU ===============')
    print('Digite 1/ para consultar a Temperatura.')
    print('Digite 2/ para consultar a Humidade.')
    print('Digite 3/ para consultar a Data.')
    print('Digite 4/ para consultar a Velocidade do Vento.')
    print('Digite 5/ para consultar a Latitude.')
    print('Digite 6/ para consultar a Longetude.')
    print('Digite 7/ para Sair.')

    ver = input('Digite o que você quer consultar:')

    if ver == '1':
        print('\nTemperatura:', clima["temperature_2m"])

    if ver == '2':
            print('\nHumidade:', clima['relative_humidity_2m'])

    if ver == '3':
        print('Data:', clima['time'])

    if ver == '4':
       print('Velocidade:', clima['wind_speed_10m'])

    if ver == '5':
        print('Latitude:', dados['latitude'])

    if ver == '6':
        print('Longetude:', dados['longitude' ])

    if ver == '7':
        print('Encerrando a consulta.')
        break



