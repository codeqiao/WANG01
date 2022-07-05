# git简介
##### 2、代码管理工具的功能
    ·防止代码丢失，做备份
    ·项目的版本管理和控制，可以通过设置节点进行跳转
    ·建立各自的开发环境分支，互不影响，方便合并
    ·在多终端开发时，方便代码的相互传输

##### 3、git的特点
    ·git是开源的，多在Linux下使用，可以管理各种文件
    ·git是分布式的项目管理工具（svn是集中式的）
    ·git数据管理更多样化，分享速度快，数据A安全
    ·git拥有更好的分支支持，方便多人协调

##### 4、git安装
    sudo apt-get install git

# git使用
##### 1、基本概念
    ·工作区
    ·暂存区
    ·仓库区
    ·远程仓库

##### 2、初始配置git
    ·配置命令：git config
        ·配置所有用户：git config --system [选项]   位置：/etc/gitconfig
        ·配置当前位置：git config --global [选项]   位置：~/.gitconfig
        ·配置当前项目：git config [选项]    位置：project/.git/config
    
##### 3、配置
    ·配置用户名
        sudo git config --system user.name Wang
    ·配置邮箱
        git config --global user.email 2063520993@qq.com
    
    
##### 4、git基本命令
    ·初始化项目
        在项目目录下 git init
    ·查看本地仓库的状态
        git status
    ·将工作区的内容提交到暂存区
        git add 文件1,文件2...
        git add * 提交所有文件（但是不能提交隐藏文件）
    ·撤回暂存
        git rm --cached 文件1,文件2...
    ·将暂存区记录的内容存储到仓库
        git commit [file1...] -m [message]
        -m表示添加一些同步信息，表达同步内容
    ·查看提交日志信息
        git log
    ·恢复文件
        git checkout -- 文件名
    ·移动或者删除文件·初始化项目
        在项目目录下 git init
        git mv [file] [path]
        git rm [file]
        和add是同一级别的操作



###### @扩展延伸
    在git项目中可以在某个文件夹下定义.gitignore文件的方式，可以忽视文件


# 版本控制
主要依赖于仓库里的内容

##### 1、退回到上一个commit节点
>git reset --hard HEAD^(加一个^就退一个版本，两个就退两个版本)
>往前退的同时日志也会被删除

##### 2、git reset --hard b3a7436
全球唯一码的前七位
>就可以前往那个版本
##### 3、git reflog
会显示记录所有的操作
>查找reflog就可以跳转到任意想要的版本

##### 4、创建标签
在项目重要的commit节点位置添加快照，保存当前的工作状态，一般用于版本的迭代
>git tag [tag_name] [commit_id] -m [message]
>git reset --hard 标签名 跳转到标签处
>git tag -d 标签名 删除标签
>git tag 显示标签列表
>git show 标签名 打印标签处的详细信息

# 保存工作区

#####保存工作区内容
在保存工作区前运行git status最好啥也没有
>***git stash save*** “封存信息”
>***git stash list*** -- 查看保存工作去列表
>***git stash aplly stash@{}*** --应用stash@{n}那个工作区版本
>git stash drop stash@{0} -- 删除0工作区
>git stash clear -- 删除所有的工作区

# 分支管理
分支即每个人在原有的代码的基础上建立自己的工作环境，单独开发，互不干扰。
>git branch 分区名 -- 创建分支
>git branch -- 查看分支
>git checkout 分支名 -- 切换到其他的分支
>git checkout -b 分支名 -- 创建一个分支并且切换到这个分支
>***git merge 分支名*** -- 在master工作目录下执行该命令，合并两个分支到该工作区

master是主分支

**注意：**
>当在分支添加文件或者文件夹时最后合并到master需要自行进行commit -- 新版本应该已经没有该问题了

在项目设计的时候需要降低耦合度，同一个文件不要让多个人对其进行操作

##### 删除分支
>git branch -d 分支名 -- 只有分支合并以后才能删除成功，如果想要强行删除那么就用 -D

# 远程仓库连接

##### 1.下载远程仓库代码
>git clone 远程仓库地址

##### 2、连接远程仓库
>git remote add origin(给远程主机取名字) https://github.com/WANG00YAN/WANG001.git -- 把该项目和远程主机进行相关联
>git remote -- 查看添加的远程的主机
>git remote rm 远程主机名(origin) -- 删除远程主机

##### 3、上传
>git push [-u](第一次上传需要的参数) 远程主机名 分支名 -- 将本地分支上传到远程主机仓库
>git push 第二次就可以直接git push

标签上传
>git push 远程主机名 标签名[--tags](上传所有标签)

>git branch -a -- 可以看到在远程仓库的分支
>git push 远程仓库名 ：分支名 -- 删除远程分支
>git push 远程仓库名 --delete tag [tagname]
>git push --force origin

##### 4、从远程获取代码
***git pull***
***git fetch***
区别：
>拉取到本地但是不会和本地的自行合并
>git detch origin master:tm -- 拉取到tm分支中，可以自行合并


# 软件项目开发流程

需求分析->该要设计->项目计划->详细设计->编码测试->项目测试
1、需求分析：确定用户的真实需求
>确定用户的真实需求，项目的基本功能
>确定项目的整体难度和可行性分析
>需求分析文档，用户确定

2、该要设计：对项目进行初步分析和整体的设计
>确定功能模块
>进行可行性分析，搭建整体架构图
>确定技术思路和使用框架
>形成该要文档指导开发流程

3、项目计划：确定项目开发的时间轴和流程
>确定开发工作的先后顺序
>确定时间轴，时间里程碑
>人员分工
>形成干特图和思维导图等辅助内容

4、详细设计：项目的具体实现
>形成详细设计文档：思路，逻辑流程，功能说明，技术点说明，数据结构说明，代码说明

5、编码测试：按照预订计划实现代码编写，并且做基本测试
>代码测试
>写测试程序
>技术公关

6、项目测试：对项目按照功能进行测试
>跨平台测试，使用测试
>根据测试报告进行代码修改
>完成测试报告

7、项目发布
>项目交付用户进行发布
>编写项目说明文档

8、后期维护
>维护项目正常运转
>进行项目的迭代升级
