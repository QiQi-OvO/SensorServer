from flask import Flask,request,render_template,redirect
from Database.sensor_db import DataTable
import data_handler
import os
import charts_generate
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    """
    登录界面
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == 'admin':
        return redirect('/index')
    else:
        return render_template('login.html',**{'msg':'用户名或者密码错误'})


@app.route('/index')
def index():
    """
    后台管理界面
    :return:
    """
    data_dict = data_handler.create_all_data_dict()
    pyecharts_line = charts_generate.get_line()
    #模版渲染
    return render_template('display.html',
                           data_dict = data_dict,
                           line_options = pyecharts_line.dump_options() )


@app.route('/detail')
def detail():
    uid = request.args.get('uid')
    item_dict = data_handler.create_all_data_dict()
    uid = int(uid)
    item_dict = item_dict.get(uid)
    # 20-60uT 手机自产磁场强度   低于60正常
    tips = data_handler.get_tips(item_dict)
    context = {}
    context['item_dict'] = item_dict
    context['tips'] = tips
    text = tips['date']
    print(data_handler.send_tips('notice_phone', 'cBgUH3WF2i_n6hawEjNBsg', text))
    text = tips['light']
    print(data_handler.send_tips('notice_phone', 'cBgUH3WF2i_n6hawEjNBsg', text))
    text = tips['temp']
    print(data_handler.send_tips('notice_phone', 'cBgUH3WF2i_n6hawEjNBsg', text))
    text = tips['mag']
    print(data_handler.send_tips('notice_phone', 'cBgUH3WF2i_n6hawEjNBsg', text))
    return render_template('detail.html',context =context)



@app.route('/demo', methods=['POST'])
def recieve():
    light = request.form["light"]
    temp = request.form["temp"]
    magnetic = request.form["magnetic"]
    print(f"light: {light}, temp: {temp},magnetic:{magnetic}")
    light = float(light)
    temp = float(temp)
    magnetic = float(magnetic)
    os.chdir('D:\Program\SensorServer\Database')
    DataTable.insert(light,temp,magnetic)
    return "ok"

if __name__ == '__main__':
    #flask run --host=0.0.0.0 --port=5000
    #http://192.168.0.105:5000/
    app.run(host='0.0.0.0')
