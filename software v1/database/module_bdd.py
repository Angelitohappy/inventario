import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='ruedas_mundial'
        )
        self.cursor = self.conn.cursor()

    def insert_data_producto(self,marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cantidad):
        query = "INSERT INTO producto(marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cantidad) VALUES ('"+marca+"','"+tipo_neumatico+"','"+anchura+"','"+perfil+"','"+radio+"','"+indice_carga+"','"+indice_velocidad+"','"+cantidad+"')"
        self.cursor.execute(query)
        self.conn.commit()
        
    def insert_data_alamcen(self,nombre,ubicacion,nro):
        query = "INSERT INTO almacen(nombre_almacen,ubicacion,nro_almacen) VALUES ('"+nombre+"','"+ubicacion+"','"+nro+"')"
        self.cursor.execute(query)
        self.conn.commit()
        
    def insert_data_usuario(self,id,name,user,email,phone,password,address,face):
        query = "INSERT INTO usuario(cedula,nombre,username,tipo_usuario,correo,telefono,direccion,clave,face) VALUES ('"+id+"','"+name+"','"+user+"','Usuario','"+email+"','"+phone+"','"+address+"','"+password+"','"+face+"')"
        self.cursor.execute(query)
        self.conn.commit()
        
    def read_data_producto_almacen(self):
        producto_almacen = []
        query = "SELECT producto.marca, producto.tipo_neumatico, producto.indice_carga, producto.indice_velocidad, almacen.nombre_almacen, almacen.ubicacion from producto INNER JOIN almacen on producto.idProducto=almacen.idAlmacen"
        self.cursor.execute(query)
        producto_almacen = self.cursor.fetchall()
        return producto_almacen
        
    def read_data_producto(self):
        query = "SELECT marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cantidad FROM producto"
        self.cursor.execute(query)
        return self.cursor.fetchone()
        
    def read_data_user(self, username, password):
        query = "SELECT * FROM usuario WHERE username = '"+username+"' AND clave = '"+password+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_nombreAlmacen(self):
        query = "SELECT nombre_almacen FROM almacen"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_Almacen(self):
        almacen = []
        query = "SELECT nombre_almacen,ubicacion,nro_almacen FROM almacen"
        self.cursor.execute(query)
        almacen = self.cursor.fetchall()
        return almacen
    
    def read_data_idAlmacen(self, almacen):
        query = "SELECT idAlmacen FROM almacen WHERE nombre_almacen = '"+almacen+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_email(self, username):
        query = "SELECT correo FROM usuario WHERE username = '"+username+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_id(self, username):
        query = "SELECT idUsuario FROM usuario WHERE username = '"+username+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update_data_clave(self,clave1,username):
        query = "UPDATE usuario SET clave = '"+clave1+"' WHERE username = '"+username+"' "
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, conditions):
        query = f"DELETE FROM {table_name} WHERE {' AND '.join(conditions)}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()