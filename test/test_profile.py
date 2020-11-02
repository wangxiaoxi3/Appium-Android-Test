# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午3:22
# @Author  : WangJuan
# @File    : test_profile.py

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from base.actions import ElementActions
from page.pages import *
from test.steps import login_later
from utils import L, tools
import pytest
import allure


@pytest.mark.run(order=2)
class TestProfile:

    @pytest.allure.feature('Home')
    @allure.story('profile')
    @allure.severity('normal')
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_avatar_to_profile_page(self, action: ElementActions):
        """
        验证profile页面

        """
        L.d('test_popular_narrators_to_profile_page')
        # 关闭广告
        login_later(action)
        action.click(MainPage.discover_album_name)
        action.sleep(2)
        before_user = action.get_text(AlbumDetailsPage.popular_user_name)
        action.click(AlbumDetailsPage.popular_user_view)

        try:
            after_user = action.get_text(ProfilePage.user_name)
            assert before_user == after_user

        except AssertionError:
            action.screenshot("popular_narrators_to_page_error")
            file = tools.Find.find_screen("popular_narrators_to_page_error")
            allure.attach('popular_narrators_to_page_error.png', file, allure.attach_type.PNG)
            action.quit()
            raise
