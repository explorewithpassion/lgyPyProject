import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid, Bar, PictorialBar
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType, SymbolType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
#获取数据
park=pd.read_excel("调研数据.xlsx",sheet_name="data1",engine="openpyxl",dtype=str)
#print(park)
##出行方式分类
didi=park.loc[(park['出行方式']=="滴滴")]
car=park.loc[(park['出行方式']=="私家车")]
gjc=park.loc[(park['出行方式']=="公交车")]
##年龄阶段饼状图
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['滴滴','私家车','公交车'],[len(didi),len(car),len(gjc)])],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="公园调研对象主要出行方式"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("html/ride_method.html")
)

##年龄段
park['年龄']=park['年龄'].astype("int")
junior=park.loc[(park['年龄']>=18)&(park['年龄']<=34)]
middle_age=park.loc[(park['年龄']>=35)&(park['年龄']<=50)]
ederly=park.loc[(park['年龄']>=51)]
##各个年龄阶段出行方式百分比柱状图
junior_didi=junior.loc[(junior['出行方式']=='滴滴')]
junior_car=junior.loc[(junior['出行方式']=='私家车')]
junior_gjc=junior.loc[(junior['出行方式']=='公交车')]
list1=[
    {"value": len(junior_didi), "percent": len(junior_didi) / len(didi)},
    {"value": len(junior_car), "percent": len(junior_car) / len(car)},
    {"value": len(junior_gjc), "percent": len(junior_gjc) / len(gjc)},
]
middle_age_didi=middle_age.loc[(middle_age['出行方式']=='滴滴')]
middle_age_car=middle_age.loc[(middle_age['出行方式']=='私家车')]
middle_age_gjc=middle_age.loc[(middle_age['出行方式']=='公交车')]

list2 = [
    {"value": len(middle_age_didi), "percent": len(middle_age_didi )/ len(didi)},
    {"value": len(middle_age_car), "percent": len(middle_age_car )/ len(car)},
    {"value": len(middle_age_gjc), "percent": len(middle_age_gjc )/ len(gjc)},
]
ederly_didi=ederly.loc[(ederly['出行方式']=='滴滴')]
ederly_car=ederly.loc[(ederly['出行方式']=='私家车')]
ederly_gjc=ederly.loc[(ederly['出行方式']=='公交车')]
list3 = [
    {"value": len(ederly_didi), "percent": len(ederly_didi) / len(didi)},
    {"value": len(ederly_car), "percent": len(ederly_car) / len(car)},
    {"value": len(ederly_gjc), "percent": len(ederly_gjc) / len(gjc)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["滴滴", "私家车", "公交车"])
    .add_yaxis("青年人", list1, stack="stack1", category_gap="50%")
    .add_yaxis("中年人", list2, stack="stack1", category_gap="50%")
    .add_yaxis("老年人", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同年龄阶段的出行方式")
    )
    .render("html/ride_method_percent.html")
)

##未乘坐原因分类
no_method=park.loc[(park['未乘坐原因']=="不知道乘坐方式")]
no_site=park.loc[(park['未乘坐原因']=="不知道乘坐地点")]
no_require=park.loc[(park['未乘坐原因']=="没有需求")]
no_interest=park.loc[(park['未乘坐原因']=="不感兴趣")]
l1 = (
    Liquid()
    .add("no_method", [len(no_method)/len(park)], center=["31%", "38%"],label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),)
    .set_global_opts(title_opts=opts.TitleOpts(title="不知道乘坐方式",pos_left=360))
)

l2 = (
    Liquid()
    .add("no_site", [len(no_site)/len(park)], center=["11%", "38%"],label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不知道乘坐地点",pos_left=80),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
)
l3 = (
    Liquid()
    .add("no_require", [len(no_require)/len(park)], center=["51%", "38%"],label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="没有乘坐的需求",pos_left=660)
    )
)
l4 = (
    Liquid()
    .add("no_interest", [len(no_interest)/len(park)], center=["71%", "38%"],label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不感兴趣",pos_left=940),
    )
)
grid = Grid(init_opts=opts.InitOpts(width="1400px")).add(l1, grid_opts=opts.GridOpts())\
    .add(l2, grid_opts=opts.GridOpts())\
    .add(l3, grid_opts=opts.GridOpts())\
     .add(l4, grid_opts=opts.GridOpts())
grid.render("html/reason.html")
#是否乘坐
ride_yes=park.loc[(park['是否乘坐']=="是")]
ride_no=park.loc[(park['是否乘坐']=="否")]
#是否愿意体验
exper_yy=park.loc[(park['是否愿意体验']=="愿意")]
exper_fcyy=park.loc[(park['是否愿意体验']=="非常愿意")]
exper_byy=park.loc[(park['是否愿意体验']=="不愿意")]
location=["不愿意","愿意","非常愿意"]
values=[len(exper_byy),len(exper_yy),len(exper_fcyy)]
c = (
    PictorialBar()
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=True),
        symbol_size=25,
        symbol_repeat="fixed",
        symbol_offset=[1, 2],
        is_symbol_clip=True,
        symbol=SymbolType.DIAMOND,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="是否愿意体验自动驾驶公交车"),
        xaxis_opts=opts.AxisOpts(is_show=True),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=3)
            ),
            axislabel_opts=opts.LabelOpts(font_size=20)
        ),
    )
    .render("html/exper.html")
)
#是否了解
konw_yes=park.loc[(park['是否了解']=="是")]
konw_no=park.loc[(park['是否了解']=="否")]
