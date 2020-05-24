>[git DOC](https://git-scm.com/docs)


### git 工作流程图

![imge](git工作流程图.png)

***

### 命令（常用）
+ reset
    + 参数 
        + --mixed HEAD~ (默认)
            + 会回滚到暂存仓库
        + --soft HEAD~
            + 只将仓库指针指向上一次
        + --hard HEAD~
            + 会回滚到暂存仓库和工作区
    + git reset 快照版本（快照hash） 目录/文件
+ diff
    + 默认比较 暂存区 和 工作区
    + git diff ID1(旧 - 红) ID2(新 - 绿)  # 白色代表共有
    + git diff ID  # 已往版本与工作区域的比较
    + git diff --cached  ID# 
+ checkout
    + checkout 
+ reflog
    + 所有提交记录
+ log
    + 参数
        + -p            # 列出变动信息
        + -number       # number表示数字 查看最近多少次的信息
        + --oneline     # 不显示 Author 和 Date信息 将摘要缩减到7显示
        + --name-only   # 值显示文件发生的变化
        + --name-status # 显示文件具体发生的变化 （更新操作很有用，上万个文件中之修改了其中几个的情况可以进行定位更新）
+ commit
    + 参数
        + -m            # 提交信息
        + -am           # 修改(不包括文件的添加)并且提交
        + --amend       # 追加上一次提交
            + 网络提交
                + git push --force-with-lease


+ branch
    + git branch -a             # 查看所有 包括远程分支 
    + git branch bran_name      # 添加分支
    + git checkout bran_name    # 切换分支
    + git checkout -b bran_name # 创建并且切换分支
    + git branch -d bran_name   # 删除分支
    + git branch -D bran_name   # 大写D 强制删除未合并过的分支
    + git branch --merged       # 查看已经合并的分支
    + git branch --no-merged
    + git branch -m old new
+ rm
    + git rm --cached *.py
    + git rm -f *.py            # 强制删除
+ mv
    + git mv old new
+ merge
    + git merge bran_name
+ stash
    + git stash
    + git stash list
    + git stash drop
    + git stash [apply|pop] [--index]
+ tag   # 打标签
    + git tag v2.0
    + git tag -d v2.0
    + git tag -l
+ archive # 打包压缩项目
    + git archive master --prefix='t/' --forma=tar.gz>t.tar.gz
+ rebase # 让子分支 往后挪 在进行住分支合并 将冲突放在子分支解决
    + git rebase master

### 与远程关联

```bash
# 添加远程主机 origin
git remote add origin git@github.com:jiuguai/local.git
git push -u origin master
git push --set-upstream origin ask # 提交分支

# 参与分支开发
git clone git_project_url
git pull origin ask:ask  # 将远程ask分支 拉到本地ask中

#-*- 合并远程分支 -*-
# 以 ask 分支为例
git checkout master
# 更新远程主分支
git pull
# 将ask 分支的基分支合为当前最新住分支
git checkout ask
git rebase master
# 合并主分支
git checkout master
git merge ask
git push

#-*- 删除远程分支 -*-
# 以 ask 分支为例
git push origin --delete ask
```


### 簡化操作
+ .bash_profile 根目录文件中添加
```bash
alias gs="git status"
alias gc="git commit -m"
alias gl="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit "
alias gb="git branch"
alias ga="git add -A"
alias go="git checkout"
```


+ .gitconfig
```bash
# 其别名
git config --global alias.a add
```


### 文件
+ .ignore
```bash
*.py
.*
!a.py
/t
/t/**/*.py

```
+
```bash
[remote "origin"]
    url = https://github.com/jiuguai/test.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master

```

### 初始化配置

    git config --global user.name zero
    git config --global user.email 
    git config --list
    存储账号密码
    git config --global credential.helper store

    git init
    git init --bare //裸露的仓库 无工作区域

    git status
    
    打包
    git archive master --prefix='zero/' --format=zip >zero.zip

### 远程仓库
    //生成 ssh 密钥、公钥
    ssh-keygen -t rsa -C
    
    git clone
    提交
    git push https://github.com/jiuguai/test.git master
    给远程仓库起别名
    git remote add gitname [url]
    git push gitname master
    //下载
    git pull git@github.com:jiuguai/test.git ask_branch:ask_branch

    //删除远程分支
    git push origin --delete ask_branch

### config 文件可以添加
        [remote "origin"]
            url = https://github.com/jiuguai/test.git
            fetch = +refs/heads/*:refs/remotes/origin/*
        [branch "master"]
            remote = origin
            merge = refs/heads/master


#### git checkout

    从暂存区还原到工作区 
    如果暂存区没有就从提交head头获取
    git checkout [head|branch_addr]-- t1.txt

******
### git分支
####查看    
    git branch [-a]
    git log --decorate --oneline --graph --all

#### 创建
    git branch dev
    
#### 切换
    git checkout dev
####创建并切换分支
    git checkout -b bran_name

#### 搭配stash    
    切换分支如果本来分支有未提交 要不提交要不使用以下命令
    git stash 
    切回来时候使用如下命令
    //查看
    git stash list
    //还原
    git stash apply stash@{num}
    //删除stash
    git stash drop stash@{num}







