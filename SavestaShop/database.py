import sqlite3

def gen_custID():
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    cur.execute("UPDATE metadata SET custnum = custnum + 1")
    conn.commit()
    custnum = str([i for i in cur.execute("SELECT custnum FROM metadata")][0][0])
    conn.close()
    id = "ID"+"0"*(7-len(custnum))+custnum
    return id

def gen_sellID():
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    cur.execute("UPDATE metadata SET sellnum = sellnum + 1")
    conn.commit()
    sellnum = str([i for i in cur.execute("SELECT sellnum FROM metadata")][0][0])
    conn.close()
    id = "SID"+"0"*(7-len(sellnum))+sellnum
    return id

def gen_prodID():
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    cur.execute("UPDATE metadata SET prodnum = prodnum + 1")
    conn.commit()
    prodnum = str([i for i in cur.execute("SELECT prodnum FROM metadata")][0][0])
    conn.close()
    id = "PID"+"0"*(7-len(prodnum))+prodnum
    return id

def gen_orderID():
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    cur.execute("UPDATE metadata SET ordernum = ordernum + 1")
    conn.commit()
    ordernum = str([i for i in cur.execute("SELECT ordernum FROM metadata")][0][0])
    conn.close()
    id = "OID"+"0"*(7-len(ordernum))+ ordernum
    return id


def add_user(data):
    conn = sqlite3.connect("SavestaShop/database.db"")
    cur = conn.cursor()
    email = data["email"]
    if data['type']=="Customer":
        a = cur.execute("SELECT * FROM customer WHERE email=?", (email,))
    elif data['type']=="Seller":
        a = cur.execute("SELECT * FROM seller WHERE email=?", (email,))
    if len(list(a))!=0:
        return False
    tup = ( data["name"],
            data["email"],
            data["phone"],
            data["area"],
            data["locality"],
            data["city"],
            data["state"],
            data["country"],
            data["zip"],
            data["password"])
    if data['type']=="Customer":
        cur.execute("INSERT INTO customer VALUES (?,?,?,?,?,?,?,?,?,?,?)",(gen_custID(), *tup))
    elif data['type']=="Seller":
        cur.execute("INSERT INTO seller VALUES (?,?,?,?,?,?,?,?,?,?,?)", (gen_sellID(), *tup))
    conn.commit()
    conn.close()
    return True

def auth_user(data):
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    type = data["type"]
    email = data["email"]
    password = data["password"]
    if type=="Customer":
        a = cur.execute("SELECT custID, name FROM customer WHERE email=? AND password=?", (email, password))
    elif type=="Seller":
        a = cur.execute("SELECT sellID, name FROM seller WHERE email=? AND password=?", (email, password))
    a = list(a)
    conn.close()
    if len(a)==0:
        return False
    return a[0]

def check_psswd(psswd, userid, type):
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    if type=="Customer":
        a = cur.execute("SELECT password FROM customer WHERE custID=?", (userid,))
    elif type=="Seller":
        a = cur.execute("SELECT password FROM seller WHERE sellID=?", (userid,))
    real_psswd = list(a)[0][0]
    conn.close()
    return psswd==real_psswd

def set_psswd(psswd, userid, type):
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    if type=="Customer":
        a = cur.execute("UPDATE customer SET password=? WHERE custID=?", (psswd, userid))
    elif type=="Seller":
        a = cur.execute("UPDATE seller SET password=? WHERE sellID=?", (psswd, userid))
    conn.commit()
    conn.close()

def check_psswd(psswd, userid, type):
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    if type=="Customer":
        a = cur.execute("SELECT password FROM customer WHERE custID=?", (userid,))
    elif type=="Seller":
        a = cur.execute("SELECT password FROM seller WHERE sellID=?", (userid,))
    real_psswd = list(a)[0][0]
    conn.close()
    return psswd==real_psswd

def set_psswd(psswd, userid, type):
    conn = sqlite3.connect("SavestaShop/database.db")
    cur = conn.cursor()
    if type=="Customer":
        a = cur.execute("UPDATE customer SET password=? WHERE custID=?", (psswd, userid))
    elif type=="Seller":
        a = cur.execute("UPDATE seller SET password=? WHERE sellID=?", (psswd, userid))
    conn.commit()
    conn.close()