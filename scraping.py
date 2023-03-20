import json

import requests
from yaspin import yaspin


def proxies():
    payload = {
        "limit": "500",
        "page": "1",
        "sort_by": "lastChecked",
        "sort_type": "desc",
    }
    url = "https://proxyyoinkserver-production.up.railway.app/"
    page_num = 1
    proxy_list = []

    while True:
        with yaspin(text=f"Scraping page {page_num}") as spinner:
            payload["page"] = str(page_num)
            data = requests.get(url, params=payload, timeout=10)
            try:
                content = data.json()["data"]
            except json.JSONDecodeError:
                print('\nERROR: requested content is empty')
                quit()
            proxy_data = [
                (proxy["ip"], proxy["port"], proxy["protocols"]) for proxy in content
            ]

            if len(content) == 0:
                spinner.fail("💥 ")
                print("\nScraping COMPLETED")
                break
            else:
                spinner.ok("✅ ")

            proxy_list.append(proxy_data)
            page_num += 1

    return proxy_list
