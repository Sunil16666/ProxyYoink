import os.path
from tqdm import tqdm


def file_splitting():
    max_lines = 100000
    try:
        with open(
            os.path.join(
                "/Users/linushenn/PycharmProjects/ProxyYoink/raw_proxies",
                "raw_proxies.txt",
            ),
            "r",
        ) as f_in:
            line_count = 0
            file_index = 0
            for line in f_in:
                if line_count % max_lines == 0:
                    file_index += 1
                    f_out = open(
                        os.path.join(
                            "/Users/linushenn/PycharmProjects/ProxyYoink/raw_proxies",
                            f"raw_proxies_{file_index}.txt",
                        ),
                        "w",
                    )
                f_out.write(line)
                line_count += 1
                if file_index > 10000:
                    break
            f_out.close()
        print("FileSplitting COMPLETED")
    except FileNotFoundError:
        print("FileNotFound")
