import pymysql

conn = pymysql.connect(
	host="localhost",user="root",
	password="root",database="test",
	port=3306,
)
cursor = conn.cursor()
# 查询
count = cursor.execute("select * from user")
print(count)
result = cursor.fetchone()
print(result)
result = cursor.fetchmany(2)
print(result)
result = cursor.fetchall()
print(result)

sql = """
	insert into user(name,age) values(%s,%s)
"""
cursor.execute(sql,('dog',3))

# 删除 更新 添加 都需要提交
conn.commit()
conn.close()




#查询
# count = cursor.execute("select * from user")
# print(count)
# result = cursor.fetchone()
# print(cursor)
# print(result)
# result = cursor.fetchmany(2)
# print(result)

# result = cursor.fetchall()
# print(result)


# 插入数据
# try:
# 	sql = """
# 	insert into user(name,age) values(%s,%s)
# 	"""
# 	cursor.execute(sql,('dog',3))
# 	conn.commit()


# 	conn.close()
# 	print('成功')
# except Exception:
# 	print('失败')
# 	conn.close()

#删除
# sql = """
# 	delete from user where id=%s
# """
# cursor.execute(sql,(4))
# conn.commit()

# conn.close()
