##汇总所有数据图表到一个页面
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid, Bar, PictorialBar, Page
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType, SymbolType
park=pd.read_excel("调研数据.xlsx",sheet_name="data1",engine="openpyxl",dtype=str)
student=pd.read_excel("Student.xlsx",sheet_name="data",engine="openpyxl",dtype=str)
##出行方式汇总
didi=park.loc[(park['出行方式']=="滴滴")]
car=park.loc[(park['出行方式']=="私家车")]
gjc=park.loc[(park['出行方式']=="公交车")]

Sdidi=student.loc[(student['主要出行方式']=="滴滴")]
Staxi=student.loc[(student['主要出行方式']=="出租车")]
Sgjc=student.loc[(student['主要出行方式']=="公交车")]
Sapollo=student.loc[(student['主要出行方式']=="自动驾驶公交车")]
def park_ride_method() -> Bar:
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(['滴滴', '私家车', '公交车'], [len(didi), len(car), len(gjc)])],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="公园调研对象主要出行方式",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            legend_opts=opts.LegendOpts(orient="vertical",pos_top="15%", pos_left="2%",item_width=38,item_height=24,textstyle_opts=opts.TextStyleOpts(font_size=20)),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",font_size=20))

    )
    return c

def student_ride_method() ->Bar:
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(['滴滴', '私家车', '公交车', '自动驾驶公交车'], [len(Sdidi), len(Staxi), len(Sgjc), len(Sapollo)])],
            center=["35%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="学校调研对象主要出行方式占比",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            legend_opts=opts.LegendOpts(pos_left="38%",item_width=38,item_height=24,textstyle_opts=opts.TextStyleOpts(font_size=20)),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",font_size=20))

    )
    return c

#公园年龄阶段分布
park['年龄']=park['年龄'].astype("int")
junior=park.loc[(park['年龄']>=18)&(park['年龄']<=34)]
middle_age=park.loc[(park['年龄']>=35)&(park['年龄']<=50)]
ederly=park.loc[(park['年龄']>=51)]
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
def park_age_classification() ->Bar:
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
                font_size=22
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="不同年龄阶段的出行方式",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 18)),
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=22),item_width=37,item_height=24),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 18)),
        )

    )
    return c

#公园调研未乘坐原因分类
no_method=park.loc[(park['未乘坐原因']=="不知道乘坐方式")]
no_site=park.loc[(park['未乘坐原因']=="不知道乘坐地点")]
no_require=park.loc[(park['未乘坐原因']=="没有需求")]
no_interest=park.loc[(park['未乘坐原因']=="不感兴趣")]

def park_reason1() ->Grid:
    l1 = (
        Liquid()
            .add("no_method", [len(no_method) / len(park)], center=["31%", "38%"], label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ), )
            .set_global_opts(title_opts=opts.TitleOpts(title="不知道乘坐方式", pos_left=360,title_textstyle_opts=opts.TextStyleOpts(font_size=22)))
    )

    l2 = (
        Liquid()
            .add("no_site", [len(no_site) / len(park)], center=["11%", "38%"], label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ), )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不知道乘坐地点", pos_left=80,title_textstyle_opts=opts.TextStyleOpts(font_size=22)),
            legend_opts=opts.LegendOpts(pos_top="48%"),
        )
    )
    l3 = (
        Liquid()
            .add("no_require", [len(no_require) / len(park)], center=["51%", "38%"], label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ), )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="没有乘坐的需求", pos_left=660,title_textstyle_opts=opts.TextStyleOpts(font_size=22))
        )
    )
    l4 = (
        Liquid()
            .add("no_interest", [len(no_interest) / len(park)], center=["71%", "38%"], label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ), )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不感兴趣", pos_left=940,title_textstyle_opts=opts.TextStyleOpts(font_size=22)),
        )
    )
    grid = Grid(init_opts=opts.InitOpts(width="1400px")).add(l1, grid_opts=opts.GridOpts())\
        .add(l2, grid_opts=opts.GridOpts()) \
        .add(l3, grid_opts=opts.GridOpts()) \
        .add(l4, grid_opts=opts.GridOpts())
    return grid

##是否愿意体验汇总
def par_exper() ->Bar:
    exper_yy = park.loc[(park['是否愿意体验'] == "愿意")]
    exper_fcyy = park.loc[(park['是否愿意体验'] == "非常愿意")]
    exper_byy = park.loc[(park['是否愿意体验'] == "不愿意")]
    location = ["不愿意", "愿意", "非常愿意"]
    values = [len(exper_byy), len(exper_yy), len(exper_fcyy)]
    c = (
        PictorialBar()
            .add_xaxis(location)
            .add_yaxis(
            "",
            values,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=32,
            symbol_repeat="fixed",
            symbol_offset=[1, 2],
            is_symbol_clip=True,
            symbol=SymbolType.DIAMOND,
        )
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="公园调研对象是否愿意体验自动驾驶公交车",title_textstyle_opts=opts.TextStyleOpts(font_size=22)),
            xaxis_opts=opts.AxisOpts(is_show=True,axislabel_opts=opts.LabelOpts(font_size=20)),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=3)
                ),
                axislabel_opts=opts.LabelOpts(font_size=20)
            ),
        )
    )
    return c
def student_exper() ->Bar:
    student_yy = student.loc[(student['是否愿意体验'] == '愿意')]
    student_byy = student.loc[(student['是否愿意体验'] == '不愿意')]
    student_fcyy = student.loc[(student['是否愿意体验'] == '非常愿意')]
    location = ["不愿意", "愿意", "非常愿意"]
    values = [len(student_byy), len(student_yy), len(student_fcyy)]
    c = (
        PictorialBar()
            .add_xaxis(location)
            .add_yaxis(
            "",
            values,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=32,
            symbol_repeat="fixed",
            symbol_offset=[1, 2],
            is_symbol_clip=True,
            symbol=SymbolType.DIAMOND,
        )
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="学校调研对象是否愿意体验自动驾驶公交车",title_textstyle_opts=opts.TextStyleOpts(font_size=22)),
            xaxis_opts=opts.AxisOpts(is_show=True,axislabel_opts=opts.LabelOpts(font_size=20)),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False,),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=3)
                ),
                axislabel_opts=opts.LabelOpts(font_size=20)
            ),
        )
    )
    return c
##乘坐目的
def student_rideGoal() ->Pie:
    goPark = student.loc[student['乘坐目的'].str.contains('公园', na=False)]
    work = student.loc[student['乘坐目的'].str.contains('办事', na=False)]
    buyVege = student.loc[student['乘坐目的'].str.contains('买菜', na=False)]
    goSchool = student.loc[student['乘坐目的'].str.contains('上学', na=False)]
    other = student.loc[student['乘坐目的'].str.contains('其他', na=False)]
    c = (
        Pie(init_opts=opts.InitOpts(width="1000px"))
            .add(
            "",
            [list(z) for z in zip(['公园游玩', '附近办事', '买菜', '上学', '其他'],
                                  [len(goPark), len(work), len(buyVege), len(goSchool), len(other)])],
            center=["35%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="在乘坐过自动驾驶公交车的同学的乘坐目的"
                                      , title_textstyle_opts=opts.TextStyleOpts(font_size=22)),
            legend_opts=opts.LegendOpts(pos_left="45%",item_width=34,item_height=24,textstyle_opts=opts.TextStyleOpts(font_size=20)),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",font_size=23))

    )
    return c
#乘坐频率
def student_ride_fequency() ->Bar:
    oneMonth = student[(student["乘坐频率"] == "一月一次")]
    oneThreeMonth = student[(student["乘坐频率"] == "三月一次")]
    oneWeek = student[(student["乘坐频率"] == "一周一次")]
    Other = student[(student["乘坐频率"] == "其他")]
    c = (
        Bar()
            .add_xaxis(['三月一次', '一月一次', '一周一次', '其他'])
            .add_yaxis("人数", [len(oneMonth), len(oneThreeMonth), len(oneWeek), len(Other)],category_gap="50%")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="乘坐频率", subtitle="",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=18)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=18)),
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20),item_width=36,item_height=24)
        )

    )
    return c
##自动驾驶和普通公交车的比较
def compare() ->Bar:
    rideStudent_yes = student.loc[(student['是否乘坐']) == "是"]
    rideStudent1 = rideStudent_yes["自动普通比较"]
    string = []
    beforCompare = [[], [], [], [], [], []]

    for i in rideStudent1:
        j = i.split("|")
        string.append(j)

    for i in string:
        for j in range(6):
            beforCompare[j].append(i[j])
    compare = pd.DataFrame({
        "空间": beforCompare[0],
        "速度": beforCompare[1],
        "总体": beforCompare[2],
        "智能": beforCompare[3],
        "外观": beforCompare[4],
        "服务": beforCompare[5]
    })
    # print(compare)
    apollo_space = compare.loc[(compare["空间"] == "自动驾驶公交车")]
    normal_space = compare.loc[(compare["空间"] == "普通公交车")]
    len(compare["空间"])
    apollo_speed = compare.loc[(compare["速度"] == "自动驾驶公交车")]
    normal_speed = compare.loc[(compare["速度"] == "普通公交车")]
    len(compare["速度"])
    apollo_total = compare.loc[(compare["总体"] == "自动驾驶公交车")]
    normal_total = compare.loc[(compare["总体"] == "普通公交车")]
    len(compare["总体"])
    apollo_intelligence = compare.loc[(compare["智能"] == "自动驾驶公交车")]
    normal_intelligence = compare.loc[(compare["智能"] == "普通公交车")]
    len(compare["智能"])
    apollo_beauity = compare.loc[(compare["外观"] == "自动驾驶公交车")]
    normal_beauity = compare.loc[(compare["外观"] == "普通公交车")]
    len(compare["外观"])
    apollo_service = compare.loc[(compare["服务"] == "自动驾驶公交车")]
    normal_service = compare.loc[(compare["服务"] == "普通公交车")]
    len(compare["服务"])
    list1 = [
        {"value": len(apollo_space), "percent": len(apollo_space) / len(compare["空间"])},
        {"value": len(apollo_speed), "percent": len(apollo_speed) / len(compare["速度"])},
        {"value": len(apollo_total), "percent": len(apollo_total) / len(compare["总体"])},
        {"value": len(apollo_intelligence), "percent": len(apollo_intelligence) / len(compare["智能"])},
        {"value": len(apollo_beauity), "percent": len(apollo_beauity) / len(compare["外观"])},
        {"value": len(apollo_service), "percent": len(apollo_service) / len(compare["服务"])}
    ]
    list2 = [
        {"value": len(normal_space), "percent": len(normal_space) / len(compare["空间"])},
        {"value": len(normal_speed), "percent": len(normal_speed) / len(compare["速度"])},
        {"value": len(normal_total), "percent": len(normal_total) / len(compare["总体"])},
        {"value": len(normal_intelligence), "percent": len(normal_intelligence) / len(compare["智能"])},
        {"value": len(normal_beauity), "percent": len(normal_beauity) / len(compare["外观"])},
        {"value": len(normal_service), "percent": len(normal_service) / len(compare["服务"])}
    ]
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["安全", "空间", "总体", '智能', '外观', '服务'])
            .add_yaxis("自动驾驶公交车", list1, stack="stack1", category_gap="50%")
            .add_yaxis("普通公交车", list2, stack="stack1", category_gap="50%")
            .set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
                formatter=JsCode(
                    "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                ),font_size=24
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="自动驾驶公交车和普通公交车在各个指标的比较",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=18)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=18)),
            legend_opts=opts.LegendOpts(pos_left=500,item_width=36,item_height=24,textstyle_opts=opts.TextStyleOpts(font_size=20))
        )

    )
    return c
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout,interval=2,js_host="https://assets.pyecharts.org/assets/")
    page.add(
        park_ride_method(),
        student_ride_method(),
        park_age_classification(),
        park_reason1(),
        par_exper(),
        student_exper(),
        student_rideGoal(),
        student_ride_fequency(),
        compare()
    )
    page.render("grosshtml/gross1.html")

if __name__ == "__main__":
    page_draggable_layout()