import plotly.graph_objects as go
data = go.Scatter(
    x=[1, 2, 3],
    y=[1, 3, 2]
)
fig = go.Figure(
    data=data,
)
fig.write_image("day03/pic/3-01.png")
fig.show()
