# git使用
#####1、基本概念
    ·工作区
    ·暂存区
    ·仓库区
    ·远程仓库

#####2、初始配置git
    ·配置命令：git config
        ·配置所有用户：git config --system [选项]   位置：/etc/gitconfig
        ·配置当前位置：git config --global [选项]   位置：~/.gitconfig
        ·配置当前项目：git config [选项]    位置：project/.git/config
    
#####3、配置
    ·配置用户名
        sudo git config --system user.name Wang
    ·配置邮箱
        git config --global user.email 2063520993@qq.com
    
    
#####4、git基本命令
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



######@扩展延伸
    在git项目中可以在某个文件夹下定义.gitignore文件的方式，可以忽视文件
    