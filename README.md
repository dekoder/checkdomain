# Checkdomain

基于对收集得到的众多子域名进行有选择筛选的探测工具



## 要求

- python 2.7
- 推荐搭配lijiejie的subdoamin生成

## 使用

1. `git clone https://github.com/Imanfeng/checkdomain.git`

2. `cd checkdomain`

3. ```

    ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
   ██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
   ██║     █████╔╝ ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
   ██║     ██╔═██╗ ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
   ╚██████╗██║  ██╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
    ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


                   V-2.2 # Modified By z3r0yu

   usage: checkDomain.py [-h] [-p] [-f]

   Example:python checkDomain.py -f alimama.txt -p 80,443,8080,7001

   OPTIONS:
     -h, --help       show this help message and exit
     -p , --port      choose a port or ports
     -f , --file      choose a subdomain txt
   ```


## 版本
- v-1.0 支持读取指定格式子域名文件，指定单端口单线程扫描，默认文件输出
- v-2.0 支持空格加逗号分隔的子域名文件，多端口多线程扫描，默认输出为out.xxx.txt
- v-2.2 输出格式进行了修改，方便导入awvs，文件默认进行了输出，修改了探测https的bug
