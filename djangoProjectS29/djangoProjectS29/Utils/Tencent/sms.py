import ssl, json
from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from djangoProjectS29 import settings


def send_sms_single(phone_num, template_id, template_parm_list):
    appid = settings.TENCENT_APPID
    appkey = settings.TENCENT_APPKEY
    sms_singn = settings.TENCENT_sms_singn
    sender = SmsSingleSender(appid, appkey)
    try:

        sender_data = sender.send_with_param(86, phone_num, template_id, template_parm_list, sign=sms_singn)
        response = json.dumps(sender_data, ensure_ascii=False, encodings='utf-8')
    except HTTPError as e:
        data = {'result': 1000, "errmsg": "网络异常发送失败"}
        response = json.dumps(data, ensure_ascii=False, encodings='utf-8')
        print(response,type(response))
    return response
