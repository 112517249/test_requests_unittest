import  requests
#发送请求

response= requests.get("http://www.baidu.com/S")

print("响应状态码:",response.status_code)

print("url:",response.url)

print("编码:",response.encoding)

print("响应头:",response.headers)

print("cookies数据:",response.cookies)

print("文本数据:",response.text)

print("字节形式content数据:",response.content)


