import numpy
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
student=pd.read_excel("Student.xlsx",sheet_name="data",engine="openpyxl",dtype=str)
#乘坐过自动驾驶公交车的学生
rideStudent_yes=student.loc[(student['是否乘坐'])=="是"]
rideStudent_no=student.loc[(student['是否乘坐'])=="否"]
#出行方式
didi=student.loc[(student['主要出行方式']=="滴滴")]
taxi=student.loc[(student['主要出行方式']=="出租车")]
gjc=student.loc[(student['主要出行方式']=="公交车")]
apollo=student.loc[(student['主要出行方式']=="自动驾驶公交车")]
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['滴滴','私家车','公交车','自动驾驶公交车'],[len(didi),len(taxi),len(gjc),len(apollo)])],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="学校调研对象主要出行方式"),
        legend_opts=opts.LegendOpts(pos_left="23%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("studenthtml/ride_method.html")
)
#是否愿意体验
student_yy=student.loc[(student['是否愿意体验']=='愿意')]
student_byy=student.loc[(student['是否愿意体验']=='不愿意')]
student_fcyy=student.loc[(student['是否愿意体验']=='非常愿意')]
location=["不愿意","愿意","非常愿意"]
values=[len(student_byy),len(student_yy),len(student_fcyy)]
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
    .render("studenthtml/exper.html")
)
##乘坐目的
# list=student["乘坐目的"].values
# print(list)
# print('公园' in list[0])
goPark=student.loc[student['乘坐目的'].str.contains('公园',na=False)]
work=student.loc[student['乘坐目的'].str.contains('办事',na=False)]
buyVege=student.loc[student['乘坐目的'].str.contains('买菜',na=False)]
goSchool=student.loc[student['乘坐目的'].str.contains('上学',na=False)]
other=student.loc[student['乘坐目的'].str.contains('其他',na=False)]
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['公园游玩','附近办事','买菜','上学','其他'],[len(goPark),len(work),len(buyVege),len(goSchool),len(other)])],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="在乘坐过自动驾驶公交车的同学的乘坐目的"
                                  ,title_textstyle_opts=opts.TextStyleOpts(font_size=15)),
        legend_opts=opts.LegendOpts(pos_left="35%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("studenthtml/rideGoal.html")
)
#print(len(goPark))
# print(goSchool)
# print(buyVege)
# print(goSchool)
# print(other)
#乘坐频率
oneMonth=student[(student["乘坐频率"]=="一月一次")]
oneThreeMonth=student[(student["乘坐频率"]=="三月一次")]
oneWeek=student[(student["乘坐频率"]=="一周一次")]
Other=student[(student["乘坐频率"]=="其他")]
c = (
    Bar()
    .add_xaxis(['三月一次','一月一次','一周一次','其他'])
    .add_yaxis("同学", [len(oneMonth),len(oneThreeMonth),len(oneWeek),len(other)])
    .set_global_opts(title_opts=opts.TitleOpts(title="乘坐频率", subtitle=""))
    .render("studenthtml/frequency.html")
)
##自动驾驶和普通公交车的比较
rideStudent_yes=student.loc[(student['是否乘坐'])=="是"]
rideStudent1=rideStudent_yes["自动普通比较"]
string=[]
beforCompare=[[],[],[],[],[],[]]

for i in rideStudent1:
    j=i.split("|")
    string.append(j)

for i in string:
    for j in range(6):
        beforCompare[j].append(i[j])
compare=pd.DataFrame({
    "空间":beforCompare[0],
    "速度":beforCompare[1],
    "总体":beforCompare[2],
    "智能":beforCompare[3],
    "外观":beforCompare[4],
    "服务":beforCompare[5]
})
# print(compare)
apollo_space=compare.loc[(compare["空间"]=="自动驾驶公交车")]
normal_space=compare.loc[(compare["空间"]=="普通公交车")]
len(compare["空间"])
apollo_speed=compare.loc[(compare["速度"]=="自动驾驶公交车")]
normal_speed=compare.loc[(compare["速度"]=="普通公交车")]
len(compare["速度"])
apollo_total=compare.loc[(compare["总体"]=="自动驾驶公交车")]
normal_total=compare.loc[(compare["总体"]=="普通公交车")]
len(compare["总体"])
apollo_intelligence=compare.loc[(compare["智能"]=="自动驾驶公交车")]
normal_intelligence=compare.loc[(compare["智能"]=="普通公交车")]
len(compare["智能"])
apollo_beauity=compare.loc[(compare["外观"]=="自动驾驶公交车")]
normal_beauity=compare.loc[(compare["外观"]=="普通公交车")]
len(compare["外观"])
apollo_service=compare.loc[(compare["服务"]=="自动驾驶公交车")]
normal_service=compare.loc[(compare["服务"]=="普通公交车")]
len(compare["服务"])
list1=[
    {"value": len(apollo_space), "percent": len(apollo_space) / len(compare["空间"])},
    {"value": len(apollo_speed), "percent": len(apollo_speed) / len(compare["速度"])},
    {"value": len(apollo_total), "percent": len(apollo_total) / len(compare["总体"])},
    {"value": len(apollo_intelligence), "percent": len(apollo_intelligence) / len(compare["智能"])},
    {"value": len(apollo_beauity), "percent": len(apollo_beauity) / len(compare["外观"])},
    {"value": len(apollo_service), "percent": len(apollo_service) / len(compare["服务"])}
]
list2=[
    {"value": len(normal_space), "percent": len(normal_space) / len(compare["空间"])},
    {"value": len(normal_speed), "percent": len(normal_speed) / len(compare["速度"])},
    {"value": len(normal_total), "percent": len(normal_total) / len(compare["总体"])},
    {"value": len(normal_intelligence), "percent": len(normal_intelligence) / len(compare["智能"])},
    {"value": len(normal_beauity), "percent": len(normal_beauity) / len(compare["外观"])},
    {"value": len(normal_service), "percent": len(normal_service) / len(compare["服务"])}
]
c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["安全", "空间", "总体",'智能','外观','服务'])
    .add_yaxis("自动驾驶公交车", list1, stack="stack1", category_gap="50%")
    .add_yaxis("普通公交车", list2, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="自动驾驶公交车和普通公交车在各个指标的比较",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=15))
    )
    .render("studenthtml/compare_percent.html")
)