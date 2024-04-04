# Linux NOTES

[TOC]



## Operating Systems

### 2.4.1 Linux Distributions

#### Red Hat

it started as a simple distribution that introduced the Red Hat Package Manager(RPM). It focus more on the server applications and released the **Red Hat Enterprise Linux(RHEL)** , which paid a service on a long release cycle.

Everything in RHEL is open source, so a project call CentOS which recompiled all the RHEL packages came to be.

**Scientific Linux** is an example of a specific-use of distribution based on Red Hat. It enables scientific computing.

#### SUSE

derived from Slackware. 

one of the first comprehensive Linux distributions.

SUSE Linux Enterprise contains proprietary code.

**openSUSE** is completely open, free version with multiple desktop packages similar to CentOS and Linux Mint.

#### Debian

support AMD and Intel. 

came up with its own package management system on the `.deb` file format.

**Ubuntu** is the most popular Debain-derived distributions. Ubuntu has several different variants for desktop, server and various specialized applications.

**Linux Mint** rely upon Ubuntu repositories. But some include proprietary codes.

#### Android

Android use the Dalvik virtual machine with Linux

#### Other

**Raspbian** is optimized to run on Raspberry Pi hardware. This has seen significant use in training for programmers and hardware designers at all levels.

**Linux from Scratch(LFS)** is more of a learning tool than a working distribution. 



### 2.4.2 Embedded Systems

 Linux's flexibility support hardware products to be full used.



## Working in Linux

### 3.1 Navigating the Linux Desktop

download a major distribution and load it onto a PC

configure things and familiarizing yourself with Linux GUI,

the next step learning how to perform tasks from the command line

#### 3.1.1 getting into command line

you need to access the command line on systems that boot to a GUI.

- GUI-based terminal
- virtual terminal



> 中间我选择安装WSL2，用来进行Linux的学习，以下是操作记录
>
> 1. 启用“适用于Linux的Windows系统”
> 2. 启用”虚拟机平台“
> 3. windows操作系统版本确认高于18363.1049
> 4. 管理员身份打开windowsPowershell
> 5. 输入dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> 6. 输入dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> 7. 重启
> 8. 下载适用于x64计算机的WSL2 Linux内核更新包
> 9. 将WSL2设置为默认版本   wsl --set-default-version 2
> 10. 安装Ubuntu 22.04 LTS ，从Microsoft Store上下载的
> 11. 启动安装好的Linux Distribution，设置用户名与密码



### 3.2 Applications

application make requests to the kernel, and in return receive resources, such as memory, CPU, and disk space.

Kernel can kill application to prevent a crash.

Application only follows the kernel's Application Programming Interface(API)

An application may even need multiple processes to function, so the kernel takes care of running the processes, starting and stopping them as requested, and handing out system resources.

#### 3.2.1 Major applications

- *server applications*

  no direct interaction with monitor

- *desktop applications*

  interact directly

- *tools*

#### 3.2.2 Sever Applications

- Web Servers

  hosts content for web pages, which are viewed by a web browser using HTTP or HTTPS. It can be static or dynamic 

  Examples: WordPress -- dynamic; Apache -- dominate web server we use today; NGINX -- based out of Russia, make use of more modern UNIX kernels.

- Private Cloud Servers

- Database Servers

  Structure Query Language(SQL)

- Email Servers

  Mail Transfer Agent(MTA), Mail Delivery Agent(MDA), POP/IMAP Server

- File Sharing

  Network File System(NFS) 

  The Internet Software Consortium maintains the most popular DNS server.

  The **Lightweight Directory Access Protocol (LDAP)** is one common directory system which also powers Microsoft’s Active Directory.

  **Dynamic Host Configuration Protocol (DHCP)**

#### 3.2.3 Desktop Applications

- Email

  Thunderbird, Evolution and Kmail

- Creative

  **Blender**, **GIMP (GNU Image Manipulation Program)**, and **Audacity** which handle 3D movie creation, 2D image manipulation, and audio editing respectively.



### 3.3 Console Tools

tools for managing systems

#### 3.3.1 shells

shell is to accept commands and to pass them to the Linux kernel for execution. 

Bash is the default shell on most systems

#### 3.3.2 Text Editors

used at the console to edit configuration files.

main applications are Vim and Emacs, both of which is complicated

Therefore, Pico and Nano are available on most systems and provide very basic text editing.



### 3.4 Package Management

A package manager takes care of keeping track of which files belong to which package and even downloading updates from repositories, typically a remote server sharing out the appropriate updates for a distribution. 

#### 3.4.1 Debian package management

`dpkg` command

`apt-get` command

#### 3.4.2 RPM Package management

According to the Linux Standard Base, the standard package management system is RPM.

 This system is what distributions derived from Red Hat, including CentOS and Fedora, use to manage software.

 SUSE, OpenSUSE, and Arch, also use RPM.

`rpm` command

`yum` and `up2date` automate the process of resolving dependency issues.

There are also GUI-based front-end tools such as **Yumex** and **Gnome PackageKit** that also make RPM package management easier.

Some RPM-based distributions have implemented the **ZYpp** (or **libzypp**) package management style

The `zypper` command is the basis of the ZYpp method

### 3.5 Development Languages

Perl, Ruby, Python

### 3.6 Security

cookies

#### 3.6.1 Password issues

`root` is the most privileged user in Linux systems.

However the first account is `adminstrator` as the first line of defense against intrusion.

Passwords needs to be complicated enough

#### 3.6.2 Protect yourself

**KeePassX** to generate passwords

If you are using Ubuntu, then the **Gufw** is a graphical interface to **Ubuntu’s Uncomplicated Firewall (UFW)**

#### 3.6.3 Privacy Tools

One well-known example is the **HyperText Transfer Protocol Secure (HTTPS)** standard used on web servers to ensure that data transmitted between users and online resources cannot be intercepted as it travels on the open Internet.

*Virtual private networks (VPN)* to connect remote server

### 3.7 The Cloud

- Public Cloud
- Private Cloud
- Community Cloud
- Hybrid Cloud

#### 3.7.1 Linux In The Cloud

plays a pivotal role in cloud computing

- **Flexibility**
- **Accessibility**
- **Manageability**
- **Security**
- **Virtualization**
- **Containers and Bare Metal Deployments**



> 从此处开始更改Linux学习方案，打算跟着b站的网课过一遍Linux



## CHAPTER 1

### 安装虚拟机

注意安装完成vmware之后，检查windows设置，打开网络，检查高级网路设置中的网络适配器，在其中检查是否有以`net1`和`net8`为后缀的vmware网卡，如果没有则属于安装失败，需要重新进行安装。

### 虚拟机安装Linux

使用`centOS`操作系统学习

`https://vault.centos.org/7.6.1810/isos/x86_64/`

### 远程连接Linux操作系统

实现Linux的使用，如果通过VMware，各类操作会显得不方便。

此时借助第三方软件FinalShell操作Linux系统，即远程连接

空白处右键，选择打开终端

输入`ifconfig`查看IP地址

在finalshell中配置远程连接即可

### 虚拟机快照

操作过程中有可能损坏操作系统，使用快照功能避免重装



## CHAPTER 2

### Linux目录结构

属于树形结构，只有一个根目录，所有文件都在该目录下面

 `linux中的路径层级关系用/表示，Windows中使用\表示路径的层级关系`

Linux开头的`/`表示根目录，后面的`/`表示层级关系

### Linux命令入门

#### 命令

命令行操作的效率更高，纯字符对系统发出操作指令。

命令是Linux程序，一个命令就是一个Linux程序，在终端中提供反馈。

#### 基础格式

`command [-options] [parameter]`

- command 命令本身
- -options 可选非必填，提供选项控制行为细节
- parameter 参数

#### ls命令

 `ls [-a -l -h] [linux路径]`

- -a -l -h 是可选的选项
- Linux路径属于可选参数
- 直接使用`ls`时，将以平铺形式列出当前工作目录下的内容

`ls`展示的是当前Linux用户下的个人账户home目录下的以个人用户名命名的文件夹的内容，每个操作用户都有一个home目录，home目录下还有一个以个人用户名命名的文件夹。

- `-a`表示all，列出全部文件，包含隐藏的文件夹
- `-l`以竖向列表形式展示并展示更多信息：权限，用户和用户组，文件大小，创建日期等
- 选项是可以组合使用的 
- `-h`选项需要与`-l`组合使用，否则没有效果，用于使文件大小变为易于阅读的形式

#### 目录切换相关命令

`cd  [Linux路径]`

如果不带参数，会回到用户home目录内

`pwd` 查看当前所在的工作目录

#### 相对路径与绝对路径

通过`pwd`获得当前工作目录的所有文件，通过`cd`加相对路径直接打开。

节省输入绝对路径的时间。

相对路径以当前目录为起点。

- `.`表示当前目录
- `..`表示上一级目录
- `~`表示home目录

#### mkdir

make directory，创建新目录

`mkdir [-P]  Linux路径`

Linux路径必填，表示要创建的文件夹的路径，相对路径与绝对路径均可

p选项可选，表示自动创建不存在的父目录，适用于创建连续多层级的目录，一次性创建多个层级。

相对路径与绝对路径的操作均可以使用

**注意！创建文件夹需要修改权限，需要确保操作均在home目录内，在home外操作涉及到权限问题。**

#### 文件操作命令 touch-cat-more

- `touch linux路径`

参数必填，表示要创建的文件路径，注意不是创建文件夹，而是创建文件。

使用`ls -l`查看库内文件，第一行中第一个字母为d的即为directory，标识为-，则为文件

- `cat Linux路径`

参数表示被查看的文件路径，相对，绝对与特殊路径符均可使用

- `more Linux路径`

more同样可以查看文件内容，但是支持翻页，内容过多时一页页演示。而cat是直接将内容全部显示出来。通过`空格`翻页，输入`q`退出。

#### 文件操作命令 cp-mv-rm

- `cp 【-r】 参数1 参数2`

  - `-r`可选，用于复制文件夹使用，表示递归（如果要复制文件夹就需要带上这个参数，否则无法成功）
  - 参数1 Linux路径，表示被复制的文件或文件夹
  - 参数2 Linux路径，表示要复制去的地方

- `mv 参数1 参数2`

  - 参数1，Linux路径，表示被移动的文件或文件夹
  - 参数2，Linux路径，表示要移动去的地方。如果目标不存在，则进行改名，确保目标存在。

- `rm 【-r -f】 参数1 参数2 .... 参数N`

  - 同`cp`命令一样，`-r`选项用于删除文件夹

  - `-f`表示force强制删除，不弹出提示确认的信息

    *普通用户删除内容不会弹出提示，只有root管理员用户删除内容才有提示，一般用户不会使用-f选项*

  - 参数1、2、3、...、N表示要删除的文件夹或文件的Linux路径，按照空格隔开。可以进行批量删除。

> `rm`命令支持通配符
>
> - `*`表示通配符，即匹配任意内容
> - `test*`表示匹配任何以test为开头的内容
> - `*test`表示匹配任何以test为结尾的内容
> - `*test*`表示匹配任何包含test的内容

**注意！`rm`是非常危险的命令，尤其是root管理员用户下的`rm -rf /`，其效果等同于在Windows上不经确认就当场执行C盘的格式化。**

#### -which-find- 命令

- `which 要查找的命令`

  命令本质上就是程序，我们可以通过which命令，查看所使用的一系列命令的程序文件存放的位置。

  命令的本体，是二进制可执行程序。

- `find 起始路径 【-name/-size +|- n[kMG]】 “被查找文件名”`

  通过该命令搜索制定的文件。

  - 起始路径表明从哪个文件夹向下搜索，如果填写`/`即为全盘搜索
  - `-name`表示以文件名的形式查找。`-size`表示以文件大小查找，+、-表示大于或小于，n表示数字，kMG表示大小单位是kb或MB或GB。
  - 写上被查找文件名，记得加双引号
  - 被查找文件名，支持使用通配符进行模糊查询。通配符的用法在上个模块中已经被提及。注意外部依然加双引号。

#### -grep-wc-管道符

`grep 【-n】 关键字 文件路径`

从文件中通过关键字过滤文件行

- 选项-n可选，表示在结果中显示匹配的行的行号
- 关键字，表示过滤的关键字，建议用`“”`把关键字包围
- 文件路径，表示要过滤内容，*可作为内容输入端口*

`wc 【-c -m -l -w】 文件路径`

统计文件的行数、单词数量等

- -c：统计bytes数量
- -m：统计字符数量
- -l：统计行数
- -w：统计单词数量
- 文件路径：被统计的文件，*可作为内容输入输出端口*

**管道符**

`|`键即为管道符

含义：将管道符左边命令的结果，作为右边命令的输入

注意，管道符可以嵌套使用，从左向右结合输出。

### echo-tail-重定向符

`echo 输出的内容`

在命令行内输出指定输出内容，建议使用双引号包围输出内容。

有时候我们有echo命令的需求，会运用`反引号`输出内容，反引号包围的内容会被作为命令执行。

`重定向符`

- `>`将左侧命令的结果，覆盖写入符号右侧文件
- `>>`将左侧命令的结果，追加写入符号右侧文件
- 只要是结果都能写

`tail 【-f -num】 Linux路径`

查看文件尾部内容，跟踪文件最新更改

- -f：表示持续跟踪
- -num：表示查看尾部多少行，不填写时默认10行
- Linux路径，表示被跟踪的文件路径

### VI/vim编辑器

vi是Linux中的文本编辑器，是命令行下对文本编辑的软件。

vim是vi的加强版，兼容vi的所有指令，而且具有shell程序编辑的功能。

- command mode

  不能自由进行文本编辑，所有写下的文本被理解为命令，驱动不同功能

- insert mode

  编辑模式，对文件内容进行自由编辑

- last line mode

  以`：`开始，通常用于文件的保存，退出

- 三个mode是vim的工作模式

`vim 文件路径`

- 如果文件路径保存的文件不存在 则此命令编辑新文件
- 如果存在，编辑已存在文件
- 一些command mode快捷指令![image-20240119121140698](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240119121140698.png)

`i/a/o/esc`

- i：当前光标位置进行输入模式
- a：当前光标位置之后假如输入模式
- I：当前行的开头输入
- A：当前行的结尾输入
- o：当前光标下一行输入
- O：当前光标上一行输入
- esc：返回command mode

`：`

进入last line mode和相关命令

![image-20240119121411951](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240119121411951.png)



## CHAPTER 3

### Linux的root用户

root表示超级管理员，拥有系统最大的系统操作权限，普通用户只在home目录内不受限。  

`su 【-】 【用户名】`

即switch user

- `-`符号是可选的，表示是否在切换用户后加载环境变量，建议带上
- 用户名表示要切换的用户，省略时默认为root
- 通过`exit`命令返回上一个用户，或`ctrl + d`
- 使用普通用户切换到其它用户，需要密码
- 使用root用户切换到其它用户，不需要密码

`sudo 其它命令`

暂时给普通命令以root授权

注意需要为普通用户配置root认证 

root用户下使用`visudo`，按`G`跳到行尾，并进入编辑模式，添加一行

`【用户名】 ALL=(ALL)	NOPASSWD:ALL`

之后回到命令模式，并`：wq`保存退出，配置认证完成，取消认证只需重复步骤，并删除添加的一行，保存退出即可。

### 用户与用户组

Linux系统可以

- 配置多个用户
- 配置多个用户组
- 用户可以加入多个用户组中

Linux关于权限管控的级别

- 针对用户的权限控制
- 针对某用户组的权限控制

**以下命令需root用户执行**

#### 用户组管理

- 创建用户组

  `groupadd 用户组名`

- 删除用户组

  `groupdel 用户组名`

#### 用户管理

- 创建用户

  `useradd 用户名 【-g -d】`

  - -g：指定用户的组，不指定会创建同名组并自动加入，指定时需要组已经存在
  - -d：指定用户HOME路径，不指定默认在`/home/用户名`

- 删除用户

  `userdel 【-r】 用户名`

  - -r：删除用户的HOME目录，不使用该选项时，home目录保留

- 查看用户所属组

  `id 用户名`

  - 参数：用户名，被查看的用户，不提供则查看自身

- 修改用户所属组

  `usermod -aG 用户组 用户名`

  将指定用户加入指定用户组，注意，一个用户可以属于多个组，原属组别仍然保留。这不是单纯的移动组，而是复制到某个指定组中。

#### getent

查看当前系统中有哪些用户

`getent passwd`

查看有哪些组

`getent group`

### 查看权限控制信息

通过`ls -l`可以通过列表形式查看内容并显示权限细节

第一列，表示文件、文件夹权限控制信息

第三列，表示所属用户

第四列，表示所属用户组

#### 认知权限信息

![image-20240119145437025](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240119145437025.png)



- r：读权限，可查看文件内容或文件夹内容
- w：写权限，可以修改文件，或在文件夹内进行一系列操作
- x：执行权限，可以将文件作为程序执行，或者更改工作目录到此文件夹，即cd进入。

### chmod命令

`chmod 【-R】 权限 文件或文件夹`

*只有文件、文件夹所属用户和root用户可以修改权限信息*

- 选项-r：对文件夹内全部内容应用相同操作

- 示例：`chmod -R u=rwx,g=rx,o=x hello`

  ![image-20240119152843957](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240119152843957.png)

r=4，w=2，x=1，加法组合即可。

### chown命令

*只有root用户可以执行该命令*，用于修改文件、文件夹所属用户和用户组

`chown 【-R】 【用户】【：】【用户组】 文件或文件夹`

- -R对文件夹内所有内容应用
- 用户：修改所属用户
- 用户组：修改所属用户组
- `：`用于分割用户和用户组，只修改组时记得加上冒号



## CHAPTER 4

### 各类小技巧快捷键

`ctrl+c`

强制停止程序运行，或者写错命令时直接退出命令输出

`ctrl+d`

- 退出账户登录
- 退出某些特定程序的专属页面
- 不能用于退出vi/vim

`history`

找到历史输入过的命令

或者用**感叹号**作为前缀**加字符**，直接执行字符匹配上的命令

`ctrl+r`

输入内容匹配历史命令

- 回车键直接执行
- 键盘左右键，可以得到此命令（不执行）

`ctrl+a`

跳到命令开头

`ctrl+e`

跳到命令结尾

`ctrl+键盘左键`

向左跳一个单词

`ctrl+键盘右键`

向右跳一个单词

`clear（注：命令）`  `ctrl+l`

清空终端内容

### 软件安装

#### yum为centos安装

`yum`，RPM包软件管理器，用于自动化安装配置Linux软件，并且可以自动解决依赖问题。

`yum 【-y】 【install|remove|search】 软件名称`

- 选项-y：自动确认，无需手动确认安装或卸载过程
- install：安装
- remove：卸载
- search：搜索

*`yum`命令需要root权限，可以使用sudo授权或su切换到root，且yum命令需要联网。Linux的软件安装包的后缀即为rpm*

#### apt为ubuntu安装

软件安装中centos与Ubuntu使用了不同的包管理器，用法与yum保持基本一致，同样需要root权限。

`apt 【-y】 【install|remove|search】 软件名称`

- 选项-y：自动确认，无需手动确认安装或卸载过程
- install：安装
- remove：卸载
- search：搜索

### systemctl命令

`systemctl start/stop/status/enable/disable 服务名`

内置或第三方软件支持该命令控制

- network manager 主网络服务
- network 副网络服务
- firewalld 防火墙服务
- sshd，ssh服务，即final shell远程登录Linux使用的服务

`yum install -y ntp`

安装ntp，通过ntpd服务名，配合systemctl控制

`yum install -y httpd`

安装apache服务器软件，通过httpd服务名，配合systemctl进行控制

### 软链接

`ln -s 参数1 参数2`

相当于快捷方式，将文件与文件夹链接到其它位置。

链接只是一个指向，不是物理移动。

- -s，表示创建软链接

- 参数1：被链接的文件或文件夹
- 参数2：要链接去的目的地 

### 日期与时区

`date 【-d】 【+格式化字符串】`

- -d，按照给定的字符串显示日期，一般用于日期计算
- 格式化字符串：通过特定的字符串标记，来控制显示的日期格式

![image-20240120114943826](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240120114943826.png)

#### date命令进行日期加减

![image-20240120115444826](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240120115444826.png)

#### 校准时间

`yum -y install ntp`

`systemctl start ntp`

`systemctl enable ntp`

自动联网校准系统时间

也可以手动校准：`ntpdate -u ntp.aliyun.com`

### IP地址和主机名

#### IP地址

对外联络联网的地址

`ipv4`的格式为`a.b.c.d`表示0~255的数字

`127.0.0.1`指代本机

`0.0.0.0`

- 可以用于指代本机
- 可以在端口绑定中用来确定绑定关系
- 在一些IP地址限制中，表示所有IP的意思，如放行规则设置为0.0.0.0表示允许任意IP访问

#### 主机名

为系统设置主机名

`hostname`

查看主机名

`hostnamectl set-hostname 主机名`

需要root，重新修改主机名

#### 域名解析

先检查本地host文件查看是否有IP地址记录，再看DNS服务器是否有记录ip地址。



![image-20240120135949994](D:\文档文本编辑\markdown_notes\LinuxNote\image-20240120135949994.png)



### 配置固定ip

#### 在VMware Workstation中配置IP地址网关和网段
自行查阅资料解决问题。

### 网络请求与下载
#### ping命令
`ping 【-c num】 ip或主机名`
- 选项-c表示检查的次数
- 参数： IP或主机名称，被检查的服务器ip地址或主机地址
#### wget命令
`wget 【-b】 url`
非交互式的文件下载器，可以在命令行内下载网络文件
- 选项-b，后台下载，将日志写入到当前工作目录的wget-log文件
- 参数url，下载链接
#### curl命令
`curl 【-O】 url`
用于发送http网络请求，可用于下载文件与获取信息
- 选项-O用于下载文件，当url是下载链接时，可以使用此选项保存文件
- 参数url，要发起请求的网络地址
### 端口
#### 端口概念
端口是设备与外界通讯交流的出入口，端口可以分为物理端口和虚拟端口。
- 物理端口：又称为接口，是可见的端口，如USB接口，RJ45网口，HDMI端口等
- 虚拟端口：计算机内部的端口，不可见，用来是操作系统和外部进行交互使用的。
计算机程序之间的通讯，通过IP只能锁定计算机，但是无法锁定具体的程序，通过端口，可以锁定计算机上具体的程序。
##### Linux端口
- 公认端口：1~1023，用于一些系统内置或知名程序的预留使用，如SSH服务的22端口，HTTPS服务的443端口。
- 注册端口：1024~49151，通常可以随意使用，松散绑定一些程序、服务
- 动态端口：49152~65535，通常不绑定固定程序，而是当程序对外部进行网络链接时，用于临时使用
#### 查看端口占用
`sudo yum -y install nmap`  
`nmap IP地址`
查看ip的对外暴露端口
`sudo yum install net-tools`
`netstat -anp|grep 端口号`
查看本机指定端口号的占用情况
### 进程管理
#### 进程
为管理运行的程序，每一个程序在运行时，被操作系统注册为一个进程，并为每一个进程分配一个独有的进程id
#### 查看进程
`ps 【-e -f】`
- 选项-e：显示出全部的进程
- 选项-f：以完全格式化的形式展示信息
- 一般来说`ps -ef`用于列出全部进程的全部信息  
- 常用管道符与grep过滤出具体信息
#### 关闭进程
`kill 【-9】 进程ID`
- 选项-9：表示强制关闭，不使用此选项，会向进程发送信号要求其关闭，但是否关闭会看程序自身的处理机制。

### 主机状态
`top -选项`
查看CPU、内存等运行情况，默认每五秒刷新一次。 
选项建议自行查阅，top的命令非常多，在top中按下h可以查看交互式选项命令。
`df [-h]`
查看硬盘使用情况，选项-h以更加人性化的单位显示
`iostat [-x] [num1] [num2]`
查看CPU、磁盘的相关信息
- 选项-x，显示更多信息
- num1：数字，刷新间隔
- num2：数字，刷新次数
`sar -n DEV num1 num2`
可以使用sar命令查看网络的相关统计，实际上sar命令非常复杂，这里仅用于统计网络
- 选项-n：表示查看网络，DEV表示查看网络接口
- num1：刷新间隔
- num2：查看次数
### 环境变量
`env`
查看环境变量
无论当前工作目录是什么，都能执行某个文件路径中的程序的原因，是借用了环境变量中`PATH`这个项目的值做到的。
它记录了系统执行任何命令的搜索路径。
#### $符号
在Linux系统中，$符号被用于取“变量”的值 
#### 自行设置环境变量
`export 变量名=变量值`
`export PATH=$PATH:自定义路径`

配置在所有用户时
`vim /etc/profile`
在文件中结尾添加export
`source /etc/profile`
通过source命令立刻生效

配置在一个用户时
`vim .bashrc `
之后同理

### 上传与下载
`yum -y install lrzsz`
安装rz、sz命令
`rz`
直接输入即可上传
`sz 要下载的文件`
文件会自动下载到桌面的`fsdownload`文件夹中

### 压缩与解压
`tar 【-c -v -x -f -z -C】 参数1 参数2...参数N`
注意，tar只有归档效果，其实没有压缩的效果
- 选项-c创建压缩文件
- -v显示压缩解压过程
- -x解压模式
- -f必须在最后一个，后接创建或解压的文件
- -z，gzip格式，否则是tarball，建议在开头使用
- -C，在前面的选项写完的后面，单独使用选择解压目的地，用于解压模式

`zip 【-r】 参数1 参数2 .... 参数3`
- -r在要包含文件夹时使用
- 参数1为压缩后的文件，最终格式为zip压缩包。
- 之后的参数为要压缩的文件

`unzip 【-d】 参数`
- -d指定要解压的位置，同tar的-C选项
- 参数，被解压的zip压缩包文件

## CHAPTER 5 部署Linux软件
### 前言
通过部署软件熟悉Linux系统操作。
#### MySQL部署
简单记录一下安装日志，就不详细记录了。
一切操作前提是需要登录root用户。
1. 配置yum仓库
- 更新密钥
- 安装MySQL yum库

