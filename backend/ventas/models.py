from django.db import models

# Create your models here.

class Region(models.Model):
    idRegion =models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
    	db_table = 'harrys_region'

class Provincia(models.Model):
    idProvincia =models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
    	db_table = 'harrys_provincia'

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='id_provincia')

    # def __init__(self,id,codigo=None,nombre=None,fCreacion=None,provincia=None):
    #     self.fCreacion = fCreacion
    #     if (provincia != None):
    #         self.provincia=provincia
    #         self.idComuna=id
    #         self.codigo=codigo
    #         self.nombre=nombre

    def __str__(self):
        return self.nombre

    class Meta:
    	db_table = 'harrys_comuna'

class Genero(models.Model):
    idGenero  = models.AutoField( primary_key=True,db_column='id_genero')
    codigo = models.CharField(max_length=10)
    nombre     = models.CharField(max_length=20, blank=False, null=False,db_column='genero')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    # def __init__(self,id,codigo=None,genero=None):
    #     self.idGenero=id
    #     self.codigo=codigo
    #     self.genero=genero

    def __str__(self):
        return self.genero
    
    class Meta:
    	db_table = 'harrys_genero'


class Persona(models.Model):
    rut    = models.IntegerField( primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    papellido = models.CharField(max_length=30, blank=True, null=True)
    sapellido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=False)
    fechaNacimiento = models.DateField(auto_now_add=True, blank=True, null=True,db_column='fecha_nacimiento')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    genero        = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    activo = models.IntegerField(blank=True, null=True)  

    # def __init__(self,rut,dv,nombre,papellido,sapellido,email,fechaNacimiento,comuna,genero):
    #     self.rut = rut
    #     self.dv = dv
    #     self.nombre = nombre
    #     self.papellido = papellido
    #     self.sapellido = sapellido
    #     self.email = email
    #     self.fechaNacimiento = fechaNacimiento
    #     print("comuna1:",comuna.idComuna)
    #     #self.comuna = comuna
    #     print("comuna2:",comuna)
    #     #self.genero = genero


   
    def __str__(self):
        return str(self.rut)+", "+ self.nombre + ", "+str(self.activo)
    
    class Meta:
    	db_table = 'harrys_persona'




class FormaPago(models.Model): 
    idFPago = models.IntegerField(null=False, primary_key=True,db_column='codFormaPago')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200, null=False,db_column='descripcion')
    
    def __str__(self):
        return self.descripcion
    class Meta:
    	db_table = 'harrys_formapago'


def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.rut, filename )


class Cliente(models.Model):    
    rut    = models.OneToOneField(Persona, models.DO_NOTHING, primary_key=True,db_column='rut')
    foto             = models.ImageField(upload_to=cargarFoto, null=True)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    credito = models.IntegerField(blank=True, null=True,default=0)  
    
    # def __str__(self):
    #     return self.rut+", "+ self.nombre+", "+str(self.edad)+", "\
    #            +str(self.id_genero)+", "+str(self.fecha_nacimiento)+", "+str(self.activo)

    class Meta:
    	db_table = 'harrys_cliente'


class Sucursal(models.Model):
    idSucursal =models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre=models.CharField(max_length=100,  null=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,default=0, db_column='id_comuna',null=True)
    direccion = models.TextField(default=0)
    fCreacion =  models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.direccion

    class Meta:
    	db_table = 'harrys_sucursal'



class Cargo(models.Model): #steve
    idCargo = models.IntegerField(null=False, primary_key=True, db_column='codCargo')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'harrys_cargo'

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)  
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    codCargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    sueldo = models.IntegerField(null=False)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.rut
    
    class Meta:
    	db_table = 'harrys_empleado'

#verbose_name
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    usuario=models.CharField(unique=True,max_length=20, null=False)
    clave=models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.usuario

    class Meta:
    	db_table = 'harrys_usuario'  
#################################################################
#verbose_name
class Color(models.Model):
    idColor = models.AutoField(primary_key=True, db_column='id')

    color=models.CharField(unique=True,max_length=20, verbose_name='Color', null=False)
    rgb=models.CharField(max_length=10, verbose_name='Paleta_RGB', null=False)
    hex=models.CharField(max_length=10,verbose_name='Paleta_Hex', null=False)
    def __str__(self):
        return self.color

    class Meta:
    	db_table = 'harrys_color'    

#################################################################
class ViewCliente(models.Model):
    rut = models.IntegerField( primary_key=True)
    dv=models.CharField(max_length=1, verbose_name='Color', null=False)
    nombre=models.CharField(max_length=20, verbose_name='Color', null=False)
    papellido=models.CharField(max_length=20, verbose_name='Color', null=False)
    sapellido=models.CharField(max_length=20, verbose_name='Color', null=False)
    email=models.CharField(max_length=20, verbose_name='Color', null=False)
    genero        = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero')
    comuna        = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna')
    usuario=models.CharField(max_length=20, verbose_name='Color', null=False)

    class Meta:
    	db_table = 'view_cliente'    
"""
drop view view_cliente;
CREATE VIEW view_cliente 
as 
select cl.rut 
       ,pe.dv
       ,pe.nombre
	   ,pe.papellido
	   ,pe.sapellido
	   ,pe.email
	   ,pe.id_genero as genero
	   ,pe.id_comuna as comuna
	   ,us.usuario
from harrys_cliente cl
    ,harrys_persona pe
	left join harrys_usuario us on us.rut = pe.rut
where pe.rut = cl.rut
  
"""          

class Productos(models.Model):
    idProd =models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=100)
    imagen_sb = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    desc_corta = models.CharField(max_length=100)
    cant_favoritos = models.IntegerField(blank=True, null=True)  
    cant_vistos = models.IntegerField(blank=True, null=True)  
    precio = models.IntegerField(blank=True, null=True)  
    class Meta:
    	db_table = 'harrys_productos'
