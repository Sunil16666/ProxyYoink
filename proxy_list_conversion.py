from scraping import proxies
import os.path

base_dir = os.path.dirname(os.path.abspath(__file__))


def proxy_list_conversion():
    x = proxies()
    proxy_list = [
        f"{protocol}://{ip}:{port}"
        for sublist in x
        for ip, port, protocols in sublist
        for protocol in protocols
    ]

    with open(
        os.path.join(
            base_dir, "raw_proxies", "raw_proxies.txt"
        ),
        "w",
    ) as f:
        for proxy in proxy_list:
            f.write("\n".join(proxy))
    print("Conversion COMPLETED")
