#pylint:disable=W0102
class game_biz:
    MiYouShe = 'bbs_cn'
    YuanShen = 'hk4e_cn'
    Genshin = 'hk4e_global'
    XingQiong = 'hkrpg_cn'
    StarRail = 'hkrpg_global'

class GenshinServer:
    China = 'cn_gf01'
    Bilibili = 'cn_qd01'
    Asia = 'os_asia'
    Euro = 'os_euro'
    USA = 'os_usa'
    CHT = 'os_cht'
    
class StarRailServer:
    China = 'prod_gf_cn'
    Bilibili = 'prod_qd_cn'
    Asia = 'prod_official_asia'
    Euro = 'prod_official_eur'
    USA = 'prod_official_usa'
    CHT = 'prod_official_cht'
    
class GameID:
    Genshin = 2
    Honkai3rd = 1
    HoYoBBS = 5
    ZZZ = 8
    StarRail = 6
    
class LauncherID:
   Honkai3rd_China = 4
   
   Genshin_China = 18
   Genshin_Bilibili = 17
   Genshin_Global = 10
   
   StarRail_China = 33
   StarRail_Bilibili = 28
   StarRail_Global = 35
   
class LauncherKey:
   Honkai3rd_China = 'SyvuPnqL'
   
   Genshin_China = 'eYd89JmJ'
   Genshin_Bilibili = 'KAtdSsoQ'
   Genshin_Global = 'gcStgarh'
   
   StarRail_China = '6KcVuOkbcqjJomjZ'
   StarRail_Bilibili = 'fSPJNRwFHRipkprW'
   StarRail_Global = 'vplOVX8Vn7cwG8yb'
   
class Salt:
    x4 = 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs'
    x6 = 't0qEgfub6cvueAPgR5m9aQWWVciEer7v'
    prod = 'JwYDpKvLj6MrMqqYU6jTKF17KNO2PXoS'
    ver = '2.70.1'
    K2 = 'S9Hrn38d2b55PamfIR9BNA3Tx9sQTOem'
    LK2 = 'sjdNFJB7XxyDWGIAk0eTV8AOCfMJmyEo'
    PublicKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDvekdPMHN3AYhm/vktJT+YJr7
cI5DcsNKqdsx5DZX0gDuWFuIjzdwButrIYPNmRJ1G8ybDIF7oDW2eEpm5sMbL9zs
9ExXCdvqrn51qELbqj0XxtMTIpaCHFSI50PfPpTFV9Xt/hmyVwokoOXFlAEgCn+Q
CgGs52bFoYMtyi+xEQIDAQAB
-----END PUBLIC KEY-----'''
    
    def __init__(self):
        pass
        
    def ds1(self,salts='K2'):
        import time
        import random
        from hashlib import md5
        salts = getattr(self,salts)
        lettersAndNumbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' 
        t = int(time.time()) 
        r = "".join(random.choices(lettersAndNumbers, k=6))
        main = f"salt={salts}&t={t}&r={r}" 
        ds = md5(main.encode(encoding='UTF-8')).hexdigest() 
        return ds
        
    def ds2(self, body: dict = {}, query: dict = {},salts='x4'):
        import json
        import time
        import random
        from hashlib import md5
        
        salts = getattr(self,salts)
        get = ""
        post = json.dumps(body)
        if post == "{}":
            post = ""
        for key, value in query.items():
            if get == "":
                get = key + "=" + value
            else:
                get = get + "&" + key + "=" + value
        get = "&".join(sorted(get.split("&")))
        t = int(time.time())
        r = random.randint(100000, 200000)
        if r == 100000:
            r = 642367
        main = f"salt={salts}&t={t}&r={r}&b={post}&q={get}"
        ds = md5(main.encode(encoding="UTF-8")).hexdigest()
        final = f"{t},{r},{ds}"
        return final
            
class Header:
    def __init__(self)::
        import random, uuid
        self.osVer = str(random.randint(7,14))
        self.deviceID = str(uuid.uuid4())
        self.channel = random.choice(['Xiaomi','OPPO','Vivo', 'HUAWEI', 'Apple','Meizu', 'Samsung', 'OnePlus','HONOR', 'Nokia', 'RedMi', 'IQOO','Pixel'])
        self.model = random.choice(['Reno 2','Reno3','Reno4','Reno5','Reno6','Reno7','Reno8','Reno9','Mate60','iPhone 6S','iPhone 7','iPhone 8','iPhone X','iPhone 10', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14', 'Mate 40','P50','Nova 10','Magic4','V40', 'X30','W22','Galaxy Z Flip3','Galaxy Z Fold3','A3','A5','A7','K1','K3','Note 10','CC9','W2013','W2014','W2015','W2016','W2017','W2018','W2019','Play 3'])
        self.name = f'{self.channel} {self.model}'
    
    def __call__(self ,url):
        import random
        from urllib.parse import urlparse
        url = urlparse(url)
        base = {
            'x-rpc-sys_version':self.osVer,
            'x-rpc-device_id':self.deviceID,
            'x-rpc-channel':self.channel,
            'x-rpc-device_model':self.model,
            'x-rpc-device_name':self.name,
            'Host':url.netloc,
            'Origin':url.scheme + '://' + url.netloc,
            'User-Agent':f'Mozilla/5.0 (Linux; Android {self.osVer}; {self.name} Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 miHoYoBBS/{Salt.ver}'
            
        }
        return base
getHeader = Header()
