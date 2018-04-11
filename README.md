# MoEar

用来实现对网络文章的爬取、mobi打包、并推送到Kindle设备上

## 项目描述

最初需求来源于对Kindle推送工具 [狗耳朵](http://www.dogear) / [KindleEar](https://github.com/cdhigh/KindleEar) 的使用，以及对类似 [Pocket](https://getpocket.com) 的文章归档、分类的需求。

在使用上述服务时遇到了痛点如下，狗耳朵收费了，而且界面不好看((｡•ˇ‸ˇ•｡)哼唧~)。。。KindleEar只能GAE部署，但是国内访问Google。。。你懂的，虽然FQ部署好后就不用管了，但总归不方便，使用过程中经常遇到漏推送的情况(不确定是项目本身问题还是由于跨洋网络问题造成)，而且界面不好看((｡•ˇ‸ˇ•｡)哼唧~)。最后，Pocket虽然很nice，但是除非氪金否则只保存链接，不保存文章本身，而知乎日报经常会遇到次日文章由于各种原因(原作者要求等)被删除的情况，强迫症不能忍。

## Road Map

* [X] `V0.1.0` 实现基于命令行的知乎日报爬取、本地化工具Demo，并将信息保存到DB
* [X] `V0.2.0` 实现基于Django框架admin应用，使用Scrapy工具爬取知乎日报，并迁移上个版本的DB数据
* [ ] `V0.2.1` 实现基础web页组件，如文章显示、阅读记录表单添加
* [ ] `V0.2.2` 实现Schedular管理，定时爬取数据
* [ ] `V0.2.3` 增加指定文章归集并生成 `.mobi` 文件，根据推送规则按时推送到当前用户的指定邮箱中
* [ ] `V0.2.4` 实现面向用户使用的Web站点页，包括账户系统、文章源页、文章页、阅读记录页、订阅规则页等
* [ ] `V0.2.5` 增加Docker部署支持
* [ ] `V0.3.0` 编写基本的说明&部署文档，并开源发布到GitHub
* [ ] `V0.3.1` 从Django和Scrapy中提取抽象出扩展文章源的插件编码方式，便于扩展其他文章源，同时编写文章源插件开发文档

## License

本项目采用 [![license](https://img.shields.io/github/license/littlemo/moear.svg)](https://github.com/littlemo/moear) 协议开源发布，请您在修改后维持开源发布，并为原作者额外署名，谢谢您的尊重。

若您需要将本项目应用于商业目的，请单独联系本人( [@littlemo](https://github.com/littlemo) )，获取商业授权。

## 问题

如果您在使用该应用时遇到任何问题，请在 GitHub 上查看本项目 [![moear](https://img.shields.io/badge/Repo-MoEar-brightgreen.svg)](https://github.com/littlemo/moear) ，并在其中提交 [Issues](https://github.com/littlemo/moear/issues) 给我，多谢您的帮助~~
