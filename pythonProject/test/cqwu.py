from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['金科小型商圈','小区数量'],[1,10] )],
        center=["30%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="文理学院红河校区附近情况"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("html/重庆文理学院.html")
)
make_snapshot(snapshot,c,"html/cqwu.png")