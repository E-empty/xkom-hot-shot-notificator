# https://www.x-kom.pl/goracy_strzal
#showing windows notification
#making a link in notifaction
#showing product + old price + new price
from win10toast import ToastNotifier
import requests
from lxml import html
import webbrowser
from apscheduler.schedulers.blocking import BlockingScheduler

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}
toaster = ToastNotifier()
url = 'https://www.x-kom.pl/goracy_strzal'
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)
product_name = ''.join(tree.xpath('//*[@id="app"]/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/h1/text()'))
product_new_price = ''.join(tree.xpath('//*[@id="app"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/span[2]/text()'))
product_old_price = ''.join(tree.xpath('//*[@id="app"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/span[1]/text()'))

msg = product_name + "\r\nStara Cena: " + product_old_price + "\r\nNowa Cena: " + product_new_price

def open_browser_tab():
    webbrowser.open(url)

def show_notification():
    toaster.show_toast("X-Kom Hot-Shot", msg, callback_on_click=open_browser_tab)

scheduler = BlockingScheduler()
scheduler.add_job(show_notification, 'cron', hour='10,22')
scheduler.start()
