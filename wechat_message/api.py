import time
import xmltodict
from wechat.api import Base
from .models import Message as MessageModel

class Message(Base):
    """
    Message Class, Receive and response message
    """
    def __init__(self):
        pass


    def receive(self, xml):
        receive_data = dict(xmltodict.parse(xml)['xml'])
        return receive_data

    def get_keyword(self, data):
        try:
            msg_type = data['MsgType']

            if msg_type == 'text':
                keyword = data['Content']
            elif msg_type == 'event':
                event = data['Event']
                if event == 'subscribe':
                    keyword = 'subscribe'
                elif event == 'unsubscribe':
                    keyword = 'unsubscribe'
                elif event == 'CLICK':
                    keyword = data['EventKey']
                else:
                    keyword = 'default'
            else:
                keyword = 'default'
        except KeyError:
            keyword = 'default'

        return keyword

    def response(self, keyword, data):
        try:
            message = MessageModel.objects.get(keyword=keyword)
            content = message.content % (
                data['FromUserName'],
                data['ToUserName'],
                int(time.time()),
            )
            return content
        except MessageModel.DoesNotExist:
            return 'success'
