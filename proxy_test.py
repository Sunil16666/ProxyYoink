from scraping import proxies

proxy_list = [
    f"{protocol}://{ip}:{port}"
    for sublist in proxies()
    for ip, port, protocols in sublist
    for protocol in protocols
]

with open('raw_proxies.txt', 'w') as f:
    for proxy in proxy_list:
        f.write('\n'.join(proxy_list))

