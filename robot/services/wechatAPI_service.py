import hashlib
import json
import urllib
from urllib import parse
from urllib.request import urlopen

from wechat_sdk import WechatBasic

token = 'hiM6D8U5pHrNCAbizS9'
appid='wx8923d705afecdf34' #个人号id
#appid='wx771b76324a64714e'
appsecret='eebc78f23b0872aa1e2fca0284f6f6be'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential'  # grant_type为固定值
menu_url='https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'
wechat = WechatBasic(token=token,appid=appid, appsecret=appsecret)

#服务器地址配置
def home(self):
    #wechat = WechatBasic(token=token)
    if wechat.check_signature(signature=self.GET.get('signature'),
                              timestamp=self.GET.get('timestamp'),
                              nonce=self.GET.get('nonce')):
        if self.method == 'GET':
            rsp = self.GET.get('echostr', 'error')
        else:
            wechat.parse_data(self.body)
            message = wechat.get_message()
            print('message:',message)

            rsp =do_message(message)

            # print('rsp', rsp)
    else:
        rsp = wechat.response_text('check error')
    return rsp


#判断消息类型,并返回自定义菜单
def do_message(message):
    message_type=message.type
    user_id=message.source
    if message_type == 'text':
         res=reply_my_friend(message.content)
         return wechat.response_text(res)
    if message_type == 'image':
        #res = reply_my_friend(message.content)
        return wechat.response_text('嘿嘿嘿~ 真好看！')
    elif message_type == 'voice':
        return wechat.response_text('嘿嘿嘿~ 真好听！')
    elif message_type == 'video':
        return wechat.response_text('嘿嘿嘿~  有点意思！')
    elif message_type == 'music':
        return wechat.response_text('嘿嘿嘿~  真好听！')
    elif message_type == 'unsubscribe':
       # wechat.delete_menu()
        return ''
    elif message_type=='subscribe':
       return wechat.response_text('吼吼~!')





# # 机器人
# def get_response(msg, FromUserName):
#     api_url = 'http://www.tuling123.com/openapi/api'
#     apikey = '4bc32d41c10be18627438ae45eb839ac'
#     # data中有userd才能实现上下文一致的聊天效果。
#     hash = hashlib.md5()
#     userid = hash.update(FromUserName.encode('utf-8'))
#     data = {'key': apikey,
#             'info': msg,
#             'userid': userid
#             }
#     try:
#         req = requests.post(api_url, data=data).json()
#         return req.get('text')
#     except:
#         return

#图灵机器人类
class JinkoRobot:
    __answer = '';

    def __init__(self):
        pass;

    # 倾听话语
    def listenFor(self, string):
        self.__answer = self.thinking(string);

    # 思考着
    def thinking(self, string):
        says = urllib.parse.quote_plus(string);
        f = urllib.request.urlopen(
            "http://www.tuling123.com/openapi/api?key=4bc32d41c10be18627438ae45eb839ac&info=" + says);
        json_str = f.read();
        thinkdata = json.loads(json_str.decode('utf-8'));
        f.close();

        if (thinkdata['code'] > 40000 and thinkdata['code'] < 40010):
            return "今天被你问得有点累了, 过会再问吧!";
        return thinkdata['text'];

    # 和你交流回答
    def answer(self):
        return self.__answer;
def reply_my_friend(msg):

    #if msg.text:
    rebot = JinkoRobot();
    rebot.listenFor(msg);
    print(rebot.answer())
    return rebot.answer()