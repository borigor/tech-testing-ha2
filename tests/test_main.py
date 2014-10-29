# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.helpers.page_objects import AuthPage, CreatePage, CampaignPage, EditPage


class TestMain(unittest.TestCase):

    DOMAIN = '@bk.ru'
    USERNAME = 'tech-testing-ha2-4@bk.ru'
    PASSWORD = os.environ.get('TTHA2PASSWORD', 'Pa$$w0rD-4')

    CAMPAIGN_NAME = u'CAMPAIGN_NAME'
    URL = 'play.google.com/store/apps/details?id=url'
    IMAGE = os.path.abspath('img2.jpg')

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_log_in(self):

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(self.USERNAME, email)

    def test_ads_create(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_settings
        base_settings.set_product_type()
        base_settings.set_pad_targeting()
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)

        banner_form = create_page.banner_form
        banner_form.set_image(self.IMAGE)
        banner_form.set_url(self.URL)

        create_page.create_button.click()

        campaign_page = CampaignPage(self.driver)
        campaign_data = campaign_page.campaign_data

        self.assertEqual(self.CAMPAIGN_NAME, campaign_data.get_name())
        self.assertEqual(u'М и Ж', campaign_data.get_sex())
        self.assertEqual(u' Россия', campaign_data.get_country())

        campaign_page.campaign_delete.click_delete()

    def test_set_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_settings
        base_settings.set_product_type()
        base_settings.set_pad_targeting()
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)

        banner_form = create_page.banner_form
        banner_form.set_image(self.IMAGE)
        banner_form.set_url(self.URL)

        edit_data = create_page.edit_data
        edit_data.set_sex()
        edit_data.set_sex_f()

        create_page.create_button.click()

        campaign_page = CampaignPage(self.driver)
        campaign_data = campaign_page.campaign_data

        self.assertEqual(self.CAMPAIGN_NAME, campaign_data.get_name())
        self.assertEqual(u'М', campaign_data.get_sex())
        self.assertEqual(u' Россия', campaign_data.get_country())

        campaign_page.campaign_delete.click_delete()

    def test_set_where(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_settings
        base_settings.set_product_type()
        base_settings.set_pad_targeting()
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)

        banner_form = create_page.banner_form
        banner_form.set_image(self.IMAGE)
        banner_form.set_url(self.URL)

        edit_data = create_page.edit_data
        edit_data.choose_country()

        create_page.create_button.click()

        campaign_page = CampaignPage(self.driver)
        campaign_data = campaign_page.campaign_data

        self.assertEqual(self.CAMPAIGN_NAME, campaign_data.get_name())
        self.assertEqual(u'М и Ж', campaign_data.get_sex())
        self.assertEqual(2, campaign_data.county_is_null())

        campaign_page.campaign_delete.click_delete()

    def test_create_ads_edit_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_settings
        base_settings.set_product_type()
        base_settings.set_pad_targeting()
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)

        banner_form = create_page.banner_form
        banner_form.set_image(self.IMAGE)
        banner_form.set_url(self.URL)

        create_page.create_button.click()

        campaign_page = CampaignPage(self.driver)
        campaign_page.campaign_edit.click_edit()

        edit_page = EditPage(self.driver)
        edit_data = edit_page.edit_data
        edit_data.set_sex()
        edit_data.set_sex_f()
        edit_page.submit.click()

        campaign_page = CampaignPage(self.driver)
        campaign_data = campaign_page.campaign_data

        self.assertEqual(self.CAMPAIGN_NAME, campaign_data.get_name())
        self.assertEqual(u'М', campaign_data.get_sex())
        self.assertEqual(u' Россия', campaign_data.get_country())

        campaign_page.campaign_delete.click_delete()

    def test_create_ads_edit_data(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_settings
        base_settings.set_product_type()
        base_settings.set_pad_targeting()
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)

        banner_form = create_page.banner_form
        banner_form.set_image(self.IMAGE)
        banner_form.set_url(self.URL)

        create_page.create_button.click()

        campaign_page = CampaignPage(self.driver)
        campaign_page.campaign_edit.click_edit()

        edit_page = EditPage(self.driver)
        edit_data = edit_page.edit_data
        edit_data.set_sex()
        edit_data.set_sex_f()
        edit_data.choose_country()
        edit_page.submit.click()

        campaign_page = CampaignPage(self.driver)
        campaign_data = campaign_page.campaign_data

        self.assertEqual(self.CAMPAIGN_NAME, campaign_data.get_name())
        self.assertEqual(u'М', campaign_data.get_sex())
        self.assertEqual(2, campaign_data.county_is_null())

        campaign_page.campaign_delete.click_delete()
