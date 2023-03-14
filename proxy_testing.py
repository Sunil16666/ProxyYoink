import os.path
from file_splitting import file_splitting


def proxy_testing():
    for i in range(0-file_splitting()):
        if os.path.exists(f'raw_proxies/raw_proxies_{i}.txt'):
            mubeng = os.system(f'mubeng -f raw_proxies/raw_proxies{i}.txt --check --output checked_proxies/checked_proxies.txt')
        else:
            print(f'raw_proxies_{i}.txt not found')
