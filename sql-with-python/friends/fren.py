# import sqlite3

# conn = sqlite3.connect("friends.db")
# c = conn.cursor()

# # c.execute(""" CREATE TABLE frens 
# #     (first_name TEXT, last_name TEXT, closeness INTEGER)""")

# c.execute("INSERT INTO frens VALUES ('Bem', 'Okram', 2)")

# conn.commit()
# conn.close()

di = { "apple":1, "banana":2}

for key in di.values():
    print (key)

for k,v in di.items():
    print(k)
    print(v)