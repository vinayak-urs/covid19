from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


# def notifyMe(head, txt):
#     notification.notify(
#         title=head,
#         message=txt,
#         app_icon="C:\\Users\\Gaviria\\Desktop\\covid19\\icon.ico",
#         timeout=15
#     )


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
    itemlst = itemlist[:27]
    # itemtotal = list(map(list, itemlist[27:]))
    itemtotal = itemlist[27:28]
    total2 = []
    total2 = itemlist[28:]
    # print(itemlist[29])
    ind = ""
    for i in itemtotal:
        ind += i
    ind += "\n"
    for i in total2:
        ind += i
    ortotal = []
    ortotal = ind.split("\n")
    # ortotal.insert(1, "INDIAN")
    itemls = []
    for item in itemlst:
        itemls.append(item.split("\n"))
    # # print(itemlst)
    for item in itemls:
        item[2] = int(item[2])

    itemls.sort(key=totalcase, reverse=True)
    itemls = itemls[:10]
    itemls.append(ortotal)

    for item in itemls[:11]:
        print(item)
        # nTitle = " Cases of COVID19"
        # nText = f"State  {item[1]}\n Total case {item[2]}\n Cured {item[3]} \n Death {item[4]}\n"
        # notifyMe(nTitle, nText)
        time.sleep(0.100)
