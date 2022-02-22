import json

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
        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"

        form_ = AdminForm()
        if form_.validate_on_submit():
            data = form_['data'].data
            print(data)
            json_ = json.loads(data)
            if json_.get('action') == 'delete':
                self.delete_member(json_.get('member'))
            if json_.get('action') == 'apply':
                self.apply_change(json_)

        member_list_ = self.load_member_lists()
        return render_template('/admin/admin.html', email=who, form=form_, member_list=member_list_)

    def load_member_lists(self):
        member_list_ = []
        result = DB.session.query(Account).all()
        for account in result:
            member_ = member()
            member_.email = account.email
            member_.joined = account.joined
            member_.nick_name = account.nick_name
            member_.permission = account.permission
            member_list_.append(member_)
        return member_list_

    def delete_member(self, list_to_delete):
        try:
            DB.session.query(Account).filter_by(email=f"{list_to_delete}").delete()
            DB.session.commit()
        except Exception as e:
            print(e)

    def apply_change(self, json_):
        update_item = json_.get('changes')
        try:
            for item in update_item:
                email_ = item.get('email')
                permission_ = item.get('permission')
                joined_ = item.get('joined')
                DB.session.query(Account).filter_by(email=f"{email_}").update({'permission': permission_, 'joined':joined_})
                DB.session.commit()
        except Exception as e:
            print(e)
