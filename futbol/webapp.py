import web
from web import form

db = web.database(dbn='mysql', db='futbol', user='root', pw='utec')
render=web.template.render('templates')
urls = (
    '/', 'login'
    ,'/index','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)

myformLogin = form.Form( 
    form.Textbox("Usuario"), 
    form.Password("Password")
    )

myformFutbol=form.Form(
    form.Textbox("Equipo"),
    form.Textbox("PJ"), 
    form.Textbox("Pts"),
    form.Textbox("TG"), 
    form.Textbox("GF"), 
    form.Textbox("GC"),
)
class login:
    def GET(self):
        form = myformLogin()
        
        return render.login(form)
    
    def POST(self): 
        form = myformLogin()
        if not form.validates(): 
            return render.login(form)
        else: 
            result=db.select("usuarios")
            dbuser=""
            dbPass=""
            for row in result:
                dbuser=row.nombre
                dbPass=row.password

            if dbuser==form.d.Usuario and dbPass==form.d.Password:
                raise web.seeother("/index")
            else:
                 return render.error(form)


class index:
    def GET(self):
        
        result=db.select('equipos')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew= myformFutbol()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformFutbol()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('equipos', nombre_eq=formNew.d.Equipo,partidosj=formNew.d.PJ,
            puntos=formNew.d.Pts,tgoles=formNew.d.TG,
            golesf=formNew.d.GF,golesc=formNew.d.GC,)
            raise web.seeother('/index')
            
class editar:
    def GET(self,id_equipo):
        formEdit=myformFutbol()
        
        result=db.select('equipos', where= "id_equipo=%s"%(id_equipo))
        
        for row in result:
            formEdit['Equipo'].value=row.nombre_eq
            formEdit['PJ'].value=row.partidosj
            formEdit['Pts'].value=row.puntos
            formEdit['TG'].value=row.tgoles
            formEdit['GF'].value=row.golesf
            formEdit['GC'].value=row.golesc
        return render.editar(formEdit)  

    def POST(self,id_equipo):
        formEdit=myformFutbol()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('equipos', where="id_equipo=%s"%(id_equipo), 
            nombre_eq=formEdit.d.Equipo,partidosj=formEdit.d.PJ,
            puntos=formEdit.d.Pts,tgoles=formEdit.d.TG,
            golesf=formEdit.d.GF,golesc=formEdit.d.GC)
            result=db.select('equipos')
            raise web.seeother('/index')
class eliminar:
    def GET(self,id_equipo):
        formEdit=myformFutbol()
        
        result=db.select('equipos', where= "id_equipo=%s"%(id_equipo))
        
        for row in result:
            formEdit['Equipo'].value=row.nombre_eq
            formEdit['PJ'].value=row.partidosj
            formEdit['Pts'].value=row.puntos
            formEdit['TG'].value=row.tgoles
            formEdit['GF'].value=row.golesf
            formEdit['GC'].value=row.golesc
        return render.eliminar(formEdit)        
    def POST(self,id_equipo):
        formEdit=myformFutbol()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('equipos', where="id_equipo=%s"%(id_equipo))
            raise web.seeother('/index')
class ver:
    def GET(self,id_equipo):
        
        result=db.select('equipos', where="id_equipo=%s"%(id_equipo))
        return render.ver(result)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()