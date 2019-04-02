"""# googleauth



1. 安装 django-google-auth2


```
pip3 install django-google-auth2
```

2. 添加 django_google_auth2 到app

```
INSTALLED_APPS = [
        ...
        'django_google_auth2',
    ]
```

3. 绑定google令牌

```
from django_google_auth2.google.bindgoogleauth.bindgoogleauth import bind_google_auth

bind_google_auth(user)

```


**函数参数：**

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|user |是  |string | 用户名 Or 邮箱   |


 **返回参数说明**
|参数名|类型|说明|
|:-----  |:-----|-----                           |
|success |bool   | True/False |
|data |string   | google令牌字符串(用于生成二维码) |

4. 解绑google令牌

```
from django_google_auth2.google.deletegoogleauth.deletegoogleauth import delete_google_auth


delete_google_auth(user)

```


**函数参数：**

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|user |是  |string | 用户名 Or 邮箱   |

 **返回参数说明**
|参数名|类型|说明|
|:-----  |:-----|-----|
|success |bool   | True/False |
|data |string   | 删除成功 |

5. 验证google令牌

```
from django_google_auth2.google.checkgoogleauth.checkgoogleauth import check_google_auth



check_google_auth(user,code)

```

**函数参数：**

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|user |是  |string | 用户名 Or 邮箱   |
|code |是  |string | 客户端动态码    |

 **返回参数说明**
|参数名|类型|说明|
|:-----  |:-----|-----|
|success |bool   | True/False |


6. 绑定google令牌Api接口


urls.py

```
from django_google_auth2.google.bindgoogleauth.bindgoogleauthapi import bind_google_auth_api


urlpatterns = [
    ...
    path('bing-google-auth-api/', bind_google_auth_api),
]

```

**请求方式：**
- POST

 **请求示例**

```
{
	"user":"cox"
}
```

**函数参数：**

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|user |是  |string | 用户名 Or 邮箱   |

 **返回**

![20190402192923-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190402192923-image.png)


7. 客户端(二选一)

> 安卓App

Google令牌+扫码器(如果手机只安装Google令牌App扫码失败,请安装扫码器)

链接：https://pan.baidu.com/s/1XeO7p4IvNuvzQOiZrq4wtw

提取码：e70f

> Chrome插件

https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai

"""
from django.contrib import admin
from django.urls import path,include
from django_google_auth2.google.bindgoogleauth.bindgoogleauthapi import bind_google_auth_api


urlpatterns = [
    path('bing-google-auth-api/', bind_google_auth_api),
]
