from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import re


def noti(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'F:\\projects\\crypto notifier\\bitcoin-icon-vector-sign-payment-260nw-792341014.ico',
        timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":

    while True:
        myHtmlData = getData('https://in.finance.yahoo.com/cryptocurrencies/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')

        myDataStr = ""
        cryptoprice = []
        for tk in soup.find_all('tr'):
            cryptoprice.append(tk.get_text())
        cryptoprice = cryptoprice[1:]
        cryp = []
        sortedcryptoprices = ""
        for i in range(0,24):
            cryp += [sortedcryptoprices]
            sortedcryptoprices = ""
            for it in range(0,len(cryptoprice[i])):
                if cryptoprice[i][it] == "-":
                    it += 3
                    for kk in range(it+1, len(cryptoprice[i])):
                        if cryptoprice[i][kk] == "+" or cryptoprice[i][kk] == "%":
                            break
                        else:
                            sortedcryptoprices += cryptoprice[i][kk]
                else:
                    continue
        cryp = cryp[1:]
        cryptoprice = []
        for j in range(0,23):
            cryptoprice += [sortedcryptoprices]
            sortedcryptoprices = ""
            for ab in range(0,len(cryp[j])):
                if cryp[j][ab] == "-":
                    break
                else:
                    sortedcryptoprices += cryp[j][ab]
        
        notititle = "Cryto Prices"
        notibody = f"prices of your favourites coins are :\n{cryptoprice[1]}\n {cryptoprice[2]}\n {cryptoprice[9]}"
        noti(notititle,notibody)

        time.sleep(20)