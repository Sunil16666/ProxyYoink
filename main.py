if __name__ == "__main__":
    from scraping import proxies
    from text_maker import proxy_list_conversion
    from file_splitting import file_splitting

    if not proxies():
        print('list is empty')
    else:
        proxy_list_conversion()
        file_splitting()



