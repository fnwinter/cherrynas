from flask import session

def get_id() -> str:
    who = None
    if session.get('nick_name'):
        who = f"{session.get('nick_name')}"
    elif session.get('email'):
        who = f"{session.get('email')}"
    return who
