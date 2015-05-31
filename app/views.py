from flask import session, request, flash, url_for, redirect, render_template, abort, g
from app import app, db, models
from app  import login_manager, login_user , logout_user , current_user , login_required
from models import User , Cuidados , Veterinario
from forms import CuidadosForm, VeterinarioForm

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    nombreusuario = request.form['nombreusuario']
    contrasena = request.form['contrasena']
    registered_user = User.query.filter_by(nombreusuario=nombreusuario,contrasena=contrasena).first()
    if registered_user is None:
        return redirect(url_for('login'))
    if registered_user.nombreusuario == 'berta':
	login_user(registered_user)
	return redirect(request.args.get('next') or url_for('index'))
    login_user(registered_user)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/')
@login_required
def index():
    return render_template('menu.html', usuario=User.query.filter_by(id = g.user.id).all())

@app.route('/streaming')
def streaming():
    return render_template('streaming.html')

@app.route('/enconstruccion')
def enconstruccion():
    return render_template('enconstruccion.html')

@app.route('/cuidadosadmin', methods=['GET', 'POST'])
def cuidadosadmin():
    form = CuidadosForm()

    if request.method == 'POST':
      if form.validate() == False:
        return render_template('cuidadosadmin.html',form=form)
      else:
        nuevocuidado = Cuidados(form.nombrecuidador.data, form.nombrecomidadura.data, form.nombrecomidablanda.data, form.pautasalimentacion.data, form.tipohigiene.data, form.pautashigiene.data)
        db.session.add(nuevocuidado)
        db.session.commit()
        flash("Cuidados guardados")
        return redirect(url_for('cuidadosadmin'))

    elif request.method == 'GET':
      return render_template('cuidadosadmin.html', form=form)


@app.route('/cuidadosusuario')
def cuidadosusuario():
    return render_template('cuidadosusuario.html', cuid = Cuidados.query.all())

@app.route('/primerosauxadmin', methods=['GET', 'POST'])
def primerosauxadmin():
    form = VeterinarioForm()

    if request.method == 'POST':
      if form.validate() == False:
        return render_template('primerosauxadmin.html',form=form)
      else:
 	nuevoveterinario = Veterinario(form.nombreveterinario.data, form.tlfnoveterinario.data, form.tlfnourgencias.data, form.direccionveterinario.data, form.emailveterinario.data)
        db.session.add(nuevoveterinario)
        db.session.commit()
        flash("Cuidados guardados")
        return redirect(url_for('primerosauxadmin'))

    elif request.method == 'GET':
      return render_template('primerosauxadmin.html', form=form)

@app.route('/primerosauxusuario')
def primerosauxusuario():
    return render_template('primerosauxusuario.html', prim = Veterinario.query.all())
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500 

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = current_user


