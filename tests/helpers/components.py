from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class CreateButton(Component):
    CREATE_BUTTON = '.main-button-new'

    def click(self):
        self.driver.find_element_by_css_selector(self.CREATE_BUTTON).click()


class BaseSettings(Component):
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    PRODUCT_TYPE = '#product-type-6039'
    PADS_TARGETING = '#pad-mobile_app_mobile_service'

    def set_campaign_name(self, name):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        element.clear()
        element.send_keys(name)

    def set_product_type(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def set_pad_targeting(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGETING)
        )
        element.click()


class BannerForm(Component):
    URL = '.banner-form__input'
    IMAGE = 'input[data-name="image"]'
    SAVE_BUTTON = '.banner-form__save-button'
    RESET_BUTTON = '.banner-form__reset'

    def set_url(self, url):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )
        for url_input in elements:
            if url_input.is_displayed():
                url_input.send_keys(url)

    def set_image(self, img_path):
        banner_form_img = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        )
        banner_form_img.send_keys(img_path)

        save_img_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SAVE_BUTTON)
        )
        save_img_button.click()


class CampaignData(Component):

    NAME = '.campaign-title__name'
    ID = '.campaign-title__id'
    SETTINGS = '.campaign-title__settings'
    PADS = '.campaign-settings-list__targeting__value .js-campaign-settings-value'

    def get_name(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.NAME)
        )
        return element.text

    def get_id(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ID)
        )
        return element.text

    def get_sex(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SETTINGS)
        )
        return element.text.split(',')[0]

    def get_country(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SETTINGS)
        )
        return element.text.split(',')[2]

    def county_is_null(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SETTINGS)
        )
        settings = element.text.split(',')
        return len(settings)


class CampaignEdit(Component):

    EDIT_BUTTON = '.control__link_edit'

    def click_edit(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.EDIT_BUTTON)
        )
        element.click()


class CampaignDelete(Component):

    DELETE_BUTTON = '.control__preset_delete'

    def click_delete(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.DELETE_BUTTON)
        )
        element.click()


class EditData(Component):

    SEX = '.campaign-setting__value'
    SEX_M = '#sex-M'
    SEX_F = '#sex-F'

    COUNTRY_RUSSIA = '//*[@id="regions188"]/input'

    def set_sex(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.SEX)
        )
        element.click()

    def set_sex_m(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_M)
        )
        element.click()

    def set_sex_f(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_F)
        )
        element.click()

    def choose_country(self):

        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COUNTRY_RUSSIA)
        )
        element.click()



