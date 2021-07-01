from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["永川协信中心",'永川规划展览馆','金科-中央金街','壹号广场','星光时代广场','小区数量'],[1,1,1,1,1,6] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="兴龙湖附近情况"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {c}"))
    .render("html/兴龙湖.html")
)
make_snapshot(snapshot,c,"html/xinglonghu.png")