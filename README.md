# test_frame_cmd
接口测试框架（命令行版/python2）

## 题外话
刚开始做接口测试的时候在网上看了几篇测试框架的文章，其中有一篇博文介绍的测试框架并不是用来测试接口的，却给了我很大的启发。这篇博客介绍了测试过程中可能会出现的几个需求：参数化、公共方法、日志输出，并且给出了详细的实现方式。  

## 项目介绍
### 框架环境
**开发语言**：python2  
**主要库**：requests、unittest、logging、pymysql
### 主要功能
- 批量执行接口测试用例
- 数据参数化
- 保存测试日志
- 输出测试报告
- 每日自启
- 用例编写简单