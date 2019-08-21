from form import AgeForm
from form import legal_or_not
from flask import Flask
from flask import request
from flask import render_template
from form import EmailForm

app = Flask(__name__)

#@app.route('/compratarjeta')
#def compratarjeta():
#    return render_template("compratarjeta.html")

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/compratarjeta', methods=['GET', 'POST'])
def compratarjeta():
    form = EmailForm(request.form)
    no_data=False

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.nombrecompleto.data is not None:
            #print(f"Nombre capturado: {form.nombrecompleto.data}")
            flag = True
            return render_template('finalcompra.html', nombrecompleto=form.nombrecompleto.data)
        else:
           no_data = True
    return render_template('compratarjeta.html', no_data=no_data)


#@app.route('/compratarjeta', methods=['GET','POST'])
#def compratarjeta_url():
#    form=EmailForm(request.form)
#    flag=False
#    if len(form.errors):
#        print(form.errors)
#    if request.method == 'POST':
#        if form.nombrecompleto.data is not None: #and form.direccion.data is not None and form.direccion.data is not None and form.calle.data is not None and form.ciudad.data is not None and form.estado.data is not None and form.codigopostal.data is not None and form.email.data is not None and form.tel.data is not None and form.numerotarjeta.data is not None and form.nombre2.data is not None and form.fecha.data is not None and form.codigoseguridad.data is not None:
#            print(f"Email capturado: {form.nombrecompleto.data}")
#            flag=True
#    return render_template('finalcompra.html',flag=flag)


#@app.route('/form', methods=['GET', 'POST'])
#def form_url():
#        form = AgeForm(request.form)
#        no_data=False
#        if len(form.errors):
#            print(form.errors)
#        if request.method == 'POST':
#            if form.nombrecompleto.data is not None and form.direccion.data is not None and form.direccion.data is not None and form.calle.data is not None and form.ciudad.data is not None and form.estado.data is not None and form.codigopostal.data is not None and form.email.data is not None and form.tel.data is not None and form.numerotarjeta.data is not None and form.nombre2.data is not None and form.fecha.data is not None and form.codigoseguridad.data is not None:
#                                return render_template('success.html',nombrecompleto=form.nombrecompleto.data,legal=legal_or_not(form.age.data))
#            else:
#                no_data= True
#        return render_template('form.html', flag=no_data)


@app.route('/Proteinas')
def proteinas():
    proteinas = {
        'item1': {
            'name': "Isopure",
            'tipo': "Suero de Leche Hidrolizado",
            'cost': 1,
            'cantidad': 2,
            'proteina': 24,
            'aminoacidos': 22,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://images-na.ssl-images-amazon.com/images/I/61v5de%2Blh7L._SY450_.jpg"
        },
        'item2': {
            'name': "100% Standard Whey Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 40,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://gimnasiorizo.files.wordpress.com/2012/11/20121110-192208.jpg"
        },
        'item3': {
            'name': "Nitro Tech",
            'tipo': "Suero de Leche Aislado",
            'cost': 3,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.demusculos.com/sitio/2792-large_default/nitro-tech-4-libras.jpg"
         },
         'item4': {
            'name': "Organcic Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 10,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.costco.com.mx/medias/sys_master/products/h5c/h9b/11215646031902.jpg"
           },
           'item5': {
            'name': "Carnivor",
            'tipo': "Suero de Leche Aislado",
            'cost': 1050,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://zentenoshop.com/709-large_default/mmd-carnivor-mass-6-lbs-proteina-de-carne.jpg"
            },
            'item6': {
            'name': "Syntha-6",
            'tipo': "Suero de Leche Aislado",
            'cost': 105,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.demusculos.com/sitio/722-large_default/syntha-6-bsn.jpg"
             },
             'item7': {
             'name': "MP Combat",
             'tipo': "Suero de Leche Aislado",
             'cost': 150,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://cdn.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/c/o/combat-proteinpowder-musclepharm_1.jpg"
              },
             'item8': {
             'name': "Mass Tech",
             'tipo': "Suero de Leche Aislado",
             'cost': 178,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://cdn.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/m/a/mass-tech-muscletech_1.jpg"
                                                        }
    }
    return render_template("Proteinas.html", proteinas=proteinas)

@app.route('/Aminoacidos')
def aminoacidos():
    aminoacidos = {
        'item1': {
            'name': "Isopure",
            'tipo': "Suero de Leche Hidrolizado",
            'cost': 115,
            'cantidad': 2,
            'proteina': 24,
            'aminoacidos': 22,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.suplementoscdmx.com.mx/wp-content/uploads/2016/08/aminox-bsn-suplemento-deportivo-mexico-df.jpg"
        },
        'item2': {
            'name': "100% Standard Whey Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 1123,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.suplementoscdmx.com.mx/wp-content/uploads/2016/09/best-amino-bpi-aminoacidos-quemadores-grasa.jpg"
        },
        'item3': {
            'name': "Nitro Tech",
            'tipo': "Suero de Leche Aislado",
            'cost': 17955,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://http2.mlstatic.com/bcaa-aminoacidos-suplemento-dietetico-capsulas-por-parker-na-D_NQ_NP_949314-MLM28398750842_102018-F.jpg"
         },
         'item4': {
            'name': "Organcic Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 1458,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://images-na.ssl-images-amazon.com/images/I/619Tkc3E1BL._SX466_.jpg"
           },
           'item5': {
            'name': "Carnivor",
            'tipo': "Suero de Leche Aislado",
            'cost': 1324,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://sc01.alicdn.com/kf/UTB8vcXDAJoSdeJk43Ow761a4XXac/Muscle-Power-Max-Sports-BCAA-Branched-Chain.png_350x350.png"
            },
            'item6': {
            'name': "Syntha-6",
            'tipo': "Suero de Leche Aislado",
            'cost': 1789,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://images-na.ssl-images-amazon.com/images/I/71NpyPqQxpL._SX425_.jpg"
             },
             'item7': {
             'name': "MP Combat",
             'tipo': "Suero de Leche Aislado",
             'cost': 23,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://cdn.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/c/o/combat-proteinpowder-musclepharm_1.jpg"
              },
             'item8': {
             'name': "Mass Tech",
             'tipo': "Suero de Leche Aislado",
             'cost': 17,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://s3.images-iherb.com/unn/unn02702/l/1.jpg"
                                                        }
    }
    return render_template("Aminoacidos.html", aminoacidos=aminoacidos)

@app.route('/Ganadores')
def ganadores():
    ganadores = {
        'item1': {
            'name': "Isopure",
            'tipo': "Suero de Leche Hidrolizado",
            'cost': 1200,
            'cantidad': 2,
            'proteina': 24,
            'aminoacidos': 22,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://cdn.laguiadelasvitaminas.com/wp-content/uploads/2016/07/Serious-Mass.jpg"
        },
        'item2': {
            'name': "100% Standard Whey Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 8,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.vitafuerte.com/wp-content/uploads/2013/05/jeje-300x300.jpg"
        },
        'item3': {
            'name': "Nitro Tech",
            'tipo': "Suero de Leche Aislado",
            'cost': 6,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://d3mtiy808mo6jm.cloudfront.net/wp-content/uploads/2017/04/28175221/cell-tech-muscletech-suplementosfitness-300x300.jpg"
         },
         'item4': {
            'name': "Organcic Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 4,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.walmart.com.mx/images/product-images/img_large/00750302482168l.jpg"
           },
           'item5': {
            'name': "Carnivor",
            'tipo': "Suero de Leche Aislado",
            'cost': 1,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://zentenoshop.com/709-large_default/mmd-carnivor-mass-6-lbs-proteina-de-carne.jpg"
            },
            'item6': {
            'name': "Syntha-6",
            'tipo': "Suero de Leche Aislado",
            'cost': 63,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.demusculos.com/sitio/722-large_default/syntha-6-bsn.jpg"
             },
             'item7': {
             'name': "MP Combat",
             'tipo': "Suero de Leche Aislado",
             'cost': 72,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://cdn.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/c/o/combat-proteinpowder-musclepharm_1.jpg"
              },
             'item8': {
             'name': "Mass Tech",
             'tipo': "Suero de Leche Aislado",
             'cost': 2,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://cdn.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/m/a/mass-tech-muscletech_1.jpg"
                                                        }
    }
    return render_template("Ganadores.html", ganadores=ganadores)

@app.route('/Accesorios')
def accesorios():
    accesorios= {
        'item1': {
            'name': "Isopure",
            'tipo': "Suero de Leche Hidrolizado",
            'cost': 2,
            'cantidad': 2,
            'proteina': 24,
            'aminoacidos': 22,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://www.fitnesas.com.ar/wp-content/uploads/2019/03/Calleras-Quuz-reforzadas-3-254x295.jpg"
        },
        'item2': {
            'name': "100% Standard Whey Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 1,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://i.linio.com/p/aaa8d38d649df2674730ff29a3e232ed-catalog.jpg"
        },
        'item3': {
            'name': "Nitro Tech",
            'tipo': "Suero de Leche Aislado",
            'cost': 4,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://resources.sears.com.mx/medios-plazavip/fotos/productos_sears1/original/2906425.jpg"
         },
         'item4': {
            'name': "Organcic Protein",
            'tipo': "Suero de Leche Aislado",
            'cost': 8,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://m1.paperblog.com/i/165/1658219/i-gym-retomamos-el-deporte-L-DoRkzE.jpeg"
           },
           'item5': {
            'name': "Carnivor",
            'tipo': "Suero de Leche Aislado",
            'cost': 6,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"http://www.bodyargentina.com/wp-content/uploads/2017/08/633.jpg"
            },
            'item6': {
            'name': "Syntha-6",
            'tipo': "Suero de Leche Aislado",
            'cost': 3,
            'cantidad': 2,
            'proteina': 48,
            'aminoacidos': 18,
            'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
            'stock': True,
            'photo':"https://gympro02.akamaized.net/5915-home_default/hand-grip-everlast-25-kg.jpg"
             },
             'item7': {
             'name': "MP Combat",
             'tipo': "Suero de Leche Aislado",
             'cost': 5,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://www.monark.com.pe/wp-content/uploads/02-400-060-MKP_002-600x600.jpg"
              },
             'item8': {
             'name': "Mass Tech",
             'tipo': "Suero de Leche Aislado",
             'cost': 2,
             'cantidad': 2,
             'proteina': 48,
             'aminoacidos': 18,
             'otros': "Glutamina 8 gr, leacina 6 gr, creatina 4 gr, peptidos 2 gr",
             'stock': True,
             'photo':"https://images-na.ssl-images-amazon.com/images/I/71VO%2BuZ1XQL._SX425_.jpg"
                                                        }
    }
    return render_template("accesorios.html", accesorios=accesorios)

@app.route('/entrenamientos')
def entrenamientos():
    return render_template("entrenamientos.html")

@app.route('/finalcompra')
def finalcompra():
    return render_template("finalcompra.html")

@app.route('/compra')
def compra():
    return render_template("compra.html")

@app.route('/contactowhats')
def contactowhats():
    return render_template("contactowhats.html")

@app.route('/dietas')
def dietas():
    return render_template("dietas.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
