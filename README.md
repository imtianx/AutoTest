# Appium + Python2.7 实现自动化操作

> 通过 `python` 做一些自动化操作，模拟用户行为，如搜索商品进行购买等。

这里本来要完成模拟用户登陆，然后购买搜索的指定商品，由于第三方授权登陆暂时无法越过，只实现了部分功能。

## 1.安装 [Appium](https://github.com/appium/appium-desktop) 框架

此处安装的 Mac 上的 desktop 版本，使用时只需连接手机，启动客户端，配置相关参数即可。具体操作参见[https://github.com/appium/appium-desktop](https://github.com/appium/appium-desktop)

## 2.编写测试代码 

使用 PyCharm 编写测试代码，python2.7 ,需要安装 [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/) 。然后即可导入使用,代码可参考：[main_tjj.py](https://github.com/imtianx/AutoTest/blob/master/src/main_tjj.py)

可以启动 appium 客户端查看对应 UI 控件的 id/name/xpath/class 等(或者使用 android sdk 中的 `uiautomatorviewer` 工具，在 `sdk/tools/bin/` 下)，然后使用 **webdriver** 来进行相关的操作。

需要注意的，测试中获取 Recyclerview 的列表，只能通过下面的方式：

```
 webdriver.find_elements_by_xpath(
        "//android.support.v7.widget.RecyclerView/*[@class='android.widget.RelativeLayout']")
```


## 3.执行测试

需要先启动 appium 客户端，然后运行 py 代码，其中需要提前配置 webdriver 的相关参数，如下：

```
{
  "deviceName": "4CBDU17601004905",
  "automationName": "Appium",
  "platformName": "Android",
  "platformVersion": "8.0",
  "appPackage": "com.huanshou.taojj",
  "appActivity": "com.app.shanjiang.main.HomeActivity",
  "unicodeKeyboard": true,
  "resetKeyboard": true,
  "noReset": true,
  "autoAcceptAlerts": true
}
```

> unicodeKeyboard ：使用 appium 键盘
noReset : 不用每次执行都重置
autoAcceptAlerts ：自动允许权限

如果真机跑完测试后，使用时无法吊起键盘，只需 卸载 `appium setting` 这个 app。

## 存在的问题
qq/wechat 等安全机制，无法模拟登陆；对于授权登陆暂时无法模拟。


