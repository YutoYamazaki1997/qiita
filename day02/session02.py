import plotly.graph_objects as go
data = go.Scatter3d(
    x=[1, 2, 3],
    y=[1, 3, 2],
    z=[5, 4, 3]
)
fig = go.Figure(
    data=data,
)
fig.show()
