import requests


def proxies():
    payload = {'limit': '500', 'page': '1', 'sort_by': 'lastChecked', 'sort_type': 'desc'}
    url = 'https://proxyyoinkserver-production.up.railway.app/?'
    page_num = 1
    proxy_list = []

    while True:
        print(f"\rPage {page_num}", end="")
        payload['page'] = str(page_num)
        data = requests.get(url, params=payload)
        content = data.json()['data']
        proxy_data = [(proxy['ip'], proxy['port'], proxy['protocols']) for proxy in content]

        if len(content) == 0:
            print('\nScraping COMPLETED')
            break

        proxy_list.append(proxy_data)
        page_num += 1

    return proxy_list
