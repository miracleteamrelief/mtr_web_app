from datetime import timedelta
from flask import Flask, session
from views import base
from config import app_cfg

app                             = Flask(__name__)
app.config.update({
    'SECRET_KEY'                : app_cfg[('FLASK', 'secret_key')],
    'EXPLAIN_TEMPLATE_LOADING'  : True,
    'TEMPLATES_AUTO_RELOAD'     : True})
app.permanent_session_lifetime  = timedelta(
    minutes=int(app_cfg[('FLASK', 'session_lifetime')]))

##############################################################################
# Main resolvers
##############################################################################
app.add_url_rule('/', view_func=base.IndexView.as_view('index'))