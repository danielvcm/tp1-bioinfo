import six.moves.urllib.request as urlreq
from six import PY3
import webbrowser
import dash
import dash_bio as dashbio
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = open("input_example.fasta").read()

app.layout = html.Div([
    html.H1("Sequence Alignment", style={'text-align':'center'}),

    dashbio.AlignmentChart(
        id='my-alignment-viewer',
        data=data
    ),
    html.Div(id='alignment-viewer-output')
])


@app.callback(
    dash.dependencies.Output('alignment-viewer-output', 'children'),
    [dash.dependencies.Input('my-alignment-viewer', 'eventDatum')]
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)


if __name__ == '__main__':
    import threading

    webbrowser.open("http://127.0.0.1:8050/", new=2)
    app.run_server(debug=True)



