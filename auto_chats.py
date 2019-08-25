# -*- coding: utf-8 -*-
import requests, datetime

if __name__=="__main__":
    talk = input("请输入第一句消息开启对话：")
    while True:
        res = requests.post("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + talk)
        res = res.json()
        print("小云：{}  ({})".format(res["content"], datetime.datetime.now()))
        talk = res["content"]
        res = requests.post("https://api.ownthink.com/bot?spoken=" + talk)
        res = res.json()
        print("小思：{}  ({})".format(res["data"]["info"]["text"], datetime.datetime.now()))
        talk = res["data"]["info"]["text"]