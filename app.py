import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
# line_bot_api = LineBotApi(config.get('line-bot', os.environ['channel_access_token']))
# handler = WebhookHandler(config.get('line-bot', os.environ['channel_secret']))


# @app.route("/callback", methods=['POST'])
# def callback():
#
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']
#
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
#     # handle webhook body
#
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)
#     return 'OK'
#
#
# @handler.add(MessageEvent, message=TextMessage)
# def pretty_echo(event):
#     if event.source.user_id != "U5be388a08b5ea3293c62ab9643176fcf":
#
#         # Phoebe 愛唱歌
#         pretty_text = ''
#
#         for i in event.message.text:
#             pretty_text += i
#
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=pretty_text)
#         )


@app.route("/", methods=['GET'])
def test():
    return 'hello'


if __name__ == '__main__':
    app.run()
