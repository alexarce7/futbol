import web
# @
db = web.database(dbn='mysql', db='futbol', user='root', pw='utec')

user=raw_input("ingrese su usuario\n")
passw=raw_input("ingrese la contrasena\n")
result=db.select("usuarios")
dbuser=""
dbPass=""
for row in result:
    dbuser=row.nombre
    dbPass=row.password