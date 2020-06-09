#导包
import  requests
#查询参数在url中
response=requests.get("http://www.baidu.com/S?ie=UTF-8&wd=python")
#参数为params字符串
response_params_string=requests.get("http://www.baidu.com/S",params="wd=淮上")

#参数为字典
response_params_dict=requests.get("http://www.baidu.com/S",params={"wd":"priest"})
#打印结果
# print(response.text)

# print("params的结果",response_params_string.text)

print("字典的结果",response_params_dict.text)