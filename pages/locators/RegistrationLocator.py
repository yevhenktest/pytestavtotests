from selenium.webdriver.common.by import By

class RegistrationLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    REGISTRATION_BTN = (By.XPATH, '/html/body/div[1]/main/div[4]/div[5]/form/div[4]/button')
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'li.auth-nav__item.auth-nav__item-registration')
    REGISTRATION_CH1 = (By.CSS_SELECTOR, 'div.checkbox')
    REGISTRATION_CH2 = (By.CSS_SELECTOR, '#clientRegistrationForm > div.global_instance_registration > div:nth-child(1) > fieldset.inform-user > div.education.education-background-non > div:nth-child(2) > label')
    REGISTRATION_CH3 = (By.CSS_SELECTOR, '#clientRegistrationForm > div.global_instance_registration > div:nth-child(1) > fieldset.inform-user > div.education.education-background-non > div:nth-child(3) > label')
    REGISTRATION_CH4 = (By.CSS_SELECTOR, '#clientRegistrationForm > div.global_instance_registration > div:nth-child(1) > fieldset.inform-user > div.education.education-background-non > div:nth-child(4) > label')
    REGISTRATION_EDUCATION = ("id", 'my_userclient__registration_form_customEducationName')
    REGISTRATION_FIRSTNAME = ("id", 'my_userclient__registration_form_username')
    REGISTRATION_LASTNAME = ("id", 'my_userclient__registration_form_lastName')
    REGISTRATION_COUNTRY = ("id", 'my_userclient__registration_form_countryObject')
    REGISTRATION_CITY = ("id", 'my_userclient__registration_form_city')
    REGISTRATION_TELEPHONE = ("id", 'my_userclient__registration_form_phone')
    REGISTRATION_EMAIL = ("id", 'my_userclient__registration_form_email')
    REGISTRATION_PASSWORD = ("id", 'my_userclient__registration_form_plainPassword_first')
    REGISTRATION_CONFIRMPASSWORD = ("id", 'my_userclient__registration_form_plainPassword_second')
    REGISTRATION_BTN_SUBMIT = (By.CSS_SELECTOR, 'button[type = "submit"]')