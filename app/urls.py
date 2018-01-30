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
app.add_url_rule('/signup', view_func=base.SignupView.as_view('signup'))
app.add_url_rule('/login', view_func=base.LoginView.as_view('login'))
app.add_url_rule('/donate', view_func=base.DonateView.as_view('donate'))
app.add_url_rule('/needs', view_func=base.NeedsView.as_view('needs'))
app.add_url_rule('/volunteers', view_func=base.VolunteersView.as_view('volunteers'))
app.add_url_rule('/contributors', view_func=base.ContributorsView.as_view('contributors'))
app.add_url_rule('/resources', view_func=base.ResourcesView.as_view('resources'))
app.add_url_rule('/collaborators', view_func=base.CollaboratorsView.as_view('collaborators'))
app.add_url_rule('/teams', view_func=base.TeamsView.as_view('teams'))
app.add_url_rule('/liaison', view_func=base.LiaisonView.as_view('liaison'))
app.add_url_rule('/events', view_func=base.EventsView.as_view('events'))
