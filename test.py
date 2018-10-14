import pymysql

configure = dict(
	host="localhost",user="root",
	password="root",database="test",
	port=3306,
)
conn = pymysql.connect(
	**configure
)

cursor = conn.cursor()

# 查询
count = cursor.execute("select * from user") # 获取返回记录条数
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

print(conn.insert_id())		# 返回最后一次插入的ID

# 批量插入
cursor.executemany(sql,[('test',1000),('fast','1')])

print(conn.insert_id()) # 批量执行 返回第一次

# 删除 更新 添加 都需要提交
conn.commit()

print(conn.insert_id()) # commit 提交后 结果为0
print(cursor.lastrowid) # 最后一条主键的ID 受到批量执行的影响

conn.close()




