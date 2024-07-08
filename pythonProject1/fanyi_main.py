import base64
import hashlib
import json
import logging
import re
import sys
import time
from Crypto.Cipher import AES
import fanyi_ui, result
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import requests


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = fanyi_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.resDlg = ResDialog()
        logging.basicConfig(level=logging.DEBUG)

    def querysear(self):
        logging.info("点击翻译")
        youdao = YouDao()
        line_text = self.ui.lineEdit.text()
        if line_text:
            a = youdao.signal(line_text)
            logging.info(f"接收到数据{a}，类型{type(a)}")
            self.resDlg.t(a)
            self.resDlg.show()


    def cleartext(self):
        logging.info("点击清除")
        self.ui.lineEdit.clear()


class ResDialog(QMainWindow):
    def __init__(self):
        super(ResDialog,self).__init__()
        self.ui = result.Ui_Form()
        self.ui.setupUi(self)
        # logging.basicConfig(level=logging.DEBUG)

    def t(self,text):
        self.ui.textEdit.setPlainText(text)


class YouDao:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "339",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-97889451@222.125.16.113; OUTFOX_SEARCH_USER_ID_NCOO=305975564.64804304; UM_distinctid=18f7a23454accf-064c1459aeea9f-26001d51-144000-18f7a23454be18; DICT_DOCTRANS_SESSION_ID=OWY4NjIwYjQtNjIzMS00NGRiLWE1YTYtZjU0ZGI5NmJjNzQ5",
            "DNT": "1",
            "Host": "dict.youdao.com",
            "Origin": "https://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "https://fanyi.youdao.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "sec-ch-ua-mobile": "?0",
        }
        self.dialog = MainDialog()

    # def querysear(self):
    #     data = {
    #         "text":self.dialog.return_linetxt(),
    #         "lang": "zh",
    #         "to": "en",
    #     }
    #     # print(self.ui.lineEdit.text())
    #     youdao_url = "https://dict.youdao.com/keyword/key"
    #     res = requests.post(url=youdao_url, headers=self.headers, data=data)

    def result(self, text_AES):
        """
        AES解密
        :param text_AES:
        :return: 解密完str
        """
        #   偏移量
        decodeiv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
        # 秘钥
        decodekey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
        # 先把密匙和偏移量进行md5加密 digest()是返回二进制的值
        key = hashlib.md5(decodekey.encode(encoding='utf-8')).digest()
        iv = hashlib.md5(decodeiv.encode(encoding='utf-8')).digest()
        # AES解密 CBC模式解密
        aes_en = AES.new(key, AES.MODE_CBC, iv)
        # 将已经加密的数据放进该方法
        data_new = base64.urlsafe_b64decode(text_AES)
        # 参数准备完毕后，进行解密
        # re.findall()
        result = aes_en.decrypt(data_new).decode()

        return result

    def signal(self, in_text):
        """
        获取sign参数，开始请求
        :param in_text:
        :return: 结果
        """
        logging.info(f"接收到文本：{in_text}")
        time_sig = str(int(time.time() * 1000))
        webtranslate = "https://dict.youdao.com/webtranslate"
        text = f"client=fanyideskweb&mysticTime={time_sig}&product=webfanyi&key=fsdsogkndfokasodnaso"
        sigal1 = hashlib.md5(text.encode('utf-8')).hexdigest()
        logging.info(f"参数为{text};加密sign:{sigal1}")
        post_data = {
            "i": in_text,
            "from": "zh-CHS",
            "to": "en",
            "useTerm": "false",
            "domain": "0",
            "dictResult": "true",
            "keyid": "webfanyi",
            "sign": sigal1,
            "client": "fanyideskweb",
            "product": "webfanyi",
            "appVersion": "1.0.0",
            "vendor": "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": time_sig,
            "keyfrom": "fanyi.web",
            "mid": "1",
            "screen": "1",
            "model": "1",
            "network": "wifi",
            "abtest": "0",
            "yduuid": "abcdefg"
        }
        logging.info(f"post--data:{post_data}")
        res = requests.post(url=webtranslate, headers=self.headers, data=post_data, verify=False)
        logging.info(f"{res.url}\n{res.status_code}")
        logging.info(f"{res.text}")
        logging.info("开始解密")
        res.text2 = self.result(res.text)
        # 正则表达式[\x00-\x1F]用于匹配ASCII码值在0到31之间的控制字符，包括换行符、制表符等。匹配到的控制字符会被替换成空字符串
        end_text = re.sub(r'[\x00-\x1F]', '', res.text2)
        # logging.info(type(res.text2))
        logging.info(f"解密成功：{end_text}")
        fanyi = json.loads(end_text)["translateResult"][0][0]['tgt']
        logging.info(f"{fanyi}")
        return fanyi


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    # resDlg = ResDialog()
    # resDlg.show()
    # resDlg.ui.textEdit.setPlainText("hello word")
    # resDlg.exec_()
    # print(myDlg.return_linetxt())
    # need_text = myDlg.return_linetxt()
    # myDlg.signal(need_text)

    sys.exit(myapp.exec_())
