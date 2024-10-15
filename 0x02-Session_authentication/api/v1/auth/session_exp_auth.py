#!/usr/bin/env python3
"""
SessionExpAuth
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth
    """
    session_duration = 0

    def __init__(self):
        """init
        """
        try:
            duration = int(getenv('SESSION_DURATION'))
            self.session_duration = duration
        except TypeError:
            pass

    def create_session(self, user_id=None):
        """create_session
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id_for_session_id
        """
        user = super().user_id_for_session_id(session_id)
        if not user:
            return None
        if not user.get('created_at'):
            return None
        if self.session_duration <= 0:
            return user["user_id"]

        time = user["created_at"] + timedelta(seconds=self.session_duration)
        if time < datetime.now():
            return None
        return user["user_id"]
