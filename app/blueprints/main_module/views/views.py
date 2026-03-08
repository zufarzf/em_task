from datetime import datetime, timezone
from flask import render_template, session, redirect, url_for
from .. import main_module
from ..forms import LoginForm






@main_module.route('/')
@main_module.route('/login')
def login():
    form = LoginForm()

    return render_template(
        'login.html',
        form = form,
    )
