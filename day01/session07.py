import plotly.express as px

fig = px.scatter(
    x=[1, 2, 3],
    y=[1, 3, 2],
    title="sample figure"
)
fig.show()
