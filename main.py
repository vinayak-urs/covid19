from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(head, txt):
    notification.notify(title=head, message=txt,app_icon='icon.ico', timeout=10, ticker='', toast=False)


def getdata(url):
    r = requests.get(url)
    return r.text


def firstelemnt(lst):
    return lst[0]


if __name__ == "__main__":

    # this portion is the soup from the mohfw.gov.in
    myHtmldata = getdata("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmldata, "html.parser")

    rawStatus = ""

    # here the parsed html will be shaped in the desired data string
    for tr in soup.find_all("tbody")[0].find_all("tr"):
        rawStatus += tr.get_text()
    rawStatus = rawStatus[1:]
    # This is the statewise divided data of the whole data
    pureStatus = rawStatus.split("\n\n")

    # this is data of the all states/city in list format
    stateData = pureStatus[:30]

    # This is the data of the india collectively
    restData = pureStatus[30:31]
    restData2 = []
    restData2 = pureStatus[31:33]

    # string to manipulate the data of the india from the website in the respective manner
    india_str = ""
    for i in restData:
        india_str += i

    india_str += "\n"

    for i in restData2:
        india_str += i

    # Whole string of the india is piled now time to mantain in a single string
    indiaData = []
    indiaData = india_str.split("\n")

    # Updating the sreial no of the india
    indiaData.insert(0, 31)
    indiaData[1] = "INDIA"

    # Cloning the data to the new list
    orData = []
    for item in stateData:
        orData.append(item.split("\n"))

    # maitining the string data in the int data as far as ease of the sorting and all things
    for item in orData:
        item[0] = int(item[0])
        item[2] = int(item[2])
        item[3] = int(item[3])
        item[4] = int(item[4])
    orData.sort(key=firstelemnt, reverse=False)

    orData.append(indiaData)
    print("STATES/CITY  CASES CURED DIED")
    # print(orData[:31])
    # printing the data of the states and city in india
    # printing the data of the states and city in india
    n = 0
    for item in orData[:31]:
        for i in item[1:]:
            print(i, end="  ")
        n = n+1
        nTitle = " Cases of COVID19"
        nText = f"State  {item[1]}  \nTotal case {item[2]}\n Cured {item[3]} \n Death {item[4]}\n"
        if n < 4 or item[0] == 31:
            notifyMe(nTitle, nText)
        time.sleep(.1)
        print("")
    #  time.sleep(7200)
    # put here the time in second after which u want the update and noification
