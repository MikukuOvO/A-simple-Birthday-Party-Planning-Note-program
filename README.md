# 一个简易的生日聚会计划便签

## 简述

本程序基于 Flask 的框架设计了一个简易的生日聚会计划便签，支持通过输入生日日期，当天日期以及提前准备的天数给出指定日期的具体信息。

> 更新于 2024 年 3 月 3 日
通过前后端分离，支持录入亲友信息，对于选定人员进行个性化生日计划定制。

## 环境

```
python==3.7.16
Flask==3.0.2
Flask-Cors==4.0.0
```

## 编译 & 运行

```
flask run
```

## 文件结构

```
-instance/
	-site.db # 数据库
-static/
	-img/
	-style.css
-templates/
	-all_info.html # 录入亲人信息
	-basic_info.html # 输入生日和当天日期
	-closepage.html # 关闭页面
	-endpage.html # 结束页面
	-index.html # 初始界面
	-result_display.html # 结果展示页面
	-set_plan_day.html # 生日聚会计划制定日期
-app.py 代码入口
```

