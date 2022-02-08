import os
os.chdir(r'C:\Users\emendoza\Desktop\multipageapp\MultipageApp\MultipageApp')

# import packages
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sqlite3
import pandas as pd
# from app.py, apps folder
from app import app, server
from apps import roi_page

# current page layout
app.layout = html.Div([
    # for the url of the page
    dcc.Location(id='url', refresh=False),
    # for the page contents
    html.Div(id='page'),
    html.Div(id='page2'),
    html.Div(id='page3')
])
# index page elements
index_page = html.Div([
    html.Div([html.H1('Hello Again!')], 
             style={'textAlign': 'center','color': '#595959','fontSize':24, 
                    'font-family':'calibri','margin-top':'120px'}
             ),
    html.Div('Please enter your credentials to access the ROI dashboard.',
             style={'textAlign': 'center','color': '#999999','fontSize':14, 
                    'font-family':'calibri','margin-top':'2px'}
             ),
    html.Div(
    dcc.Input(id="user", type="text", placeholder="Username",className="unamebox",
              style={'margin-left':'40%','width':'300px','height':'45px',
                     'padding':'10px','margin-top':'20px','font-size':'16px',
                     'border-width':'3px','border-color':'#f5f5f5','borderRadius':5}
              ),
    ),
    html.Div(
    dcc.Input(id="passw", type="password", placeholder="Password",className="pwordbox",
              style={'margin-left':'40%','width':'300px','height':'45px',
                     'padding':'10px','margin-top':'10px','font-size':'16px',
                     'border-width':'3px','border-color':'#f5f5f5','borderRadius':5}
              ),
    ),
    html.Div(
    html.Button('LOG IN', id='login', n_clicks=0, 
                style={'border-width':'3px','font-size':'14px',
                       'background-color': '#007bff','borderRadius':5,
                       'color': 'white','border-color':'#f5f5f5',
                       'width':'260px','height':'45px',}),
                style={'margin-left':'41.5%','padding-top':'30px'}),
    html.Div([dcc.Input(id='submitmode', value = 0)], 
             style={'display':'none'}
             )
    ])

# ERROR index page elements
err_index_page = html.Div([
    html.Div([html.H1('Hello Again!')], 
             style={'textAlign': 'center','color': '#595959','fontSize':24, 
                    'font-family':'calibri','margin-top':'120px'}
             ),
    html.Div('Please enter your credentials to access the ROI dashboard.',
             style={'textAlign': 'center','color': '#999999','fontSize':14, 
                    'font-family':'calibri','margin-top':'2px'}
             ),
    html.Div('Incorrect USERNAME / PASSWORD. Please try again.',id="errormsg",
              style={'textAlign': 'center','color': '#d0312d','fontSize':14, 
                    'font-family':'calibri','margin-top':'3px'}
              ),
    html.Div(
    dcc.Input(id="user", type="text", placeholder="Username",className="unamebox",
              style={'margin-left':'40%','width':'300px','height':'45px',
                     'padding':'10px','margin-top':'20px','font-size':'16px',
                     'border-width':'3px','border-color':'#f5f5f5','borderRadius':5}
              ),
    ),
    html.Div(
    dcc.Input(id="passw", type="password", placeholder="Password",className="pwordbox",
              style={'margin-left':'40%','width':'300px','height':'45px',
                     'padding':'10px','margin-top':'10px','font-size':'16px',
                     'border-width':'3px','border-color':'#f5f5f5','borderRadius':5}
              ),
    ),
    html.Div(
    html.Button('LOG IN', id='login', n_clicks=0, 
                style={'border-width':'3px','font-size':'14px',
                       'background-color': '#007bff','borderRadius':5,
                       'color': 'white','border-color':'#f5f5f5',
                       'width':'260px','height':'45px',}),
                style={'margin-left':'41.5%','padding-top':'30px'}),
    html.Div([dcc.Input(id='submitmode', value = 0)], 
             style={'display':'none'}
             )
    ])

logout_btn = html.Div([
        html.Div(id='hiUser', style = {'color':'white', 'margin-left':'2%', 'margin-top':'2px', 
                                                    'width':'30%','display':'inline-block', 'font-size':'20px'}),
        html.A(
            html.Button('Logout', className = 'logout_btn',
                        style = {'color':'black', 'background-color':'rgb(211,211,211)', 
                                'margin-left':'58%','margin-top':'4px','height':'30px',
                                'borderRadius':5,'border-color':'#f5f5f5'
                                }),
            href='/logout',
            ),
        # dcc.Store(id='hiUsermemory', storage_type='local')
    ], style = {'background-color':'rgb(0,123,255)', 'width':'100%', 'height':40}
    )

# callback for username and password
@app.callback(
   Output('url', 'pathname'),
   Input('login', 'n_clicks'),
   [State('user', 'value'),
    State('passw', 'value')]
)
def update_output(n_clicks, uname, passw):
    # added for user_mgt
    conn = sqlite3.connect('user_management.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_mgt;")
    data = pd.DataFrame(cur.fetchall())
    data.columns=['uname','passw','id']#
    data = data.drop(columns=['id'])#
    users_data = data.set_index('uname').T.to_dict('rows')
    li = users_data[0]

    # li={'admin':'password', 'edcanoy':'eddyson', 'elmend':'ellouise'}
    if uname =='' or uname == None or passw =='' or passw == None:
        return '/'
    elif uname not in li:
        return '/error'
    elif li[uname]==passw:
        return '/roi-dashboard'
    else:
        return '/'

# callback for page contents
@app.callback(
    [Output('page', 'children'),
     Output('page2', 'children'),
     Output('page3', 'children')
     ],
    [Input('url', 'pathname')],
)
def display_page(pathname):
    if pathname == '/':
        return index_page, "", ""
    elif pathname == '/roi-dashboard':
        return "",logout_btn, roi_page.get_dashboard_layout()
    elif pathname == '/error':
        return "", "", err_index_page
    elif pathname == '/logout':
        return index_page, "", ""
    else:
        return index_page, "", ""

# hi user
# @app.callback(
#     Output('hiUsermemory', 'data'),
#     [Input('login', 'n_clicks')],
#     [State('user', 'value')])
# def save_memory(login, user):
#     print(user)
#     if login > 0:
#         print(user)
#         hiUsermemory = user
#         print(hiUsermemory)
#         return hiUsermemory

# @app.callback(
#     [Output('hiUser', 'children')],
#     [Input('url', 'pathname')],
#     [State('hiUsermemory','data')]
#     )
# def load_memory(pathname, hiUsermemory):
#     if pathname == '/roi-dashboard':
#         hiUser_txt = "Hi, "+str(hiUsermemory)
#         print(hiUser_txt)
#     return [hiUser_txt]


if __name__ == '__main__':
    app.run_server()
