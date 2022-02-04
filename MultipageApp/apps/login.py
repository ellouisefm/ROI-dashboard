# import os
# os.chdir(r'C:\Users\emendoza\Documents\DSP\Python Programming\Python Day 5\MultipageApp')

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input,State
from app import app # connect to the app.py file
# from app import server
# from apps import roi_page
# from dash.exceptions import PreventUpdate
# import dash_auth
# from apps import roi_page

# app = dash.Dash(__name__)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        dcc.Input(id="user", type="text", placeholder="Enter Username",className="inputbox1",
        style={'margin-left':'35%','width':'450px','height':'45px','padding':'10px','margin-top':'60px',
        'font-size':'16px','border-width':'3px','border-color':'#a0a3a2'
    }),
    ),
    html.Div(
        dcc.Input(id="passw", type="text", placeholder="Enter Password",className="inputbox2",
        style={'margin-left':'35%','width':'450px','height':'45px','padding':'10px','margin-top':'10px',
        'font-size':'16px','border-width':'3px','border-color':'#a0a3a2',
    }),
    ),
    html.Div(
        html.A(html.Button('Verify', className = 'verify', n_clicks=0, style={'border-width':'3px','font-size':'14px'}),
        style={'margin-left':'45%','padding-top':'30px'},  href='/apps/roi_page')
        ),
    # html.Div(id='output1'),
    html.Div(id='page-content', children=[])
])

# dcc.Link(
#     html.Button('Navigate to "page-2"'),
#     href='/page2')


@app.callback(
    Output('page-content', 'children'),
    # Output('output1', 'children'),
    [Input('url', 'pathname')],
   # [State('user', 'value'),
   #  State('passw', 'value')]
   )

def display_page(pathname):#, uname, passw):
    # li={'admin':'password'}
    if pathname == '/apps/roi_page':
        pass
    # if (pathname == '/apps/roi_page') & (li[uname]==passw):
    #     return roi_page.get_dashboard_layout()
    # elif (pathname == '/apps/roi_page') & (uname =='' or uname == None or passw =='' or passw == None):
    #      return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    # elif (pathname == '/apps/roi_page') & (uname not in li):
    #     return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    else:
        return "fail"
        # return html.Div(children='Incorrect Password',style={'padding-left':'550px','padding-top':'40px',
        #                                                             'font-size':'16px'})
             


# def display_page(pathname, uname, passw):
#     li={'admin':'password'}
#     if (pathname == '/apps/roi_page') & (li[uname]==passw):
#         return roi_page.get_dashboard_layout()
#     elif (pathname == '/apps/roi_page') & (uname =='' or uname == None or passw =='' or passw == None):
#          return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
#     elif (pathname == '/apps/roi_page') & (uname not in li):
#         return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
#     else:
#         return html.Div(children='Incorrect Password',style={'padding-left':'550px','padding-top':'40px',
#                                                                    'font-size':'16px'})

# def update_output(n_clicks, uname, passw):
    # li={'admin':'password'}
    # # if uname =='' or uname == None or passw =='' or passw == None:
    # #     return html.Div(children='',style={'padding-left':'550px','padding-top':'10px'})
    # # elif uname not in li:
    # #     return html.Div(children='Incorrect Username',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    # if (li[uname]==passw) & n_clicks:
    #     pathname = 
    #     access_grant = html.Div(dcc.Link('Access Granted!', href='/apps/roi_page',
    #                               style={'color':'#183d22','font-family': 'serif', 'font-weight': 'bold', 
    #                                     "text-decoration": "none",'font-size':'20px'}),
    #                     style={'padding-left':'605px','padding-top':'40px'}) 
    #     return []
    #     return access_grant
    #     return access_grant, dcc.Location(pathname="/apps/index", id="url")
    
    # else:
    #     return html.Div(children='Incorrect Password',style={'padding-left':'550px','padding-top':'40px',
    #                                                           'font-size':'16px'})


# if __name__ == '__main__':
#     app.run_server()