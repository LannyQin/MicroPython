import urequests

def _get_weather(city,key):
    url="http://apis.juhe.cn/simpleWeather/query?city="+city+"&key="+key
    response=urequests.get(url)
    return response.json()

def get_weather(city,key):
    result=_get_weather(city,key)
    
    if result['error_code']==0:
        realtime=result['result']['realtime']
        weather=Weather(realtime['temperature'],realtime['info'],realtime['direct'],realtime['power'],realtime['humidity'],realtime['aqi'])
        
        future=result['result']['future']
        future_list=[]
        for i in future:
            future_weather=FutureWeather(i['date'],i['temperature'],i['weather'],i['direct'])
            future_list.append(future_weather)
        
        return weather,future_list
    
    else:
        raise APIRequsetError

class Weather:
    def __init__(self,temperature,info,direct,power,humidity,aqi):
        self.temperature=int(temperature)    #温度
        self.info=info    #天气状况
        self.direct=direct    #风向
        self.power=power    #风速
        self.humidity=int(humidity)    #湿度
        self.aqi=int(aqi)    #空气指数

class FutureWeather:
    def __init__(self,date,temperature,weather,direct):
        date_list=date.split('-')
        self.year=date_list[0]
        self.month=date_list[1]
        self.day=date_list[2]
        
        temperature_list=temperature.replace('℃','').split('/')
        self.low_temperature=int(temperature_list[0])
        self.high_temperature=int(temperature_list[1])
        
        self.weather=weather
        self.direct=direct

class APIRequsetError(Exception):
    pass