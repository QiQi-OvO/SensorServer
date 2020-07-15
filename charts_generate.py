from Database.sensor_db import DataTable
import os
from pyecharts.charts import Line
import data_handler


def get_line():
    all_dict = data_handler.create_all_data_dict()
    print(all_dict)
    x_list = []
    y_temp_list = []
    y_lux_list = []
    y_mag_list = []
    for i in range(0,len(all_dict)):
        x_list.append(i)
        y_temp_list.append(all_dict.get(i).get('temp'))
        y_lux_list.append(all_dict.get(i).get('light'))
        y_mag_list.append(all_dict.get(i).get('mag'))

    line = (
        Line()
            .add_xaxis(x_list)
            .add_yaxis("温度(℃)", y_temp_list)
            .add_yaxis("光照(Lux)", y_lux_list)
            .add_yaxis('磁场强度(nT)',y_mag_list)

    )
    return line

if __name__ == '__main__':
    os.chdir('D:\Program\SensorServer\Database')
    print(os.getcwd())
    get_line()