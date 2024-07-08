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
    #Insert   
    def insert_data_registro_insert(self,idUsuario):
        query = "INSERT INTO registro_acceso(tipo_movimiento,timeStamp,id_usuario_registro) VALUES ('Agregar Producto', now(),'"+idUsuario+"')"
        self.cursor.execute(query)
        self.conn.commit()
        
    def insert_data_registro_move(self,idUsuario):
        query = "INSERT INTO registro_acceso(tipo_movimiento,timeStamp,id_usuario_registro) VALUES ('Movimiento', now(),'"+idUsuario+"')"
        self.cursor.execute(query)
        self.conn.commit()
        
    def insert_data_registro_edit(self,idUsuario):
        query = "INSERT INTO registro_acceso(tipo_movimiento,timeStamp,id_usuario_registro) VALUES ('Modificar Producto', now(),'"+idUsuario+"')"
        self.cursor.execute(query)
        self.conn.commit() 
    
    def insert_data_producto_almacen(self,idPro,idAl):
        query = "INSERT INTO producto_almacen(idPro,idAl) VALUES ('"+idPro+"','"+idAl+"')"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data_producto(self,marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cod):
        query = "INSERT INTO producto(marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,codigo) VALUES ('"+marca+"','"+tipo_neumatico+"','"+anchura+"','"+perfil+"','"+radio+"','"+indice_carga+"','"+indice_velocidad+"','"+cod+"')"
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
        
        
    #Read
    def read_data_producto_almacen(self):
        producto_almacen = []
        query = "SELECT marca, tipo_neumatico, indice_carga, indice_velocidad from producto"
        self.cursor.execute(query)
        producto_almacen = self.cursor.fetchall()
        return producto_almacen
    
    def read_data_movimiento(self):
        producto_almacen = []
        query = "SELECT producto.codigo ,producto.marca, almacen.nombre_almacen, almacen.ubicacion from producto join producto_almacen on IdProducto = idPro join almacen on idAlmacen = idAl"
        self.cursor.execute(query)
        producto_almacen = self.cursor.fetchall()
        return producto_almacen
        
    def read_data_producto(self):
        query = "SELECT codigo,marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad FROM producto"
        self.cursor.execute(query)
        return self.cursor.fetchone()
        
    def read_data_user(self, username, password):
        query = "SELECT * FROM usuario WHERE username = '"+username+"' AND clave = '"+password+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_idMovimiento(self, idPro):
        query = "SELECT idMovimiento FROM producto_almacen WHERE idPro = '"+idPro+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_codProducto(self):
        query = "SELECT codigo FROM producto"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_data_nombreAlmacen(self):
        query = "SELECT nombre_almacen FROM almacen"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_data_ultimo_id_producto(self):
        query = "SELECT MAX(idProducto) FROM producto"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_data_ultimo_idMovimiento(self):
        query = "SELECT MAX(idMovimiento) FROM producto_almacen"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_data_Almacen(self):
        almacen = []
        query = "SELECT nombre_almacen,ubicacion,nro_almacen FROM almacen"
        self.cursor.execute(query)
        almacen = self.cursor.fetchall()
        return almacen
    
    def read_data_Almacen_buscador(self,value):
        almacen = []
        self.cursor.execute(f"SELECT nombre_almacen, ubicacion, nro_almacen FROM almacen WHERE nombre_almacen LIKE '%{value}%' ")
        almacen = self.cursor.fetchall()
        return almacen
    
    def read_data_idAlmacen(self, almacen):
        query = "SELECT idAlmacen FROM almacen WHERE nombre_almacen = '"+almacen+"'"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def read_data_idProducto(self, cod):
        query = "SELECT idProducto FROM producto WHERE codigo = '"+cod+"'"
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

    #Update
    def update_data_clave(self,clave1,username):
        query = "UPDATE usuario SET clave = '"+clave1+"' WHERE username = '"+username+"' "
        self.cursor.execute(query)
        self.conn.commit()
    
    def update_data_producto_almacen(self,idPro,idAl):
        query = "UPDATE producto_almacen SET idAl = '"+idAl+"' WHERE idPro = '"+idPro+"' "
        self.cursor.execute(query)
        self.conn.commit()
        
    def update_data_producto(self,marca,tipo_neumatico,anchura,perfil,radio,indice_carga,indice_velocidad,cod):
        query = "UPDATE producto SET marca = '"+marca+"',tipo_neumatico = '"+tipo_neumatico+"',anchura = '"+anchura+"',perfil = '"+perfil+"',radio = '"+radio+"',indice_carga = '"+indice_carga+"',indice_velocidad = '"+indice_velocidad+"' WHERE idProducto = '"+cod+"' "
        self.cursor.execute(query)
        self.conn.commit()

    #Delete
    def delete_data(self, table_name, conditions):
        query = f"DELETE FROM {table_name} WHERE {' AND '.join(conditions)}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()