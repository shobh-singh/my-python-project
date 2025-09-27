import pymysql

# Step 1: MySQL se connect hona
conn = pymysql.connect(
    host="localhost",        # hamesha string
    user="root",             # apna MySQL username
    password="6376361029@Vss", # apna MySQL password 
    database="Teacher"       # apna database
)

cursor = conn.cursor()

# ---------------- CREATE (Insert) ----------------
cursor.execute("INSERT INTO student1 (id, name, age) VALUES (%s, %s, %s)", (1, "Vikram", 18))
cursor.execute("INSERT INTO student1 (id, name, age) VALUES (%s, %s, %s)", (2, "Rohit", 20))
conn.commit()
print("✅ Records inserted")

# ---------------- READ (Select) ----------------
cursor.execute("SELECT * FROM student1")
rows = cursor.fetchall()
print("\n📌 Person Table Data (READ):")
for row in rows:
    print(row)

# ---------------- UPDATE ----------------
cursor.execute("UPDATE student1 SET age=%s WHERE id=%s", (21, 2))
conn.commit()
print("\n✏️ Record updated (Rohit age = 21)")

# ---------------- READ again ----------------
cursor.execute("SELECT * FROM student1")
rows = cursor.fetchall()
print("\n📌 Person Table Data After Update:")
for row in rows:
    print(row)

# ---------------- DELETE ----------------
cursor.execute("DELETE FROM student1 WHERE id=%s", (1,))
conn.commit()
print("\n🗑️ Record with id=1 deleted")

# ---------------- READ again ----------------
cursor.execute("SELECT * FROM student1")
rows = cursor.fetchall()
print("\n📌 Person Table Data After Delete:")
for row in rows:
    print(row)

# Step 4: Connection close
cursor.close()
conn.close()



