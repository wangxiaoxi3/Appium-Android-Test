# Android-UI自动化开源框架


---

## 一、环境部署
#### Python3:

	brew install python3
	pip3 install Appium-Python-Client
    pip3 install Jinja2
    pip3 install PyYAML
    pip3 install pytest
    pip3 install pytest-allure-adaptor


#### Appium：

	npm install -g appium
	npm install -g appium-doctor

---

## 二、Jenkins定时运行

#### 1、start appium service:

	appium --address 127.0.0.1 --port 4723 --log "log_path" --log-timestamp --local-timezone --session-override


#### 2、Jenkins构建
    当打包工程构建成功后，当前工程自动开始构建，构建成功生成Allure Report，并发送邮件。
    登入Jenkins即可查看Allure Report。
    具体配置请参照Jenkins工程。

---


## 三、编写测试case

```python
class TestLogin:
    @pytest.allure.feature('Login')
    def test_fb_login(self, action: ElementActions):
        L.d('test_fb_login')
        action.click(LoginPage.fb)
        action.sleep(10)
        action.back_press()
        action.click(MainPage.nav_drawer)
        assert action.is_text_displayed('papaya')
```



