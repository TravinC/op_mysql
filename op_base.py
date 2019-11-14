# -*- coding: utf-8 -*-
from tools.DB_Utils.op_mysql_tool import MyPymysqlPool

# 数据库操作语句

# 查询语句
def getAll(sql, param=None):
    mysql = MyPymysqlPool()
    try:
        if param is None:
            result = mysql.getAll(sql)
        else:
            result = mysql.getAll(sql, param)
    except Exception as e:
        # log.debug("请求db异常:", e)
        raise e
    finally:
        mysql.close()
    return result

# 增加语句
def insert(sql, param):
    mysql = MyPymysqlPool()
    try:
        result = mysql.insert(sql, param)
    except Exception as e:
        # log.debug("请求db异常:", e)
        raise e
    finally:
        mysql.close()
    return result

# 修改语句
def update(sql, param):
    mysql = MyPymysqlPool()
    try:
        result = mysql.update(sql, param)
    except Exception as e:
        # log.debug("请求db异常:", e)
        raise e
    finally:
        mysql.close()
    return result

# 删除语句
def delete(sql, param):
    mysql = MyPymysqlPool()
    try:
        result = mysql.delete(sql, param)
    except Exception as e:
        raise e
    finally:
        mysql.close()
    return result