import sqlite3

conn = sqlite3.connect("data.sqlite")
cur = conn.cursor()

def get_entrys(date):
    cur.execute("""
    select 
    Amount, Firstname, Lastname, Street, Housenummer, Citycode, City, IBAN, Email
    from Dueto
    inner join People on People.ID  = Dueto.Personid
    inner join Bankdata on Bankdata.Personid  = Dueto.Personid
    inner join Person_Address_Match on Person_Address_Match.Personid = Dueto.Personid
    inner join Addresses on Addresses.ID = Person_Address_Match.Addressid
    where Duedate = (?)
    """, (date,))
    return cur.fetchall()


def close():
    cur.close()
    conn.close()