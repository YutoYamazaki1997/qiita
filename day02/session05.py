import plotly.graph_objects as go
# 極座標の描画
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
# のdataパラメータのものは渡すことができる。
data = go.Scatterpolar(
    r=[1, 2, 3],
    theta=[90, 180, 270],
    mode="markers",
)
fig = go.Figure(
    data=data
)
fig.write_image("2-5.png")
fig.show()
