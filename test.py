from Database.sensor_db import DataTable
import os
from pyecharts.charts import Line,Pie
from pyecharts import options as opts


if __name__ == '__main__':
    os.chdir('D:\Program\SensorServer\Database')
    print(os.getcwd())
    #DataTable.insert(146, 27, 62)
    data = DataTable.query_all()
    #print(data)
    test_dict = {}
    for i in range(len(data)):
        item_dict = {}
        item_dict['日期'] = data[i][0]
        item_dict['时间'] = data[i][1]
        item_dict['光照'] = data[i][2]
        item_dict['磁场强度'] = data[i][3]
        item_dict['温度'] = data[i][4]
        test_dict[i] = item_dict
    print(test_dict)
    #print(test_dict.get(1))

    print(len(test_dict))
    x_list = []
    y_temp_list = []
    y_lux_list = []
    y_mag_list = []
    for i in range(0,len(test_dict)):
        x_list.append(i)
        y_temp_list.append(test_dict.get(i).get('温度'))
        y_lux_list.append(test_dict.get(i).get('光照'))
        y_mag_list.append(test_dict.get(i).get('磁场强度'))
    line = Line()
    line = (
        Line()
            .add_xaxis(x_list)
            .add_yaxis("温度", y_temp_list)
            .add_yaxis("光照", y_lux_list)
            .add_yaxis('磁场强度',y_mag_list)

    )
    line.render()
    # pie = (
    #     Pie()
    #     .add("", [list(z)
    # for z in zip(x_list, y_mag_list)])
    # .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    #
    # # 系统配置项
    # # 设置标签
    # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    # .render()
    # )
