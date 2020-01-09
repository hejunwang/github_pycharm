

# Git 初始化

​    现在进入本篇文章真正的主题，介绍一下Git的基本命令和操作，会从Git的版本库的初始化，基本操作和独有的常用命令三部分着手，让大家能够开始使用Git。

​    Git通常有两种方式来进行初始化:

​    **git clone**: 这是较为简单的一种初始化方式，当你已经有一个远程的Git版本库，只需要在本地克隆一份，例如'git clone git://github.com/someone/some_project.git some_project'命令就是将'git://github.com/someone/some_project.git'这个URL地址的远程版 本库完全克隆到本地some_project目录下面

​    **git init**和**git remote**：这种方式稍微复杂一些，当你本地创建了一个工作目录，你可以进入这个目录，使用 git init 命令进行初始化，Git以后就会对该目录下的文件进行版本控制，这时候如果你需要将它放到远程服务器上，可以在远程服务器上创建一个目录，并把 可访问的URL记录下来，此时你就可以利用 git remote add 命令来增加一个远程服务器端，例如'git remote add origin git://github.com/someone/another_project.git'这条命令就会增加URL地址为'git: //github.com/someone/another_project.git'，名称为origin的远程服务器，以后提交代码的时候只需要使用 origin别名即可

# Git 基本命令  

   现在我们有了本地和远程的版本库，让我们来试着用用Git的基本命令吧：

​    **git pull**：从版本库(既可以是远程的也可以是本地的)将代码更新到本地，例如：'git pull origin master'就是将origin这个版本库的代码更新到本地的master主枝，该功能类似于SVN的update

​    **git add**：将所有改动的文件（新增和有变动的）放在暂存区，由git进行管理

​    **git rm**：从当前的工作空间中和索引中删除文件，例如'git rm app/model/user.rb'，移除暂存区

​    **git commit**：提交当前工作空间的修改内容，类似于SVN的commit命令，例如'git commit -m "story #3, add user model"'，提交的时候必须用-m来输入一条提交信息

​    **git push**：将本地commit的代码更新到远程版本库中，例如'git push origin branchname'就会将本地的代码更新到名为orgin的远程版本库中

​    **git log**：查看历史日志

​    **git revert**：还原一个版本的修改，必须提供一个具体的Git版本号，例如'git revert bbaf6fb5060b4875b18ff9ff637ce118256d6f20'，Git的版本号都是生成的一个哈希值、

​    上面的命令几乎都是每个版本控制工具所公有的，下面就开始尝试一下Git独有的一些命令：

# Git 独有命令

​    **git branch**：对分支的增、删、查等操作，例如 git branch new_branch 会从当前的工作版本创建一个叫做new_branch的新分支，git branch -D new_branch 就会强制删除叫做new_branch的分支，git branch 就会列出本地所有的分支

​    **git checkout**：Git的checkout有两个作用，其一是在 不同的branch之间进行切换，例如 'git checkout new_branch'就会切换到new_branch的分支上去;另一个功能是 还原代码的作用，例如git checkout app/model/user.rb 就会将user.rb文件从上一个已提交的版本中更新回来，未提交的内容全部会回滚

​    **git rebase**：用下面两幅图解释会比较清楚一些，rebase命令执行后，实际上是将分支点从C移到了G，这样分支也就具有了从C到G的功能 （使历史更加简洁明了）

​                       ![Git使用基础篇 ](http://static.open-open.com/lib/uploadImg/20120328/20120328111440_202.png)

​    **git reset**：回滚到指定的版本号，我们有A-G提交的版本，其中C 的版本号是 bbaf6fb，我们执行了'git reset bbaf6fb'那么结果就只剩下了A-C三个提交的版本

​                        ![Git使用基础篇 ](http://static.open-open.com/lib/uploadImg/20120328/20120328111443_111.png)

​    **git stash**：将当前未提交的工作存入Git工作栈中，时机成熟的时候再应用回来，这里暂时提一下这个命令的用法，后面在技巧篇会重点讲解

​    **git config**：新增、更改Git的各种设置，例如：git config branch.master.remote origin 就将master的远程版本库设置为别名叫做origin版本库

​    **git tag**：将某个版本打上一个标签，例如：git tag revert_version bbaf6fb50 来标记这个被你还原的版本，那么以后你想查看该版本时，就可以使用 revert_version标签名，而不是哈希值了

# Git 其他命令

　　**add**         #添加文件内容至索引

　　**branch**      #列出、创建或删除分支

　　**checkout**     #检出一个分支或路径到工作区

　　**clone**       #克隆一个版本库到一个新目录

　　**commit**  　#最近一次的提交，--amend修改最近一次提交说明

　　**diff**        #显示提交之间、提交和工作区之间等的差异　　

　　**fetch**       #从另外一个版本库下载对象和引用　

　　**init**        #创建一个空的 Git 版本库或重新初始化一个已存在的版本库

　　**log**         #显示提交日志 --stat 具体文件的改动

　　**reflog**　　　　#记录丢失的历史

　　**merge**      #合并两个或更多开发历史，--squash 把分支所有提交合并成一个提交

　　**mv**         #移动或重命名一个文件、目录或符号链接

　　**pull**        #获取并合并另外的版本库或一个本地分支（相当于git fetch和git merge）

　　**push**         #更新远程引用和相关的对象　　

　　**rebase**       #本地提交转移至更新后的上游分支中

　　**reset**         #重置当前HEAD到指定状态

　　**rm**         #从工作区和索引中删除文件

　　**show**        #显示各种类型的对象

　　**status**        #显示工作区状态

　　**tag**         #创建、列出、删除或校验一个GPG签名的 tag 对象 

　　**cherry-pick** #从其他分支复制指定的提交，然后导入到现在的分支

　　

#### git分支命令

创建分支：

git branch linux              #创建分支

git checkout linux            #切换分支

git branch                   #查看当前分支情况,当前分支前有*号

git add readme.txt            #提交到暂存区

git commit -m “new branch”    #提交到git版本仓库

git checkout master           #我们在提交文件后再切回master分支



分支合并：（合并前必须保证在master主干上）

**git branch** 　　　　　 #查看在哪个位置

**git merge Linux**　　　　#合并创建的Linux分支（–no–ff默认情况下，Git执行”快进式合并”（fast-farward merge），会直接将Master分支指向Develop分支。使用–no–ff参数后，会执行正常合并，在Master分支上生成一个新节点。）

**git branch -d linux**　　 #确认合并后删除分支

如果有冲突：

**git merge linux** 　　　#合并Linux分支(冲突)

Auto-merging readme.txt

CONFLICT (content): Merge conflict in readme.txt

Automatic merge failed; fix conflicts and then commit the result.

　　#那么此时，我们在master与linux分支上都分别对中readme文件进行了修改并提交了，那这种情况下Git就没法再为我们自动的快速合并了，它只能告诉我们readme文件的内容有冲突，需要手工处理冲突的内容后才能继续合并

自己修改完readme.txt文件后再次提交

　

 

# Git 工作流程如下

　　1. 在工作目录中修改某些文件。

　　2. 对修改后的文件进行快照，然后保存到暂存区域。

　　3. 提交更新，将保存在暂存区域的文件快照永久转储到 Git 目录中。

　　所以，我们可以从文件所处的位置来判断状态：如果是 Git 目录中保存着的特定版本文件，就属于已提交状态；如果作了修改并已放入暂存区域，就属于已暂存状态；如果自上次取出后，作了修

改但还没有放到暂存区域，就 是已修改状态。到第二章的时候，我们会进一步了解其中细节，并学会如何根据文件状态实施后续操作，以及怎样跳过暂存直接提交。

在正式使用前，我们还需要弄清楚Git的三种重要模式，分别是**已提交、已修改、已暂存**

　　　　　　　　　　　　**![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174201623-1776071686.png)**

 

　　已提交(committed):表示数据文件已经顺利提交到Git数据库中。

　　已修改(modified):表示数据文件已经被修改，但未被保存到Git数据库中。

　　已暂存(staged):表示数据文件已经被修改，并会在下次提交时提交到Git数据库中。

# 实战

\1. 先创建一个工程的目录mkdir test_project

\2. cd test_project

\3. git init 初始化git工作目录（git init –bare功能相同）

  git init的结果（这个隐藏的git目录里面的内容和--bare创建的相同）

![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174416513-612893373.png)

  git init --bare 路径

![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174424076-543342440.png)

\4. touch readme 创建一个文件

\5. git status 查看状态

　　第一次查看，这个文件还没有添加到暂存区的

　　　![image-20200108202116707](C:\Users\Hua-cloud\AppData\Roaming\Typora\typora-user-images\image-20200108202116707.png)

6.git add readme 将readme文件添加到暂存区

　　既然有添加，那就有删除（此处说的是暂存区的操作，不会删除文件）

　　git rm --cached readme 　

7.git status 再次查看暂存区的状态

　　将readme添加到暂存区后的状态

　　　　![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174509185-269205270.png)

\8. git commit -m "first commit" 提交到自己的中央仓库（init就是创建自己的中央仓库） 

\9. git log查看日志（相当与svn的提交日志）

　　　　 ![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174535123-619959998.png)

　　到目前为止自己本地仓库就提交结束了

　　之后就是提交到远程仓库了

10 git remote –v 查看本地存储的远程仓库信息，如果是clone出来的工程这个结果如下

　　　　 ![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174555513-2058573015.png)

　　origin 表示的是远程仓库的别名（默认为origin，也可以自己起，fetch更新类似于update，push推数据相当于commit）

　　如果不是clone的工程，就不会有任何结果，要自己添加，命令如下：

　　git remote add test ssh://root@10.0.0.5/usr/GitData/DingDang/.git

　　　　![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174606123-1903416899.png)

　　　　![img](https://images2017.cnblogs.com/blog/1232780/201711/1232780-20171101174622435-717896173.png)

11.做完这步然后就是远程推数据了（必须保证本地仓库里面有提交，注意是本地仓库而不是暂存区）

　　git push test

　　到此自己创建的文件就推到了远程的git仓库了

12 还有一个功能比较重要，本地仓库的版本回退

　　git reset --hard HEAD^  #还原历史提交版本上一次

　　git reset --hard 版本号  #就是上图黄色的部分，仅需要前7位即可

　如果回退过头了，log是看不到未来的版本号的，想看可以用git reflog查看

### git本地创建分支,并提交到github上 

那么怎么在本地创建分支，并提交到github或者是远程仓库中呢？

其实很简单：

第一步：

```
git checkout -b fenzhi1 创建新的分支
```

第二步：

```
git push origin branch_name 这样远程仓库中也就创建了一个test分支
```

第三步 : 

​            

```
git remote –v 查看本地存储的远程仓库信息

​			origin  git@github.com:/hejunwang/github_pycharm.git (fetch)
​			origin  git@github.com:/hejunwang/github_pycharm.git (push)
```

第四步 :

​		 把这个分支提交到github上 ,完成以上，我们就将本地的分支提交到远程仓库了。

		$ git push origin fenzhi2
		
		Enumerating objects: 11, done.
	Counting objects: 100% (11/11), done.
	Delta compression using up to 4 threads
	Compressing objects: 100% (7/7), done.
	Writing objects: 100% (8/8), 854 bytes | 142.00 KiB/s, done.
	Total 8 (delta 3), reused 0 (delta 0)
	remote: Resolving deltas: 100% (3/3), completed with 1 local object.
	remote:
	remote: Create a pull request for 'fenzhi2' on GitHub by visiting:
	remote:      https://github.com/hejunwang/github_pycharm/pull/new/fenzhi2
	remote:
	To github.com:/hejunwang/github_pycharm.git
	
	 * [new branch]      fenzhi2 -> fenzhi2






#### git 创建分支 

创建 `dev` 分支,列出分支已验证是否创建成功

```ruby
# 创建分支
$git branch dev
# 列出分支
$ git branch
  dev
* master
$ 
```

> \* `master` 前面的 * 标记表明当前仍然处于 `master` 分支



## 切换分支

切换到新分支以便在分支上开展工作



```ruby
# 切换分支
$ git checkout dev
Switched to branch 'dev'
# 列出分支
$ git branch
* dev
  master
$
```



现在,我们在 `dev` 分支上奋笔疾书,先后提交两个版本后完成分支开发工作:



```ruby
# 查看当前文件列表
$ ls
LICENSE     README.md   test.txt
# 查看目标文件内容
$ cat test.txt
add test.txt
see https://snowdreams1006.github.io/git/usage/remote-repository.html

# 第一个版本: learn git branch
$ echo "learn git branch" >> test.txt
$ git add test.txt
$ git commit -m "learn git branch"
[dev 9c30e50] learn git branch
 1 file changed, 1 insertion(+)

# 第二个版本: see https://snowdreams1006.github.io/git/usage/branch-overview.html
$ echo "see https://snowdreams1006.github.io/git/usage/branch-overview.html" >> test.txt
$ git add test.txt
sunpodeMacBook-Pro:git-demo sunpo$ git status
On branch dev
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    modified:   test.txt

$ git commit -m "see https://snowdreams1006.github.io/git/usage/branch-overview.html"
[dev 413a4d1] see https://snowdreams1006.github.io/git/usage/branch-overview.html
 1 file changed, 1 insertion(+)
```





此时,再从 `dev` 分支切换回 `master` 分支,合并`dev`分支前看一下当前文件内容:



```ruby
# 切换回 master 分支
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
sunpodeMacBook-Pro:git-demo sunpo$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
# 查看当前文件列表
$ ls
LICENSE     README.md   test.txt
# 查看文件内容: 无 dev 分支更改
$ cat test.txt
add test.txt
see https://snowdreams1006.github.io/git/usage/remote-repository.html
$ 
```



## 合并分支

切换回 `master` 分支并没有我们在 `dev` 分支的更改,因为两条时间线是独立的,现在合并 `dev` 分支,再看一下当前文件内容:

```csharp
# 合并 dev 分支
$ git merge dev
Updating b3d8193..413a4d1
Fast-forward
 test.txt | 2 ++
 1 file changed, 2 insertions(+)
# 查看文件内容: 已经存在 dev 分支的更改!
$ cat test.txt
add test.txt
see https://snowdreams1006.github.io/git/usage/remote-repository.html
learn git branch
see https://snowdreams1006.github.io/git/
```



## 删除分支

合并分支后,`dev` 分支的历史使命已经完成,应该及时清空不必要分支.



```ruby
# 删除 dev 分支
$ git branch -d dev
Deleted branch dev (was 413a4d1).

# 列出当前分支: 只剩下 master 分支
$ git branch
* master
$ 
```



以上场景包括了分支的常用操作,创建分支(`git branch `),切换分支(`git checkout `),删除分支(`git branch -d `)一系列操作十分流畅,因此 `git` 鼓励我们大量使用分支!

## 小结

- 列出分支 `git branch`

- ```
  $ git branch
  
  * fenzhi2
    master
  ```

  * 

- 创建分支 `git branch `

  ```
  $ git branch fenzhi2
  
  ```

  

- 切换分支 `git checkout `    

  ```
  $ git checkout fenzhi2
  Switched to branch 'fenzhi2'
  
  ```

- 创建并切换分支 `git checkout -b `

- 合并指定分支到当前分支 `git merge '

  ```
  $ git merge fenzhi2
  合并分支2
  ```

- 删除分支 `git branch -d ` 

#### 主分支master上创建文件并上传到远程仓库

```python
Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ ls
dev_test.py*  numpy_file/  parse_pressresult/  readMe.txt  test.py*  venv/
matplotlib/   pandas/      Read.py*            runbook/    test.txt  zhuabao.py*

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git pull               #合并本地的文件
Already up to date.

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ echo "master 新建文件并上传" >>mastertext.txt     #新建文件

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git status                    #查看状态
On branch master
Your branch is ahead of 'origin/master' by 8 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        mastertext.txt

nothing added to commit but untracked files present (use "git add" to track)

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git add mastertext.txt      #暂存到本地库 
warning: LF will be replaced by CRLF in mastertext.txt.
The file will have its original line endings in your working directory

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git commit -m "新建一个txt文件 在master上推送到远程仓库"      #提交到远程库
[master dcf6d05] 新建一个txt文件 在master上推送到远程仓库
 1 file changed, 1 insertion(+)
 create mode 100644 mastertext.txt


Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git remote -v
origin  git@github.com:/hejunwang/github_pycharm.git (fetch)
origin  git@github.com:/hejunwang/github_pycharm.git (push)

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ ls
dev_test.py*    matplotlib/  pandas/             Read.py*    runbook/  test.txt  zhuabao.py*
mastertext.txt  numpy_file/  parse_pressresult/  readMe.txt  test.py*  venv/

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 9 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)
$ git push                 #推送到远程库
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 737 bytes | 184.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To github.com:/hejunwang/github_pycharm.git
   b873a52..dcf6d05  master -> master

Hua-cloud@26242-hejw MINGW64 /d/PycharmProjects/github_pycharm (master)

```

