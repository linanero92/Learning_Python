# URL normalization
def normalize_url(url):
    https = 'https://'
    http = 'http://'
    if url[:8] == https:
        return url
    else:
        if url[:7] == http:
            return (f'{https}{url[7:]}')
        else:
            return (f'{https}{url}')
