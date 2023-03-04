import plotly.graph_objects as go
fig = go.Figure(
    data=go.Scatter(x=[1, 2, 3], y=[1, 3, 2])
)
fig.show()
