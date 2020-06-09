# 导包
import  requests

# json会失败
response= requests.post("http://192.168.1.244:8094/web/user/login",
                        data={"loginAccount":"zz","password":"19ede66f218015fd9df85ac886488926"})

#打印结果
print("管理后台登录结果: {} ".format(response.json()))