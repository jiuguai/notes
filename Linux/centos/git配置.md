
1. 创建git用户
	adduser git
	passwd git
	ssh git@[ip|domain]

2. 创建密钥
	su git
	ssh-keygen -t rsa -C wind2zero@163.com

3. 添加公钥
	cat zero.pub >> authorized_keys

4. 第一次提交
	git remote add origin git@[ip|domian]:path
	git push -u origin master

5. 禁止客户端以shell 登陆
	+ su git
	+ mkdir /home/git/git-shell-commands
	+ su root
	+ vi /etc/passwd   
		+ 找到 git:x:1000:1000::/home/git:/bin/bash
		+ 改为 git:x:1000:1000::/home/git:/bin/git-shell
