web: gunicorn app:app
web: bokeh serve --port=5000 --num-procs=0 --allow-websocket-origin="https://adamdolandataincubatorproject.herokuapp.com/" --address=0.0.0.0 --use-xheaders app.py