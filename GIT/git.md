>[git DOC](https://git-scm.com/docs)


### git 工作流程图

![imge](git工作流程图.png)

***

### 命令（常用）
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

+ branch
    + git branch -a             # 查看所有 包括远程分支 
    + git branch bran_name      # 添加分支
    + git checkout bran_name    # 切换分支
    + git checkout -b bran_name # 创建并且切换分支
    + git branch -d bran_name   # 删除分支
    + git branch -D bran_name   # 大写D 强制删除未合并过的分支
    + git branch --merged       # 查看已经合并的分支
    + git branch --no-merged
+ rm
    + git rm --cached *.py
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

# 合并远程分支
# 以 ask 分支为例
git checkout master`
# 更新远程主分支
git pull
git checkout ask
# 将ask 分支的基分支合为当前最新住分支
git rebase master
git checkout master
# 合并主分支
git merge ask
git push

# 删除远程分支
# 以 ask 分支为例
git push origin --delete ask
```


### 簡化操作
+ .bash_profiel 根目录文件中添加
```bash
alias gs="git status"
alias gc="git commit -m"
alias gl="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit "
alias gb="git branch"
alias ga="git add ."
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



******
### 命令
####git add

    git add filename 
    git add .           #不包括删除文件
    git add -u          #不会提交新文件
    git add -A          #. -u 的综合体
    git add *.txt


####git commit

    git commit -m 'first'
    git commit -m 'second' test.txt


    //一次性提交
    git commit -am 'headname' [filenames]
  
    //修正上一次提交
    git commit --amend 
    //追加
    git commit -C head -a --amend

    //查看提交信息
    git log
    git log --oneline

####git reset
    git reset --[mixed|soft|hard] HEAD~5
    git reset 7f33013

    回滚文件 HEAD 指针不移动

#### git diff
    比较工作区和暂存区
    git diff

    比较两个快照
    git diff 7f33013 7fwd013

    工作区和快照比较
    git diff 7f33013

    暂存区与快照比较
    git --cached [7f33013]

#### git rm
    git rm filename
    git rm --cached filename
    git rm -f filename


#### git mv
    git mv oldfile newfile

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

####   删除      
    //切换到另一个分支才可以删除
    git branch -d dev
    
#### 修改分支名
    git branch -m dev fix_name

####git merge
    git  merge dev [--no-commit]
    解决冲突后
    git commit -am 'mergeversion'
####git rebase  
    #replace base
    业务场景 分支处理冲突
    ask   $ git rebase master
    再交给住分支合并
    master $ git merge  ask


