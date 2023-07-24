from selenium.webdriver.common.by import By

class FeedbackLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    PRODUCTS_BTN_MENU = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[2]/a')
    LOGIN_BTN_CLICK = (By.XPATH, '/html/body/div[3]/div[3]/a[1]')
    LOGIN_USER_NAME = (By.CSS_SELECTOR, 'input[data-action-type="phone-change"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[class="form-control custom-required-validation-message"]')
    LOGIN_BTN = (By.CLASS_NAME, 'al-login-form__btn')
    FEEDBACK_ALEXA_VOLUME_PRODUCT_EN = (By.XPATH, '/html/body/div[1]/main/div[5]/div[1]/div/div')
    FEEDBACK_ALEXA_VOLUME_PRODUCT_LOCALIZATION = (By.XPATH, '/html/body/div[1]/main/div[5]/div[2]/div/div/div[4]')
    FEEDBACK_DISCOUNTS_CONSTRUCTOR = (By.XPATH, '/html/body/div[1]/main/div[5]/div/div[3]/a[2]')
    FEEDBACK_overlay = (By.XPATH, '/html/body/div[3]/div[3]/a[1]')
    FEEDBACK_btn1 = (By.CLASS_NAME, 'al-login-form__btn')
    FEEDBACK_btn2 = (By.XPATH, '/html/body/div[1]/main/div[5]/div[1]/div/div')
    FEEDBACK_FULLNAME = (By.ID, 'appbundle_comment_single_guestName')
    FEEDBACK_EMAIL = (By.ID, 'appbundle_comment_single_guestEmail')
    FEEDBACK_TELEPHONE = (By.ID, 'appbundle_comment_single_guestPhone')
    FEEDBACK_COMMENT = (By.ID, 'appbundle_comment_single_comment')
    FEEDBACK_BTN_SUBMIT = (By.XPATH, '/html/body/div[1]/main/article/section/div/div/div[1]/form/div[2]/button')
    FEEDBACK_SIGNOUT_LINK = (By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/ul/li/a/span')