import plotly.graph_objects as go

data = go.Pie(
    labels=["A型", "O型", "B型", "AB型"],
    values=[4500, 2500, 1053, 500]
)
fig = go.Figure(
    data=data
)
fig.show()
