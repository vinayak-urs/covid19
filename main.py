from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(head, txt):
    notification.notify(title=head, message=txt,
                        app_icon='C:\\Users\\Gaviria\\Desktop\\covid19\\icon.ico', timeout=10, ticker='', toast=False)


def getdata(url):
    r = requests.get(url)
    return r.text


def totalcase(lst):
    return lst[2]


if __name__ == "__main__":
    #  notifyMe("pagal", "lets track the COVID 19")
    myHtmldata = getdata("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmldata, "html.parser")
    myDataStr = ""
    itemtotal = []

    for tr in soup.find_all("tbody")[0].find_all("tr"):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemlist = myDataStr.split("\n\n")
    itemlst = itemlist[:29]
    # itemtotal = list(map(list, itemlist[27:]))
    itemtotal = itemlist[30:31]
    total2 = []
    total2 = itemlist[31:33]
    ind = ""
    for i in itemtotal:
        ind += i
    ind += "\n"
    for i in total2:
        ind += i
    ortotal = []
    ortotal = ind.split("\n")
    # print(ortotal)
    ortotal.insert(0, 000)
    itemls = []
    for item in itemlst:
        itemls.append(item.split("\n"))
    # # print(itemlst)
    for item in itemls:
        item[2] = int(item[2])
    ortotal[1] = "INDIA"
    itemls.sort(key=totalcase, reverse=True)
    itemls = itemls[:3]
    itemls.append(ortotal)
    print("STATES/CITY  CASES CURED DIED")
    for item in itemls[:4]:
        for i in item[1:]:
            print(i, end="  ")
        print("")
        nTitle = " Cases of COVID19"
        nText = f"State  {item[1]}  \nTotal case {item[2]}\n Cured {item[3]} \n Death {item[4]}\n"
        notifyMe(nTitle, nText)
        time.sleep(5)
    # time.sleep(7200)
