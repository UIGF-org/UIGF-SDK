import requests
from . import utils
def getFP(device_id=None):
    import json
    import time
    import uuid
    import random
    import moyanlib
    if not device_id:
        device_id = moyanlib.genVerifiCode(15)
    
    url = "https://public-data-api.mihoyo.com/device-fp/api/getFp"
    payload = json.dumps({ 
        "device_id": device_id, 
        "seed_id": str(uuid.uuid4()), 
        "seed_time": str(int(round(time.time() * 1000))), 
        "platform": "2", 
        "device_fp": ''.join(random.choices('0123456789',k=10)), 
        "app_name": "bbs_cn", 
        "ext_fields": "{ \"cpuType\":\"arm64-v8a\", \"romCapacity\":\"512\", \"productName\":\"ishtar\", \"romRemain\":\"459\", \"manufacturer\":\"Xiaomi\", \"appMemory\":\"512\", \"hostname\":\"xiaomi.eu\", \"screenSize\":\"1440x3022\", \"osVersion\":\"13\", \"aaid\":\"a945fe0c-5f49-4481-9ee8-418e74508414\", \"vendor\":\"中国电信\", \"accelerometer\":\"0.061016977x0.8362915x9.826724\", \"buildTags\":\"release-keys\", \"model\":\"2304FPN6DC\", \"brand\":\"Xiaomi\", \"oaid\":\"67b292338ad57a24\", \"hardware\":\"qcom\", \"deviceType\":\"ishtar\", \"devId\":\"REL\", \"serialNumber\":\"unknown\", \"buildTime\":\"1690889245000\", \"buildUser\":\"builder\", \"ramCapacity\":\"229481\", \"magnetometer\":\"80.64375x-14.1x77.90625\", \"display\":\"TKQ1.221114.001 release-keys\", \"ramRemain\":\"110308\", \"deviceInfo\":\"Xiaomi/ishtar/ishtar:13/TKQ1.221114.001/V14.0.17.0.TMACNXM:user/release-keys\", \"gyroscope\":\"7.9894776E-4x-1.3315796E-4x6.6578976E-4\", \"vaid\":\"4c10d338150078d8\", \"buildType\":\"user\", \"sdkVersion\":\"33\", \"board\":\"kalama\" }", "bbs_device_id": "b66a6178-f56d-30ed-97aa-297560c98fc1" })
    
    response = requests.request("POST", url, headers=utils.getHeader(url), data=payload)
    return response.json()['data']['device_fp'],device_id
