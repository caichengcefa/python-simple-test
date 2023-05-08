import datetime
# import time
# import sys
# import os



tmp_datetime_show = datetime.datetime.now()  # 修改成默认是当日执行 + datetime.timedelta()

tmp_hour_int = int(tmp_datetime_show.strftime("%H"))


if tmp_hour_int < 12 :
    # 判断如果是每天 中午 12 点之前运行，跑昨天的数据。
    tmp_datetime_show = (tmp_datetime_show + datetime.timedelta(days=-1))
tmp_datetime_str = tmp_datetime_show.strftime("%Y-%m-%d %H:%M:%S.%f")

print(" ## %s ##" % tmp_datetime_str)
# print("\n######################### hour_int %d " % tmp_hour_int)
# str_db = "MYSQL_HOST :" + MYSQL_HOST + ", MYSQL_USER :" + MYSQL_USER + ", MYSQL_DB :" + MYSQL_DB
# print("\n######################### " + str_db + "  ######################### ")
# print("\n######################### begin run %s %s  #########################" % (run_fun, tmp_datetime_str))