1.isbn两种形式
  1.1 isbn13 13个0-9的数字组成
  1.2 isbn10 10个0-9的数字组成,其中包括一些 ' - '字符

2.isdigit() 判断是否为数字的函数

3.# 视图函数
@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.baidu.com'
    }
    # 方式1
    # response = make_response('hello world', 301)
    # response.headers = headers
    # return response
    # 方式2
    return 'hello world', 301, headers

4.多个判断条件时,应该把可能性为假的判断放在前面,可提升代码效率.

5.视图函数是web项目的入口或者起点.

6.测试API  http://t.yushu.im/v2/book/isbn/9787501524044
          http://t.yushu.im/v2/book/search?q=红楼梦
          http://localhost:81/book/search/9787501524044/1
          http://localhost:81/book/search?q=9787501524044&page=1
          http://localhost:81/book/search?q=红楼梦&page=2
          http://localhost:81/book/search?q=9787070511209

7.做忘记密码发送邮件时,测试发送邮件,邮箱需要是已经本项目服务器注册的邮箱.否则send_email 不会被执行,404 错误