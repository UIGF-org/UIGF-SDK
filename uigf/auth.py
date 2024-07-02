import requests
import time
from . import utils, error
class User:
    def __init__(self):
        self.ltoken = ''
        self.ltoken_v2 = ''
        self.stoken = ''
        self.mid = ''
        self.ltmid_v2 = ''
        self.cookie_token = ''
        self.cookie_token_v2 = ''
        self.login_ticket = ''
        self.account_id_v2 = ''
        self.account_id = ''
        self.account_mid_v2 = ''
        self.ltuid = ''
        self.ltuid_v2 = ''
        self.cookie = ''
        
    def PasswordLogin_Pass(self, account, password,mmt_key,geetest_v4_data='',geetest_challenge='',geetest_validate='',geetest_seccode=''):
        data = {
            'account':account,
            'password':password,
            'is_crypto':False,
            'source':'user.mihoyo.com',
            'mmt_key':mmt_key,
            'geetest_seccode':geetest_seccode,
            'geetest_v4_data':geetest_v4_data,
            'geetest_challenge':geetest_challenge,
            'geetest_validate':geetest_validate,
            't': int(time.time())
        }
        url = 'https://webapi.account.mihoyo.com/Api/login_by_password'
        res = requests.post(
            url,
            json=data,
            headers=utils.getHeader(url)
        )
        if res.status_code != 200 or res.json['data']['status'] != 1:
            raise Exception('dd')
        self.login_ticket = res.json['data']['account_info']['weblogin_token']
        return res.json['data']['account_info']
        
    def QRLogin(self):
        import qrcode,os
        
        url = 'https://passport-api.miyoushe.com/account/ma-cn-passport/web/createQRLogin'
        
        header = utils.getHeader(url)
        header['x-rpc-app_id'] = 'bll8iq97cem8'
        
        req = requests.post(url,headers=header)
        
        barcode_url = req.json()['data']['url']
        qr = qrcode.QRCode()
        qr.add_data(barcode_url)
        
        print('Please scan the code to log in')
        print('You Can also scan '+os.path.abspath('qr.png'))
        
        qr.print_ascii(invert=True)
        
        img = qr.make_image()
        img.save('qr.png')
        ticket  = req.json()['data']['ticket']
        url = 'https://passport-api.miyoushe.com/account/ma-cn-passport/web/queryQRLoginStatus'
        while True:
            req = requests.post(url, json={"ticket":ticket},headers=header)
            
            retcode = req.json()['retcode']
            if retcode == -3501:
                raise error.ServerError('The QR code has expired.')
                
            elif retcode == -3505:
                raise error.ServerError('The user cancels the scan.')
                
            else:
                status = req.json()['data']['status']
                if status == 'Confirmed':
                    print(req.cookies)
                    self.ltoken = req.cookies['ltoken']
                    self.ltoken_v2 = req.cookies['ltoken_v2']
                    self.ltmid_v2 = req.cookies['ltmid_v2']
                    self.account_id = req.cookies['account_id']
                    self.account_id_v2 = req.cookies['account_id_v2']
                    self.account_mid_v2 = req.cookies['account_mid_v2']
                    self.ltuid = req.cookies['ltuid']
                    self.ltuid_v2 = req.cookies['ltuid_v2']
                    self.cookie_token = req.cookies['cookie_token']
                    self.cookie_token_v2 = req.cookies['cookie_token_v2']
                    
                    self.cookie = req.headers['Set-Cookie']
                    break
            time.sleep(0.1)
        print('Login successful.')   
        return req.json()['data'] 
               
    def GetStoken(self):
        if self.login_ticket == '':
            raise error.TokenError('login_ticket does not exist.')
        url = 'https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket'
        if self.account_id == '':
            if self.ltuid == '':
                if self.account_id_v2 == '':
                    if self.ltuid_v2 == '':
                        raise error.TokenError('No user ID')
                    else:
                        uid = self.ltuid_v2
                else:
                    uid = self.account_id_v2
            else:
                uid = self.ltuid
        else:
            uid = self.account_id
        res = requests.get(url,params={'token_types':5,'uid':int(uid),'login_ticket':self.login_ticket})
        print(res.text)
        print(res.json()['data']['list'])
   
    def GetLoginTicket_ck(self,cookie):
        import http
        ck = http.cookies.SimpleCookie()
        ck.load(cookie)
        self.login_ticket = ck['login_ticket'].value
        if 'stoken' in ck:
            self.stoken = ck['stoken']
        
        
