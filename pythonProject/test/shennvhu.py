from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["重庆市机电学校",'小区数量','永川博物馆','幸福广场','碧桂园翡翠湾'],[1,3,1,1,1] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="神女湖附近情况"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {c}"))
    .render("html/神女湖.html")
)
make_snapshot(snapshot,c,"html/shennvhu.png")