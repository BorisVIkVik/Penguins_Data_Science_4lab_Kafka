import json

asd = {'asd': 123, 'dsa': 321}
print(asd)
dsa = json.dumps(asd)
print(type(dsa))
print(json.loads(dsa))