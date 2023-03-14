from scraping import proxies
import os.path

proxy_list = [
    f"{protocol}://{ip}:{port}"
    for sublist in proxies()
    for ip, port, protocols in sublist
    for protocol in protocols
]

with open(os.path.join('/Users/linushenn/PycharmProjects/ProxyYoink/raw_proxies', 'raw_proxies.txt'), 'w') as f:
    for proxy in proxy_list:
        f.write('\n'.join(proxy_list))


# os.system('mubeng -f raw_proxies.txt --check --output checked_proxies.txt')

