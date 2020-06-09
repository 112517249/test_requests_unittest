
# 导包
import  requests

#发送get请求
response=requests.get("https://www.baidu.com/")

print("响应数据为: ",response.text)