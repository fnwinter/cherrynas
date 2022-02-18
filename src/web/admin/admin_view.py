from flask_classful import FlaskView, route
from flask import render_template, session, redirect

from web.admin.admin_form import AdminForm
from web.database.account_db import Account
from web import DB

class member:
    id = 0
    email = None
    nick_name = None
    joined = False
    permission = 'all'

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

        form_ = AdminForm()

        member_list_ = self.load_member_lists()

        return render_template('/admin/admin.html', email=who, form=form_, member_list=member_list_)

    def post(self):
        member_list_ = self.load_member_lists()

        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"

        form_ = AdminForm()
        if form_.validate_on_submit():
            data = form_['data'].data
            print("data > " + data)

        return render_template('/admin/admin.html', email=who, form=form_, member_list=member_list_)

    def load_member_lists(self):
        member_list_ = []
        result = DB.session.query(Account).all()
        index = 0
        for acount in result:
            member_ = member
            member_.id = index
            member_.email = acount.email
            member_.joined = acount.joined
            member_.nick_name = acount.nick_name
            member_.permission = acount.permission
            member_list_.append(member_)
            index += 1

            member_ = member
            member_.id = index
            member_.email = acount.email
            member_.joined = acount.joined
            member_.nick_name = acount.nick_name
            member_.permission = acount.permission
            member_list_.append(member_)
            index += 1

        return member_list_

    def delete_member(self, list_to_delete):
        pass

    def apply_change(self, member_list):
        pass