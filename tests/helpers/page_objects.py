import urlparse
from tests.helpers.components import AuthForm, TopMenu, BaseSettings, CreateButton, BannerForm, \
    CampaignData, CampaignEdit, CampaignDelete, EditData


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_settings(self):
        return BaseSettings(self.driver)

    @property
    def banner_form(self):
        return BannerForm(self.driver)

    @property
    def edit_data(self):
        return EditData(self.driver)

    @property
    def create_button(self):
        return CreateButton(self.driver)


class CampaignPage(Page):
    PATH = '/ads/campaigns'

    @property
    def campaign_data(self):
        return CampaignData(self.driver)

    @property
    def campaign_edit(self):
        return CampaignEdit(self.driver)

    @property
    def campaign_delete(self):
        return CampaignDelete(self.driver)


class EditPage(Page):

    @property
    def edit_data(self):
        return EditData(self.driver)

    @property
    def submit(self):
        return CreateButton(self.driver)
