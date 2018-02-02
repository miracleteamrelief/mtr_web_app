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
app.add_url_rule('/about', view_func=base.AboutView.as_view('about'))
app.add_url_rule('/signup', view_func=base.SignupView.as_view('signup'))
app.add_url_rule('/login', view_func=base.LoginView.as_view('login'))
app.add_url_rule('/donate', view_func=base.DonateView.as_view('donate'))
app.add_url_rule('/needs', view_func=base.NeedsView.as_view('needs'))
app.add_url_rule('/contributors', view_func=base.ContributorsView.as_view('contributors'))
app.add_url_rule('/resources', view_func=base.ResourcesView.as_view('resources'))
app.add_url_rule('/resources/volunteers', view_func=base.ResourcesVolunteersView.as_view('resources-volunteers'))
app.add_url_rule('/resources/vehicles', view_func=base.ResourcesVehiclesView.as_view('resources-vehicles'))
app.add_url_rule('/resources/supplies', view_func=base.ResourcesSuppliesView.as_view('resources-supplies'))
app.add_url_rule('/collaborators', view_func=base.CollaboratorsView.as_view('collaborators'))
app.add_url_rule('/collaborators/shelters', view_func=base.CollaboratorsSheltersView.as_view('collaborators-shelters'))
app.add_url_rule('/collaborators/distribution_centers', view_func=base.CollaboratorsDistributionCentersView.as_view('collaborators-distribution_centers'))
app.add_url_rule('/collaborators/teams', view_func=base.CollaboratorsTeamsView.as_view('collaborators-teams'))
app.add_url_rule('/collaborators/liaisons', view_func=base.CollaboratorsLiaisonsView.as_view('collaborators-liaison'))
app.add_url_rule('/events', view_func=base.EventsView.as_view('events'))
