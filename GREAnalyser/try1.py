import cx_Oracle
import sys

connection = cx_Oracle.connect("piyush/piyushchaudhari@localhost")

cursor = connection.cursor()
# # cursor.execute("create table puks(name varchar(20))")
# cursor.execute("select *from tab")
# for row in cursor:
#     print(row[0])

pref1 = "\'Massachusetts Institute of Technology (MIT)\'"
# q1 = f' select * from student_gre where university_name = {pref1}'
# q1 = f'CREATE VIEW pref_uni35 AS SELECT preference1, preference2, preference3, GRE_SCORE FROM student_gre'
# print(q1)

# query1 = f'-- select preference1, GRE_SCORE from pref_uni35 where preference1 = {pref1}'
# l = list(cursor.execute(query1))
# p = []
# import statistics as st
# o =  [ p.append(i[1])  for i in l]
# o =  [ p.append(i[1])  for i in l]
# o =  [ p.append(i[1])  for i in l]
#
# print(p)
# print(l)
# for r in cursor:
#     print(r)
# count = len(list(cursor.execute(query1)))
# print(count)
insertUniName = 'JIUU678'
insertUniWRank = 5656
insertUniCountry = 'gfhfg'
queryInsert = f'insert into university_list values(\'{insertUniName}\',{insertUniWRank},\'{insertUniCountry}\')'

# print(queryInsert)
# dic = {'insertUniName' : 'JIUU678', 'insertUniWRank' : 5656, 'insertUniCountry' : 'JIUU678'}
# gh = 'insert into university_list(university_name, world_rank, country) values(:insertUniName, :insertUniWRank, :insertUniCountry)'
# cursor.execute(queryInsert)
# cursor.execute("INSERT INTO university_list VALUES (%s, %i, %s)", (insertUniName, insertUniWRank, insertUniCountry))
# cursor.commit()
# print(cursor)
sql = 'insert into university_list values(:insertUniName, :insertUniWRank, :insertUniCountry)'
cursor.execute(sql, insertUniName = 'JIUU678',insertUniWRank = 5656, insertUniCountry = 'gfhfg' )
