import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()

# cursor.execute("""
#     create table doctor (
#         id text,
#         name text,
#         password text
#         )""")

# cursor.execute("""
#     create table patient (
#         id text,
#         name text,
#         password text
#         )""")

# cursor.execute("""
#     insert into doctor values ("191-45042", "karim", "admin")
# """)

# cursor.execute("""
#     insert into patient values ("192-65443", "Roni", "admin")
# """)

# cursor.execute("""
#     create table patientDetails (
#         ID text,
#         Name text,
#         BloodGroup text,
#         Phone text,
#         Height text,
#         Weight int,
#         CurrentAdd text,
#         PermanentAdd text
#         )""")

# cursor.execute("""
#     insert into patientDetails values ("192-65443", "Roni", "A+", "01954342323", "6'02", 80, "Mirkadim Munshiganj Dhaka","Mirkadim Munshiganj Dhaka")
# """)


cursor.execute("""
    select * from patientDetails
""")
print(cursor.fetchall())

conn.commit()
conn.close()
