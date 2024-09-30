import pymysql

class Database:
    def connect(self):

        return pymysql.connect(host='localhost', user='root', password='', database="db_kelompok5")

    def create(self,data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO vcd(title, stock, price, description, image, genre) VALUES (%s, %s, %s, %s, %s, %s)', (data['title'], data['stock'], data['price'], data['description'], data['image'], data['genre'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM vcd')
            else:
                cursor.execute('SELECT * FROM vcd where id = %s',(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readImage(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT image FROM vcd where id = %s',(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('UPDATE vcd SET title = %s, stock = %s, price = %s, description = %s, image = %s, genre = %s WHERE id = %s', (data['title'], data['stock'], data['price'], data['description'], data['image'], data['genre'], id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('DELETE FROM vcd WHERE id = %s',(id))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def checkUser(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user WHERE email = %s', (str(data['email']),))
            if len(cursor.fetchall()) == 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()

    def checkLogin(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (data['email'], data['password']),)
            if len(cursor.fetchall()) != 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()

    def readUser(self, email):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user WHERE email = %s',(email,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readUserEmail(self, email):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if email == None:
                cursor.execute('SELECT * FROM user')
            else:
                cursor.execute('SELECT * FROM user WHERE email = %s',(email,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readRole(self, email):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT role FROM user WHERE email = %s',(email,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ()
        except:
            return ()
        finally:
            con.close()

    def selectTitle(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT title FROM vcd WHERE id = %s',(id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ()
        except:
            return ()
        finally:
            con.close()

    def getPrice(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT price FROM vcd WHERE id = %s',(id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ()
        except:
            return ()
        finally:
            con.close()

    def getImage(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT image FROM vcd WHERE id = %s',(id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ()
        except:
            return ()
        finally:
            con.close()

    def getUsername(self, email):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT name FROM user WHERE email = %s',(email,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return ()
        except:
            return ()
        finally:
            con.close()

    def makeTransaction(self,title,price,name,image,date,email,id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO transaksi(email, customer_name, vcd_id, vcd, date, price, image, active) VALUES (%s, %s, %s, %s, %s, %s, %s, true)', (email, name, id, title, date, price, image,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def deleteTransaction(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('DELETE FROM transaksi WHERE transaction_id = %s',(id))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def getStock(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT stock FROM vcd WHERE id = %s', (id,))
            stock = cursor.fetchone()[0]  # Fetch the stock value
            return stock
        except Exception as e:
            print(f"Error in getStock: {e}")
            return None
        finally:
            con.close()

    def stockUpdate(self, id, stock):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('UPDATE vcd SET stock = %s WHERE id = %s', (stock, id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def readUserTransaction(self, email):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM transaksi where email = %s AND active = true',(email,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def readTransaction(self):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM transaksi')
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def stockUpdate(self, id, stock):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('UPDATE vcd SET stock = %s WHERE id = %s', (stock, id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def getVcdId(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT vcd_id FROM transaksi where transaction_id = %s',(id,))
            return cursor.fetchone()
        except:
            return ()
        finally:
            con.close()

    def returnTransaction(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('UPDATE transaksi SET active = false WHERE transaction_id = %s', (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()