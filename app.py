import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = 'ROI Dashboard'
# added
server.secret_key = os.environ.get('secret_key', 'secret')
