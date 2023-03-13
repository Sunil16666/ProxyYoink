from scraping import proxies
import json

index = 0
proxy_list = []
while True:
    for proxy in proxies():
        proxy_list.append(f'{proxy[index][2][0]}://{proxy[index][0]}:{proxy[index][1]}')
    index += 1
    if index == 19:
        break


with open('proxies.json', 'w') as f:
    json.dump(proxy_list, f)
