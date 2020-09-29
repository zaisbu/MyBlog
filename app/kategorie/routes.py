import datetime
import os

from flask import render_template, request, redirect, url_for, flash, app
from app import db
from app.kategorie import bp
from app.blog.form import Blogform
from app.kategorie.form import Kategorieform
from app.models import Blog, Kategorie

app.secret_key = "huerefuck"

@bp.route('/kategorie/overview')
def kategorie():
    return render_template('kategorie/uebersicht.html', items=Kategorie.query.all())


@bp.route('/kategorie/detail/<int:id>')
def kategorie_detail(id):
    kategorie = Kategorie.query.get_or_404(id)
    return render_template('kategorie/kategorie.html', kategorie=kategorie)


@bp.route('/kategorie/remove/<int:id>')
def kategorie_remove(id):
    kategorie = Kategorie.query.get_or_404(id)
    db.session.delete(kategorie)
    db.session.commit()
    flash("Kategorie wurde gelöscht.")
    return redirect(url_for('kategorie.index'))

@bp.route('/kategorie/create')
def kategorie_create():
    form = Kategorieform(request.form)
    return render_template('kategorie/erstellen.html', form=form)


@bp.route('/kategorie/create', methods=['POST'])
def kategorie_create_post():
    form = Kategorieform(request.form)
    if form.validate():
        kategorie = Kategorie()
        kategorie.name = form.name.data
        db.session.add(kategorie)
        db.session.commit()
        return redirect(url_for('kategorie.kategorie'))
    return render_template('kategorie/erstellen.html', form=form)

@bp.route('/kategorie/update/<int:id>')
def kategorie_update_get(id):
    kategorie = Kategorie.query.get_or_404(id)
    form = Kategorieform(request.form)
    form.kategorie.data = kategorie.name
    return render_template('kategorie/update_kategorie.html', form=form)


@bp.route('/kategorie/update/<int:id>', methods=['POST'])
def kategorie_update_post(id):
    form = Kategorieform(request.form)
    if form.validate():
        kategorie = Kategorie.query.get_or_404(id)
        kategorie.id = form.kategorie_id.data
        kategorie.name = form.kategorie.data
        db.session.add(kategorie)
        db.session.commit()
        return redirect(url_for('kategorie.kategorie_detail', id=kategorie.id))
    return render_template('kategorie/update_kategorie.html', form=form)
