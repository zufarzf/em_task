from datetime import datetime, timezone
from flask import render_template, session, redirect, url_for
from .. import main_module
from ..forms import *






@main_module.route('/login')
def login():
    form = LoginForm()

    if session.get('record_id') is None:
        if record_id and record_id != 0:
            session['record_id'] = record_id
            record = LaboratoryRecords.query.get(record_id)
            record.start_exam = datetime.now(timezone.utc)
        elif not record_id:
            give_flash(True, 'На приёме нет пациента.')
            return redirect(url_for('laboratory.patients_queue'))
    elif session.get('record_id') != record_id:
        give_flash(False, 'Для приёма следующего пациента завершите или отмените текущий приём!')
        return redirect(url_for('laboratory.appointment', record_id=session.get('record_id')))

    return render_template(
        'staff/med_accounts/laboratory/laboratory_exam.html',
        employee_id = session.get('this_employee_id'),
        record_id = session.get('record_id'),
        form = form)
