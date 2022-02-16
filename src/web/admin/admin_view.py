from flask_classful import FlaskView, route
from flask import render_template, session, redirect

from web.admin.admin_form import AdminForm

class AdminView(FlaskView):
    """
    Admin Page
    """
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        """
        admin.html
        """
        is_admin = session.get('admin')
        if is_admin != 'yes':
            redirect('/')

        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"

        _form = AdminForm()

        if _form.validate_on_submit():
            data = _form['data'].data
            print(data)

        return render_template('/admin/admin.html', email=who, form=_form)

    def post(self):
        _form = AdminForm()

        return render_template('/admin/admin.html', form=_form)
