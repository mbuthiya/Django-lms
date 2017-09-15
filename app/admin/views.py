from . import admin
from flask import render_template,redirect,url_for
from .forms import CreateLesson

@admin.route('/dashboard/newLesson',methods = ['GET','POST'])
def newLesson():
    form = CreateLesson()
    if form.validate_on_submit():
        title =form.title.data
        days = form.days.data
        body = form.body.data

        return redirect(url_for('main.index'))



    return render_template('admin/newLesson.html',form = form)
