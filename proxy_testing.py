import os.path


def proxy_testing():
    if os.path.exists('raw_proxies/raw_proxies.txt'):
        mubeng = os.system('mubeng -f raw_proxies/raw_proxies.txt --check --output checked_proxies/checked_proxies.txt')
    else:
        print('raw_proxies.txt not found')
