import requests
import json
import libs.secret.tokenlib as se

if __name__ == '__main__':
    print('Error: Este script no se puede ejecutar directamente.')
else:
    def dondeEsta():
        try:
            # Cambia el token entre comillas por el token que te entregó Chilexpress.
            token = se.CHILEXPRESS_TOKEN
            
            ce_r_dondeEsta = requests.get('https://services.wschilexpress.com/agendadigital/api/v5/Tracking/GetTracking?gls_Consulta='+ token , headers={ 'Host': 'services.wschilexpress.com',    'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',    'Sec-Ch-Ua-Mobile': '?0',    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',    'Access-Control-Allow-Methods': 'GET',    'Content-Type': 'application/json',    'Access-Control-Allow-Origin': '*',    'Accept': 'application/json, text/plain, */*',    'Ocp-Apim-Subscription-Key': '7b878d2423f349e3b8bbb9b3607d4215',    'Sec-Ch-Ua-Platform': '"Windows"',    'Origin': 'https://centrodeayuda.chilexpress.cl',    'Sec-Fetch-Site': 'cross-site',    'Sec-Fetch-Mode': 'cors',    'Sec-Fetch-Dest': 'empty',    'Referer': 'https://centrodeayuda.chilexpress.cl/',    'Accept-Language': 'es-ES,es;q=0.9',    'Connection': 'close',}, verify=True, params= { 'gls_Consulta': token,})
            ce_r_dondeEsta_json = json.loads(ce_r_dondeEsta.text)
            return '📝 **Último estado:** \n`' + ce_r_dondeEsta_json['ListTracking'][0]['gls_tracking'] + ' | ' + ce_r_dondeEsta_json['ListTracking'][0]['fec_track'].split('T')[0] + ' ' + ce_r_dondeEsta_json['ListTracking'][0]['fec_track'].split('T')[1] + '\n\n\n`**Entrega prevista:** ' + ce_r_dondeEsta_json['DatosOT']['fechaCreacion'].split('T')[0]
        except Exception as e:
            print(e)
            return 'Error al consultar el estado de tu envío.'