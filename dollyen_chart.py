import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import numpy as np

rows = []
column =[]
datas = [[],[],[],[],[],[],[],[],[],[],[],[]]
all_datas = []

def get_data():
    load_url = "https://www.77bank.co.jp/kawase/usd2022.html"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content,"html.parser")

    # findで要素を探す
    values = soup.find("table")
    ths = values.find_all("th")
    tds = values.find_all("td")

    # thsの中から列と行で分ける
    cnt = 0
    for i in ths:
        if cnt <=12:
            rows.append(i.text)
        else:
            column.append(i.text)
        cnt += 1

    cnt = 0
    for j in tds:
        datas[cnt % 12].append(j.text)
        cnt += 1

def main():
    df = pd.DataFrame(datas,index=rows,columns=column)
    #折れ線グラフ
    st.subheader("折れ線グラフ")
    st.line_chart(df)

    st.button("更新")

if __name__ == "__main__":
    get_data()
    main()
