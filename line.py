import os
import random #加到第一行
import json
import pandas as pd
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import pandas as pd
import dataframe_image as dfi

from urllib.parse import quote,unquote


app = Flask(__name__)
url_path = 'https://9c2c-49-213-233-84.jp.ngrok.io/'
line_bot_api = LineBotApi("i7iAG4qxwGY5+PHLj3Kb0OjjnLRNhb/X7leGiCKiXD16ZnZ3ZaG/fWZp0igZGvYZoWCF3mzRMLCq7daFF+/xsvh9SPxYOG3JBQMzBRgNVDS/83V4ThAZumseoTNGLak1GwZ6KMiInSId3iMEaCMmUQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("3c7828c5953292b9559ebead7870ab6f")

@ app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@ handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    df = pd.read_csv('db.csv', encoding ='cp950')
    if '增加' in event.message.text:
        temp = event.message.text.split(' ')
        if(len(temp)) !=  5 :
            msg = TextSendMessage(text='輸入資料有誤,需要填寫: 輸入 增加 姓名 品項 功能 數值')
            line_bot_api.reply_message(event.reply_token, messages=msg)          
        try: 
            df.loc[0,'數量'] = temp[3]
            msg = TextSendMessage(text='更新成功')
            df.to_csv('db.csv',encoding='cp950')
            line_bot_api.reply_message(event.reply_token, messages=msg)
        except:
            msg = TextSendMessage(text='更新失敗')
            line_bot_api.reply_message(event.reply_token, messages=msg)
    if '測站' == event.message.text.split(' ')[0]:
        temp = event.message.text.split(' ')
        測站 = pd.read_html('https://e-service.cwb.gov.tw/wdps/obs/state.htm')[0].iloc[:,[0,1,2,6]]
        測站資料 =  測站[測站['地址'].str.contains(temp[1])]
        if 測站資料.shape[0] > 0 :
            dfi.export(測站資料, 'png/%s.png' % temp[1] )
            編碼 = quote(temp[1])
            print(url_path +'get_image?name=%s' % 編碼)
            image_message = ImageSendMessage(
                original_content_url= url_path +'get_image?name=%s' % 編碼,
                preview_image_url= url_path +'get_image?name=%s' % 編碼
            )
            
            line_bot_api.reply_message(event.reply_token, image_message)
        else:
            msg = TextSendMessage(text='此鄉鎮無測站資料')
            line_bot_api.reply_message(event.reply_token, messages=msg)

    if '查詢測站' == event.message.text.split(' ')[0]:

        try:
            temp = event.message.text.split(' ')
            測站 = pd.read_html('https://e-service.cwb.gov.tw/wdps/obs/state.htm')[0].iloc[:,[0,1,2,6]]
            測站資料 =  測站[測站['站名'] == temp[1]]
            url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=%s&stname=%s&datepicker=%s&altitude=%s"
            url = url  % (測站資料.iloc[0,0]  ,  quote(測站資料.iloc[0,1]).replace('%','%25') , temp[2],int(測站資料.iloc[0,2]) )
            print(url)
            msg = TextSendMessage(text=url)
            line_bot_api.reply_message(event.reply_token, messages=msg)
        except:
            msg = TextSendMessage(text='此鄉鎮無測站資料')
            line_bot_api.reply_message(event.reply_token, messages=msg)
    # msg = []
    # if "運勢" in event.message.text:
    #     fortune = random.choice(['大凶', '凶', '末吉', '吉','中吉','大吉'])
    #     msg.append(TextSendMessage(text=fortune))
        
    # # if "按鈕介面" in event.message.text:
    # #     line_bot_api.reply_message(event.reply_token, buttons_message())

    # line_bot_api.reply_message(event.reply_token, messages=msg[:2])


from flask import send_file

@app.route('/get_image',methods = ['GET'])
def get_image():
    name = request.args.get('name')
    filename = 'png/%s.png' %  unquote(name)
    return send_file(filename, mimetype='image/gif')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug = True)
