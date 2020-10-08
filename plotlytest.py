import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[12, 3, 15, 23, 45]))
fig.write_html('first_figure.html', auto_open=True)