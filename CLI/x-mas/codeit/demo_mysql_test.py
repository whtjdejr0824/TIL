import mysql.connector

# db 접속 : id,비번 입력
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="-",
  database="mydatabase"
)

# print(mydb)

##객체지정 및 DB불러오기
mycursor = mydb.cursor()
# DB생성
# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")
# #존재하는 DB 목록 확인
# for x in mycursor:
#   print(x)

# 테이블 생성
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# 생성된 테이블 확인
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# Primary key
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# 이미 있으면 ALTER_TABLE 키워드 사용
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# "customers"테이블에 레코드를 삽입
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


# 여러 행 삽입
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# 삽입된 ID 가져오기
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ('Amy', 'Apple st 652')
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

# "customers"테이블에서 모든 레코드를 선택하고 결과를 표시합니다.
# 참고 :fetchall() 마지막으로 실행 된 문에서 모든 행을 가져 오는 메서드를 사용합니다 .
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# 선택 된 열(이름, 주소)만 출력
# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# 한 행에만 관심이있는 경우 fetchone()방법을 사용
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)


# 필터링
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# 와일드 카드 문자
# way는 단어가 포함된 레코드 선택
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# SQL 주입방지
# placholder %s 메서드 를 사용하여 쿼리 값을 이스케이프
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # 결과 정렬(SORT)
# sql = "SELECT * FROM customers ORDER BY name"
# 오름차순 정렬
# sql = "SELECT * FROM customers ORDER BY name DESC"


# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#데이터베이스 삭제
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# delete 문에서도 쿼리 값을 이스케이프하는 것이 좋음.
# 이는 데이터베이스를 파괴하거나 오용하는 일반적인 웹 해킹 기술인 SQL 주입을 방지하기위한 것
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# 테이블삭제
# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# 존재하는 경우에만 삭제
# 오류 발생 방지
# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)

# 테이블 업데이트
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")


# SQL 주입 방지
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# limit(5개만 출력)
# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# 다른위치에서 시작하여 출력(3번째 부터 시작하여 5개)
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# 테이블 생성
# mycursor.execute("CREATE TABLE users (id VARCHAR(255), name VARCHAR(255), fav VARCHAR(255))")
#mycursor.execute("CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))")

# 생성된 테이블 확인
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)

# sql = "INSERT INTO users (id, name, fav) VALUES (%s, %s, %s)"
# val = [
#   ('1', 'John', '154'),
#   ('2', 'Peter', '154'),
#   ('3', 'Amy', '155'),
#   ('4', 'Hannah', ''),
#   ('5', 'Michael', '')
# ]

# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
#   ('154', 'Chocolate Heaven'),
#   ('155', 'Tasty Lemons'),
#   ('156', 'Vanilla Drams')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# join(양쪽에 값이 있는 것들을 기준으로 병합)
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# LEFT JOIN(왼쪽(name)기준으로 병합)
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#right join(오른쪽(fav-name)기준으로 병합)
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"


# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
