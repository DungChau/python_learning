#!/usr/local/bin/python3

import sqlite3

def main():
	db = Database()
	db.add_record(("david", "dev", 3400))
	db.add_record(("ray", "designer", 2000))

	for row in db.query():
		print(row)

class Database(object):
	"""docstring for Database"""
	def __init__(self):
		super(Database, self).__init__()
		self.conn = sqlite3.connect("db1")
		self.cur = self.conn.cursor()
		self.table = self.cur.execute("create table people (name char(30)," 
									"job char(10), pay int(4))")

	def add_record(self, record):	
		self.cur.execute("insert into people values (?,?,?)", record)
		return self.cur.rowcount

	def query(self):
		self.cur.execute("select * from people")
		return self.cur.fetchall()

if __name__ == '__main__':
	main()