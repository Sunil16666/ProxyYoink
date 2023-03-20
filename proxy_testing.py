import os.path


def proxy_testing():
    try:
        num_lines = sum(1 for line in open('raw_proxies/raw_proxies.txt'))
        for i in range(1, num_lines // 100000 + 1):
            if os.path.exists(f"raw_proxies/raw_proxies_{i}.txt"):
                mubeng = os.system(
                    f"mubeng -f --update raw_proxies/raw_proxies{i}.txt --check --timeout 5 --output checked_proxies/checked_proxies.txt"
                )
            else:
                print(f"raw_proxies_{i}.txt not found")
    except FileNotFoundError:
        print('raw_proxies.txt not found')