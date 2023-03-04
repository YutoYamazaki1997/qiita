import plotly.graph_objects as go
data = go.Scatter(
    # ここにデータを書く
)

layout = go.Layout(
    # ここにレイアウトを書く
)
fig = go.Figure(
    data=data,
    layout=layout
)

fig.show()
