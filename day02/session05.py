import plotly.graph_objects as go
data = go.Scatterpolar(
    r=[1, 2, 3],
    theta=[90, 180, 270],
    mode="markers",
)
fig = go.Figure(
    data=data
)

fig.show()
