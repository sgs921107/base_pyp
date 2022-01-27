# 项目说明
> python项目基础框架

## 环境依赖
- system: CentOS Linux release 7.6
- python: python3.6.8
- python depend: deploy/requirements.txt
- mysql: 5.7  max_connections>=512
- redis: 5.0
- rabbitmq: 3.8

## 部署
> 1.手动clone代码并切换至目标分支或标签  
> 2.根据configs/env_demo生成并配置env文件/etc/base_pyp/.env  
> 3.root用户运行: source /etc/base_pyp/.env && cd $HOST_PROJECT_DIR/deploy && sh deploy.sh

## docker容器服务说明
1. demo: this is a demo

## 运维
进入项目部署目录: source /etc/base_pyp/.env && cd $HOST_PROJECT_DIR/deploy  
> 配置查看: docker-compose run --rm demo python env_manager.py -l  
> 执行迁移: docker-compose run --rm demo python db_manager.py upgrade head  
> 单元测试: docker-compose run --rm demo sh unit_test.sh  
> 启动服务: docker-compose up [-d]  
> 停止服务: docker-compose stop  
> 重启服务: docker-compose restart  
> 删除服务: docker-compose down