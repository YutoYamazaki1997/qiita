import plotly.graph_objects as go
data = go.Scatter(
    x=[1, 2, 3],
    y=[1, 3, 2]
)

layout = go.Layout(
    title="test"
)
fig = go.Figure(
    data=data,
    layout=layout
)

fig.show()
