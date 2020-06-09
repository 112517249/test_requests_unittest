import requests
# 设置请求头
# headers = {"Content-Type":"application/json"}

headers = {"Content-Type":"application/x-www-form-urlencoded"}

# response=requests.post("http://192.168.1.135:8082/api/user/login",data={"mobile":"18598274082","password":"19ede66f218015fd9df85ac886488926","way":"0"},headers=headers)
response=requests.post("http://192.168.1.135:8082/api/user/login",data={"mobile":"18598274082","password":"19ede66f218015fd9df85ac886488926","way":"0"},headers=headers)
# 打印结果
print("管理后台登录结果: {} ".format(response.json()))