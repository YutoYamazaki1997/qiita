import plotly.graph_objects as go
data = go.Scatter(
    x=[1, 2, 3],
    y=[1, 3, 2]
)

layout = go.Layout(
    # タイトルの文字設定を細かく指定
    title=dict(
        text="test",
        font=dict(
            size=26,
            color="grey",
        )
    ),
    # 凡例を消す
    showlegend=True,
)
fig = go.Figure(
    data=data,
    layout=layout
)

fig.show()
