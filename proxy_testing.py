import os.path
import subprocess


def proxy_testing():
    try:
        num_lines = sum(1 for line in open('raw_proxies/raw_proxies.txt'))
        for i in range(1, num_lines // 100000 + 1):
            if os.path.exists(f"raw_proxies/raw_proxies_{i}.txt"):
                subprocess.run(
                    f'mubeng -f raw_proxies/raw_proxies_{i}.txt --check --output checked_proxies/checked_proxies.txt --timeout 5s'
                )
            else:
                print(f"raw_proxies_{i}.txt not found")
    except FileNotFoundError:
        print('raw_proxies.txt not found')


proxy_testing()

