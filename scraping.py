import requests


def proxies():
    payload = {'limit': '500', 'page': '1', 'sort_by': 'lastChecked', 'sort_type': 'desc'}
    url = 'https://proxylist.geonode.com/api/proxy-list?'
    page_num = 1
    proxy_list = []

    while True:
        payload['page'] = str(page_num)
        data = requests.get(url, params=payload, proxies=proxies)
        content = data.json()['data']
        proxy_data = [(proxy['ip'], proxy['port'], proxy['protocols']) for proxy in content]

        if not content:
            break

        proxy_list.append(proxy_data)
        page_num += 1

    return proxy_list


