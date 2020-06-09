# 搭建unittest框架
# 导包
import requests, unittest
# 创建集成unittest.testcase测试类
class TestFbcLogin(unittest.TestCase):
    # 初始化setUP和tearDown函数
    # 执行函数之前先运行
    def setUp(self) -> None:
        # 实例化session
        self.session = requests.session()
        self.login_url="http://192.168.1.135:8082/api/user/login"
    #  执行函数之后运行
    def tearDown(self) -> None:
        # 关闭session(不关会抛出错误)
        self.session.close()
    # 创建测试登录成功的函数
    def test_login_success(self):

     response_login = self.session.post(self.login_url,data={"mobile":"18598274082","password":"19ede66f218015fd9df85ac886488926","way":"0"})
     # 设置返回数据类型为字典
     jsonData = response_login.json() # type:dict
     print("登录结果:",jsonData)
     # 断言响应状态码
     self.assertEqual(200,response_login.status_code)
     # 断言errorMessage数据
     self.assertEqual(None,jsonData.get("errorMessage"))


     pass


