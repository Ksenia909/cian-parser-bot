import logging

import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from random import choice

from config_data.proxy_config import proxy_list

logger = logging.getLogger(__name__)


class CianParser:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def _get_headers_and_proxies():
        headers = {'User-Agent': UserAgent().random}
        proxies = {'http://': choice(proxy_list)}
        return headers, proxies

    async def get_links(self):
        headers, proxies = self._get_headers_and_proxies()
        async with httpx.AsyncClient(headers=headers, proxies=proxies) as client:
            response = await client.get(url=self.url)
            links = []
            try:
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    data = soup.find('div', class_='_93444fe79c--wrapper--W0WqH').find_all('div')
                    for d in data:
                        result = d.find('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
                        if result:
                            link = result.find('a', class_='_93444fe79c--media--9P6wN').get('href')
                            links.append(link)
                else:
                    logger.error(f'Failed to retrieve data. Status code: {response.status_code}')
            except Exception as e:
                logger.error(f'Error getting links: {e}')

            return links




