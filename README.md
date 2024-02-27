# 一个简易的生日聚会计划便签

## 简述

本程序基于 Flask 的框架设计了一个简易的生日聚会计划便签，支持通过输入生日日期，当天日期以及提前准备的天数给出指定日期的具体信息。

## 环境

```
python==3.7.16
Flask==3.0.2
```

## 编译 & 运行

```
flask run
```

## 文件结构

```
-static/
	-img/
	-style.css
-templates/
	-basic_info.html # 输入生日和当天日期
	-index.html # 初始界面
	-set_plan_day.html # 生日聚会计划制定日期
-app.py 代码入口
```

