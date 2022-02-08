# ROI Dashboard

This repository contain source code for ROI Dashboard, a multipage application created using Plotly Dash. 

## Running the app

In order to run the app locally, you'll need to install [Plotly Dash](https://dash.plot.ly/installation) and its dependencies. Once you've installed Dash and it's dependencies, run the following line of code in your terminal:

```
python index.py
```

## Dash Code Structure

```
plotly-dash-multipage-template
│   index.py
|   app.py
|   mydatastore.csv
│
└───apps
│   │   dashboard.py
|   |   dashboard2.py
│   
└───assets
│   │   main.css
│   │   gtag.js
```

The main app runs from index.py in the top-level folder and pairs alongside required files for a Plotly Dash app. Currently, the architecture is set up to run from one main file, index.py, and will house a navigation and callbacks with/to other dashboards within the /apps/ folder.

## Data

Currently, this file structure uses a blank csv and the dashboard is built from that datastore.

## Deployment

To deploy, you can run it locally or set up Heroku via the [instructions linked here](https://dash.plot.ly/deployment).

## Useful Links

* [Plotly Dash Documentation](https://dash.plot.ly/)
* [Plotly Multi-Page Documentation](https://dash.plot.ly/urls)
