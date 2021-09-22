import time
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup as bs



async def main():
    async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page(storage_state= 'auth.json')
            await page.goto('https://www.instagram.com/explore/tags/alanzoka/')
            time.sleep(6)
            html = await page.content()
            soup = bs(html, 'html.parser')
            link = soup.find_all('img')
            for link in soup.find_all('img'):
                foto = (link.get('src'))
                
            # tratar os dados
                await page.goto(foto)
                time.sleep(15)
                await page.screenshot(path='patinho.png')         
    
            
            # organizar links com pandas

            
        

            

            # await page.goto('https://www.instagram.com/explore/tags/duckcute/')

                
                
                

          
            time.sleep(5)
            
            #await browser.close()

asyncio.run(main())




    


