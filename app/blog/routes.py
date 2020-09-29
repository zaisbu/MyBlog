import datetime
import os

from flask import render_template, request, redirect, url_for, flash, app
from app import db
from app.blog import bp
from app.blog.form import Blogform
from app.models import Blog, Kategorie

app.secret_key = "huerefuck"

@bp.route('/')
def index():
    return render_template('blog/index.html', items=Blog.query.limit(3).all())

@bp.route('/blog/blogs')
def blogs():
    return render_template('blog/blogs.html', items=Blog.query.all())

@bp.route('/blog/entries/<int:id>')
def entries(id):
    blog = Blog.query.filter_by(kategorie_id=id)
    flash("Diese Kateogire enthält folgende Blogeinträge.")
    return render_template('blog/entries.html', items=blog)


@bp.route('/blog/detail/<int:id>')
def blog_detail(id):
    blog = Blog.query.get_or_404(id)
    return render_template('blog/blog.html', blog=blog)


@bp.route('/blog/remove/<int:id>')
def blog_remove(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('blog.index'))

@bp.route('/blog/erstellen')
def blog_erstellen():
    form = Blogform(request.form)
    kategorie = Kategorie.query.all()
    return render_template('blog/erstellen.html', form=form, kategorie=kategorie)


@bp.route('/blog/erstellen', methods=['POST'])
def blog_erstellen_post():
    flash("Blog-Eintrag wurde erstellt.")
    form = Blogform(request.form)
    if form.validate():
        blog = Blog()
        blog.titel = form.blogtitel.data
        blog.kategorie_id = form.kategorie.data
        blog.text = form.text.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog.blogs'))
    return render_template('blog/blogs.html', form=form)

@bp.route('/blog/update/<int:id>')
def blog_update_get(id):
    flash("Blog-Eintrag wurde geladen.")
    blog = Blog.query.get_or_404(id)
    form = Blogform(request.form)
    form.blogtitel.data = blog.titel
    form.kategorie.data = blog.kategorie_id
    form.text.data = blog.text
    return render_template('blog/update_blog.html', form=form, kategorie=Kategorie.query.all())


@bp.route('/blog/update/<int:id>', methods=['POST'])
def blog_update_post(id):
    flash("Blog-Eintrag wurde aktualisiert.")
    form = Blogform(request.form)
    if form.validate():
        blog = Blog.query.get_or_404(id)
        blog.titel = form.blogtitel.data
        blog.kategorie_id = form.kategorie.data
        blog.text = form.text.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog.blog_detail', id=blog.id))
    return render_template('blog/update_blog.html', form=form,  kategorie=Kategorie.query.all())
