import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid, Bar
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
#获取数据
park=pd.read_excel("调研数据.xlsx",sheet_name="data1",engine="openpyxl",dtype=str)
#print(park)
##出行方式分类
didi=park.loc[(park['出行方式']=="滴滴")]
car=park.loc[(park['出行方式']=="私家车")]
gjc=park.loc[(park['出行方式']=="公交车")]

##年龄段
park['年龄']=park['年龄'].astype("int")
junior=park.loc[(park['年龄']>=18)&(park['年龄']<=34)]
middle_age=park.loc[(park['年龄']>=35)&(park['年龄']<=50)]
ederly=park.loc[(park['年龄']>=51)]
#青年人中 出行方式分类
junior_didi=junior.loc[(junior['出行方式']=='滴滴')]
junior_car=junior.loc[(junior['出行方式']=='私家车')]
junior_gjc=junior.loc[(junior['出行方式']=='公交车')]
ederly_gjc=ederly.loc[(ederly['出行方式']=='公交车')]

# print(junior_didi,junior_car,junior_gjc)
# print(len(junior))
#中年人中出行方式分类
middle_age_didi=middle_age.loc[(middle_age['出行方式']=='滴滴')]
middle_age_car=middle_age.loc[(middle_age['出行方式']=='私家车')]
middle_age_gjc=middle_age.loc[(middle_age['出行方式']=='公交车')]
# print(middle_age_didi,middle_age_car,middle_age_gjc)
# print(len(middle_age))
#老年人中出行方式分类
ederly_didi=ederly.loc[(ederly['出行方式']=='滴滴')]
ederly_car=ederly.loc[(ederly['出行方式']=='私家车')]
ederly_gjc=ederly.loc[(ederly['出行方式']=='公交车')]
print(ederly_didi,ederly_car,ederly_gjc)
print(len(ederly))
##未乘坐原因分类
no_method=park.loc[(park['未乘坐原因']=="不知道乘坐方式")]
no_interest=park.loc[(park['未乘坐原因']=="不知道乘坐地点")]
no_require=park.loc[(park['未乘坐原因']=="没有需求")]
#是否乘坐
ride_yes=park.loc[(park['是否乘坐']=="是")]
ride_no=park.loc[(park['是否乘坐']=="否")]
#是否体验
exper_yy=park.loc[(park['是否愿意体验']=="愿意")]
exper_fcyy=park.loc[(park['是否愿意体验']=="非常愿意")]
exper_byy=park.loc[(park['是否愿意体验']=="不愿意")]
#是否了解
konw_yes=park.loc[(park['是否了解']=="是")]
konw_no=park.loc[(park['是否了解']=="否")]

