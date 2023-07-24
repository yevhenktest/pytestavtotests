import pytest
from pages.MedicalTrainers import MedicalTrainer
import datetime

@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.medicaltrainer_ru
    @pytest.mark.medicaltrainer
    @pytest.mark.smoke
    def test_medicalform_ru(self):
        print("*******")
        print("TEST THE MEDICAL TRAINER FORM IN RU INSTANCE PASSED")
        print("*******")
        medicaltrainer = MedicalTrainer(self.driver)
        medicaltrainer.go_to_medical_trainer()
        medicaltrainer.clicking_localization_dropdown()
        medicaltrainer.select_ru_in_localization_dropdown()
        medicaltrainer.click_trainer_main_menu()
        medicaltrainer.click_join_button()
        medicaltrainer.scroll_page()
        medicaltrainer.click_checkbox1()
        medicaltrainer.click_checkbox2()
        medicaltrainer.input_fullname('Test')
        medicaltrainer.input_telephone(+380987654321)
        medicaltrainer.input_email('a@a.')
        medicaltrainer.input_country('Ukraine')
        screen_valid_name = f'medicaltrainer_COM_valid_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        medicaltrainer.click_submit_button()
        screen_confirm_name = f'medicaltrainer_COM_confirm_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)