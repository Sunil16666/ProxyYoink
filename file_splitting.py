import os.path


def file_splitting():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    max_lines = 100000
    try:
        with open(
            os.path.join(
                base_dir, "raw_proxies",
                "raw_proxies.txt",
            ),
            "r",
        ) as f_in:
            line_count = 0
            file_index = 0
            f_out = None
            for line in f_in:
                if line_count % max_lines == 0:
                    file_index += 1
                    f_out = open(
                        os.path.join(
                            base_dir, "raw_proxies",
                            f"raw_proxies_{file_index}.txt",
                        ),
                        "w",
                    )
                f_out.write(line)
                line_count += 1
                if file_index > 10000:
                    break
            try:
                f_out.close()
            except AttributeError:
                print('raw_proxies.txt is empty')
        print("FileSplitting COMPLETED")
    except FileNotFoundError:
        print("FileNotFound")
