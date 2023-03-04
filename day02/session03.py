import plotly.graph_objects as go
data = go.Bar(
    x=["斎藤", "田中", "鈴木"],
    y=[100, 87, 60]
)
fig = go.Figure(
    data=data,
)
fig.write_image("2-03.png")
fig.show()
