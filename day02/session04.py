import plotly.graph_objects as go
x = [0, 0, 0, 1, 2, 2, 3, 3, 3, 3, 3]
data = go.Histogram(
    x=x
)
fig = go.Figure(
    data=data,
)
fig.write_image("2-4.png")
fig.show()
