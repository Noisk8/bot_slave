import requests
import json
from urllib.request import urlopen



r = requests.post('https://api.telegram.org/botTPKRNBOT/sendMessage',
                 data={'chat_id': 'xxxxx', 'text': 'a ver que pedo'})
                       
data=json.loads(r.text)
print(data)
