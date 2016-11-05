微信消息管理模块
================

基于django-wechat-base的简单微信消息管理模块

快速开始:
---------

安装django-wechat-message:

.. code-block::

    pip install django-wechat-message

修改settings.py文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'wechat',
        'wechat_message',
        ...
    )

在settings.py文件底部添加:

.. code-block::

    # wechat config
    WECHAT = [
        {
            'appid': 'demo',
            'appsecret': 'demo',
            'token': 'demo',
        },
    ]

修改urls.py文件:

.. code-block::

    urlpatterns = [
        ...
        url(r'^wx/', include('wechat_message.urls', namespace='wx')),
        ...
    ]


版本更改:
---------
- v1.0 使用统一的xml回复
