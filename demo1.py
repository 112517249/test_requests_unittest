# 导包
import pymysql

# 建立连接,有事务autocommit=True

conn=pymysql.connect(host='192.168.1.139',user='root',password='123456',database='online_trade_server',port=3306,autocommit=False,charset='utf8')

# 获取游标
cursor =conn.cursor()

# 执行操作
cursor.execute("select nick_name from t_user where id=2179;")
# 打印查询结果
result= cursor.fetchone()
print("结果:",result)

#关闭游标
cursor.close()
# 关闭连接
conn.close()

