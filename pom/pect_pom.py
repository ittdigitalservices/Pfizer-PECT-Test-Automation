from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


"""This Class is for PECT PageObjectModel"""
class PECT_WebElement_Locators:
    home_page_logo = "//*[@id='slide-navbar-collapse']/li[1]/div/a"
    """//a[img]"""
    # "//*[@id='block-myclinicaltrial-branding']/a/img"
    pfizer_home_image = "//*[@id='block-myclinicaltrial-branding']/a/img"
    home_page_text = "//*[@id='block-homepagehero']/div[2]/div/h1"
    pfizer_find_a_trial_navbar = "//*[@id='slide-navbar-collapse']/li[*]/div/a[contains(text(), 'Find a trial')]"
    pfizer_show_filters_link = "//*[@class='filters-showing-btn' and contains(text(), 'Show Filters')]"
    pfizer_find_a_trial_search_filter = "//*[@id='edit-search-flexdatalist']"
    pfizer_find_a_trial_search_filter_result = "//*[@class='items-count-wrapper']"
    pfizer_find_trial_button = "//*[@id='submit-pf-clinical-trial-search']"
    pfizer_COVID_19_trial_info_text = "//*[contains(text(), 'COVID-19 clinical')]"
    find_pfizer_COVID_19_trial_info = "//*[contains(text(), 'Find Pfizer clinical trials')]"
    about_clinical_trials = "//*[contains(text(), 'About clinical trials')]"
    about_clinical_trials_text = "//h3[contains(text(), 'About \n"+"<br>clinical trials')]"
    about_clinical_trials_link = "//*[contains(text(), 'About clinical trials')]"
    #"//href[contains(text(), '/about-clinical-trials')]"
    agree_to_accept_cookies = "//*[@id='_evidon-accept-button']"
    how_clinical_trial_works = "//*[contains(text(), 'How clinical trials work')]"
    our_research = "//*[contains(text(), 'Our research')]"
    vaccines = "//*[contains(text(), 'Vaccines')]"
    coronavirus_COVID_2019 = "//*[contains(text(), 'Coronavirus (COVID-19)')]"

