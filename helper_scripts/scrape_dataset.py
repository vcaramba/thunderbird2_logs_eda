import requests
import wget
from bs4 import BeautifulSoup

ZIP_PATH = '../data/tbird2.gz'
RAW_DATASET_PATH = '../data/tbird2.txt'


def get_data_link(url):
    headers = requests.utils.default_headers()
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    link = soup.find("a", href=lambda href: href and "tbird2" in href)

    if len(soup.find_all("a", href=lambda href: href and "tbird2" in href)) == 1:
        return link.get('href')
    else:
        raise Exception('no matching url found')


def download_dataset(url):
    data_link = get_data_link(url)
    try:
        wget.download(data_link, ZIP_PATH)
    except Exception as e:
        print("Could not download file")
        print(e)


if __name__ == '__main__':
    url = "https://www.usenix.org/cfdr-data"
    download_dataset(url)
