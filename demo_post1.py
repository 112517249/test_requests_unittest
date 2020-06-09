# 导包
import  requests

#发送post请求(from)
response=requests.post("http://192.168.1.135:8082/api/user/login",
                       json={"mobile":"18598274082","password":"19ede66f218015fd9df85ac886488926","way":"0"})



print("交易所结果:{} ".format(response.json()))