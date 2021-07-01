from pyecharts import options as opts
from pyecharts.charts import Pie,Grid
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
gys = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["时代国际幼儿园",'红河幼儿园','小区数量','永川中学新校区','永川体育馆'],[1,1,5,1,1] )],
        center=["50%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="观音山公园附近情况"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

)
snh = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["重庆市机电学校",'小区数量','永川博物馆','幸福广场','碧桂园翡翠湾'],[1,3,1,1,1] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="神女湖附近情况"),
        legend_opts=opts.LegendOpts(pos_right="60%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {c}"))

)
xlh = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["永川协信中心",'永川规划展览馆','金科-中央金街','壹号广场','星光时代广场','小区数量'],[1,1,1,1,1,6] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="兴龙湖附近情况"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {c}"))

)
cqwu = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['金科小型商圈','小区数量'],[1,10] )],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="重庆文理学院红河校区附近情况"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

)
grid = (
    Grid()
    .add(gys, grid_opts=opts.GridOpts(pos_left="55%"))
    .add(snh, grid_opts=opts.GridOpts(pos_right="55%"))
    #.add(xlh, grid_opts=opts.GridOpts(pos_left="55%"))
    #.add(cqwu, grid_opts=opts.GridOpts(pos_left="55%"))
    .render("html/汇总.html")
)
#make_snapshot(snapshot,c,"html/xinglonghu.png")