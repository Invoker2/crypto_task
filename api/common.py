import datetime

def time_now(fmt = "%Y%m%d"):
    return  datetime.datetime.now().strftime(fmt)

def time_today_after_tomorrow(fmt = "%Y%m%d"):
    return (datetime.datetime.now()+datetime.timedelta(days=2)).strftime(fmt)


def time_func():
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
    pastTimeMinutes = (datetime.datetime.now()+datetime.timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')#5分钟后
    pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#一小时前
    afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#昨天
    tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
    print("现在：    "+nowTime)
    print("5分钟后： "+pastTimeMinutes)
    print("一小时前： "+pastTime)
    print("后天：    "+afterTomorrowTime)
    print("昨天：    "+yesterday)
    print("明天：    "+tomorrowTime)

if __name__ == "__main__":
    # time_func()
    print(time_today_after_tomorrow())