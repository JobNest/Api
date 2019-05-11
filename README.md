# Api
在线接口API
## 环境依赖

- python3
- flask
- requests
- yaml
- uwsgi

### uwsgi 缺少运行库
可以先 type 查询 uwsgi的路径，然后ldd 这个路径，查看uwsgi缺少的库。

都可以在anaconda3的库里找到，建立软连接到/usr/lib64。

另外如果系统的libstdc++.so.6版本过低，也可以从anaconda的lib里找到libstdc++.so.6建立软连接。

## 启动uwsgi
```
uwsgi --ini conf/uwsgiconfig.ini
```
