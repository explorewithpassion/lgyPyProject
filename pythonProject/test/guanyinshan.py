from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["时代国际幼儿园",'红河幼儿园','小区数量','永川中学新校区','永川体育馆'],[1,1,5,1,1] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="观音山公园附近情况"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("html/观音山.html")
)
make_snapshot(snapshot,c,"html/guanyinshan.png")