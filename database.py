
import pymysql.cursors
def SELECT(id:int, F_1:float, F_2:float, TOT_MIN: float, TOT_MAX:float):
	connect = pymysql.connect(host='eu-cdbr-west-03.cleardb.net',
                             user='bbf5b4dbf0864d',
                             password='ffd3bdd6',
                             db = 'heroku_d6ef91a5f99ed5e',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
	with connect.cursor() as cursor:
		cursor.execute("""show tables""")
		sql = """insert into valleyball (id, F_1, F_2, TOT_MIN, TOT_MAX) value (%s, %s, %s, %s, %s)"""
		val = (id, F_1, F_2, TOT_MIN, TOT_MAX)
		cursor.execute(sql, val)

	connect.commit()
	connect.close()
def UPDATEVOLLEY(TOT_MIN: float, TOT_MAX:float):
	connect = pymysql.connect(host='eu-cdbr-west-03.cleardb.net',
                             user='bbf5b4dbf0864d',
                             password='ffd3bdd6',
                             db = 'heroku_d6ef91a5f99ed5e',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
	with connect.cursor() as cursor:
		cursor.execute("""show tables""")
		sql = """UPDATE valleyball SET TOT_MIN='%s' , TOT_MAX='%s' WHERE id='1'"""
		val = (TOT_MIN, TOT_MAX)
		cursor.execute(sql, val)
		connect.commit()
	connect.close()
def UPDATEBASKET(F_1:float, F_2:float, TOT_MIN: float, TOT_MAX:float):
	connect = pymysql.connect(host='eu-cdbr-west-03.cleardb.net',
                             user='bbf5b4dbf0864d',
                             password='ffd3bdd6',
                             db = 'heroku_d6ef91a5f99ed5e',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
	with connect.cursor() as cursor:
		cursor.execute("""show tables""")
		sql = """UPDATE valleyball SET F_1='%s', F_2='%s', TOT_MIN='%s' , TOT_MAX='%s' WHERE id='2'"""
		val = (F_1, F_2, TOT_MIN, TOT_MAX)
		cursor.execute(sql, val)
		connect.commit()
	connect.close()

def vollinfo():
	connect = pymysql.connect(host='eu-cdbr-west-03.cleardb.net',
                             user='bbf5b4dbf0864d',
                             password='ffd3bdd6',
                             db = 'heroku_d6ef91a5f99ed5e',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
	with connect.cursor() as cursor:
		cursor.execute("""show tables""")
		sql = """SELECT TOT_MIN, TOT_MAX FROM valleyball WHERE id='1'"""
		cursor.execute(sql)
		return(cursor.fetchone())
	connect.close()
def basketinfo():
	connect = pymysql.connect(host='eu-cdbr-west-03.cleardb.net',
                             user='bbf5b4dbf0864d',
                             password='ffd3bdd6',
                             db = 'heroku_d6ef91a5f99ed5e',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
	with connect.cursor() as cursor:
		cursor.execute("""show tables""")
		sql = """SELECT F_1, F_2, TOT_MIN, TOT_MAX FROM valleyball WHERE id='2'"""
		cursor.execute(sql)
		return(cursor.fetchone())
	connect.close()
