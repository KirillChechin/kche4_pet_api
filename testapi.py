import requests
import json

base = 'http://127.0.0.1:8000'
calls = [#"/",
		'/repeat2/', '/repeat2/jaga_', 
		'/coffie', "/coffie/?name=mocachino&size=0.2&toppings=suggar",
		]

for c in calls:
	r = requests.get(base+c)
	print("\n[CALL]\t\t",c,"\n[RESPONSE]\t", json.loads(r.text))

