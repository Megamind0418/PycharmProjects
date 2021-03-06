from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_

# from app.forms.book import DriftForm
# from app.libs.email import send_mail
# from app.libs.enums import PendingStatus
# from app.models.base import db
# from app.models.drift import Drift
# from app.models.gift import Gift
# from app.models.user import User
# from app.models.wish import Wish
# from app.view_models.book import BookViewModel
# from app.view_models.drift import DriftCollection
from . import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    pass


@web.route('/pending')
@login_required
def pending():
    pass


@web.route('/drift/<int:did>/reject')
@login_required
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
@login_required
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
@login_required
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    pass
