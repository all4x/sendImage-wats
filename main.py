<<<<<<< HEAD
import time
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup as bs


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page(storage_state='auth.json')
        await page.goto('https://www.instagram.com/explore/tags/alanzoka/')
        time.sleep(6)
        html = await page.content()
        soup = bs(html, 'html.parser')
        link = soup.find_all('img')
        for link in soup.find_all('img'):
            foto = (link.get('src'))
            print(foto)

            # organizar links com pandas

        # await page.goto('https://www.instagram.com/explore/tags/duckcute/')

        time.sleep(5)

        # await browser.close()


asyncio.run(main())
=======
import time
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup as bs


async def main():
    async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page(storage_state= 'auth.json')
            await page.goto('https://www.instagram.com/explore/')
            time.sleep(15)
            html = await page.content()
            soup = bs(html, 'html.parser')
            link = soup.find_all('img')
            for link in soup.find_all('img'):
                url = (link.get('src'))
                return url
            # tratar os dados
            print(url)
                         
    
            
            # organizar links com pandas

            
        

            

            # await page.goto('https://www.instagram.com/explore/tags/duckcute/')

                
                
                

          
            time.sleep(5)
            
            #await browser.close()

asyncio.run(main())




    


>>>>>>> f238b564304ae1ce6052dfea88eb9134e2eab08b
