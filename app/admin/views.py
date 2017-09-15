from . import admin

@admin.route('/dashboard/newLesson',methods = ['GET','POST'])
def newLesson():
    
