from Database.sensor_db import DataTable
import os
import requests




def create_all_data_dict():
    os.chdir('D:\Program\SensorServer\Database')
    data = DataTable.query_all()
    all_data_dict = {}
    for i in range(len(data)):
        item_dict = {}
        item_dict['date'] = data[i][0]
        item_dict['time'] = data[i][1]
        item_dict['light'] = data[i][2]
        item_dict['mag'] = data[i][3]
        item_dict['temp'] = data[i][4]
        all_data_dict[i] = item_dict
    return all_data_dict

def get_tips(data_dict):
    date = data_dict['date']
    time = data_dict['time']
    light = data_dict['light']
    mag = data_dict['mag']
    temp = data_dict['temp']
    tips={}
    tips['date'] = '监控日期为 '+ date+" 当日时间 "+time
    tips['light'] = '光照为'+str(light)+"lux 建议:"+lux_tip(light,time)
    tips['temp'] = '室温为'+str(temp)+"℃ 建议:"+temp_tip(temp,time)
    tips['mag'] = '室内磁场强度为'+str(mag)+'uT 建议:'+mag_tip(mag)
    return tips

def send_tips(event_name, key, text):
    url = "https://maker.ifttt.com/trigger/" + event_name + "/with/key/" + key + ""
    payload = "{\n    \"value1\": \"" + text + "\"\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    return response.text

def lux_tip(lux,time):
    hour = int(time.split('-')[0])
    if lux<30:
        if 7<hour<19:
            return "当前环境较暗，如果天气晴朗的话，打开窗帘吧"
        else:
            return "当前室内光线较暗，打开灯吧"
    elif lux<120:
        return "当前光照较为适宜,继续保持哦"
    else:
        if 7<hour<19:
            return "当前光照较为强烈，适当关闭窗帘吧"
        else:
            return "当前室内光线较亮，适当关小灯源亮度吧"


def temp_tip(temp,time):
    hour = int(time.split('-')[0])
    if temp<19:
        if hour<5 or hour >22:
            return "时间不早了，不要着凉注意休息"
        else:
            if temp<10:
                return "当前室温较低，请做好保暖措施，尽快提高室温"
            else:
                return "当前环境较为凉爽,请适当注意气温走向"
    elif temp <33:
        return "当前室温较为适宜，请继续保持吧"
    else:
        return "当前室温较高，请做好防暑措施，尽快降低室温"


def mag_tip(mag):
    if mag<20:
        return "当前传感器工作状态不稳定，注意关注后续变化和检查相应硬件"
    elif mag<60:
        return "当前传感器正常工作，您所处的环境没有强磁干扰，继续保持哦"
    else:
        return "当前传感器工作环境为强磁环绕，请注意检查附近环境，保证自身健康"

if __name__ == '__main__':
    data_dict = {'date': '2020-07-02', 'time': '23-57', 'light': 37.1, 'mag': 101.2, 'temp': 16.0}
    tips = get_tips(data_dict)


    # lux = 140
    # time = '20-57'
    # print(lux_tip(lux,time))
    #print(text)