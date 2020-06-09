# 手动设置编码
import requests

url = "http://www.weather.com.cn/data/sk/101280601.html"

response = requests.get(url)

# 打印json结果
print("响应的json数据:", response.json())

response.encoding= 'utf-8'

print("设置编码格式:", response.json())

print("字节码:", response.content.decode(encoding='utf-8'))

