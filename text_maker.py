from scraping import proxies
import os.path


def proxy_list_conversion():
    x = proxies()
    proxy_list = [
        f"{protocol}://{ip}:{port}"
        for sublist in x
        for ip, port, protocols in sublist
        for protocol in protocols
    ]

    with open(os.path.join('/Users/linushenn/PycharmProjects/ProxyYoink/raw_proxies', 'raw_proxies.txt'), 'w') as f:
        for proxy in proxy_list:
            f.write('\n'.join(proxy))
    print('Conversion COMPLETED')

