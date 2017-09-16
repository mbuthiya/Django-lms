from . import main
from flask import render_template

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('errors/fourOwfour.html'),404

@main.app_errorhandler(500)
def five_hundred(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('errors/five_hundred.html'),500
