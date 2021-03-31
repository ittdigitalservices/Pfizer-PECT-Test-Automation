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
    visit_our_research_page = "//*[contains(text(), 'Visit Our Research')]"
    vaccines = "//*[contains(text(), 'Vaccines')]"
    coronavirus_COVID_2019 = "//*[contains(text(), 'Coronavirus (COVID-19)')]"
    rights_as_a_participant = "//*[contains(text(), 'rights as a participant')]"
    clinical_trial_participants_text = "//*[contains(text(), 'Clinical trial participants are our priority')]"
    pfizer_research_vaccines = "//*[contains(text(), 'Vaccines')]"
    respiratory_diseases = "//*[contains(text(), 'Respiratory ')]"
    trial_for_respiratory_diseases = "//*[@class='items-count-wrapper']"
    research_page_text_content = "//*[contains(text(), 'Pfizer’s focus in clinical research')]"
    pfizer_video = "//*[@class='start-video']"
    pfizer_contact_us = "//*[@class='contact-us']"
    pfizer_clinical_trial_faqs = "//*[contains(text(), 'FAQs')]"
    pfizer_frequently_asked_questions = "//*[contains(text(), 'Frequently asked questions')]"
    pfizer_search_faqs = "//*[@class='fq-search-input']"
    pfizer_search_faq_form_field = "//*[@class='form-text form-control']"
    pfizer_faqs_expand_all = "//span[@class='toggle-fqs fq-button' and contains(text(), 'Expand')]"
    pfizer_faqs_collapse_all = "//span[@class='toggle-fqs fq-button collapse' and contains(text(), 'Collapse')]"
    pfizer_internal_medicine_link = "//*[contains(text(), 'Internal Medicine')]"
    pfizer_internal_medicine_clinical_trials = "//*[contains(text(), 'clinical trials in internal medicine')]"
    internal_medicine_covid = "//span/a[contains(text(), 'COVID')]"
    pfizer_thumbs_up_label = "//*[@class='form-item js-form-item form-type-radio js-form-type-radio form-item-value js-form-item-value rating-label thumbsupdown-rating-label thumbsupdown-rating-label-up']"
    pfizer_thumbs_down_label = "//*[@class='form-item js-form-item form-type-radio js-form-type-radio form-item-value js-form-item-value rating-label thumbsupdown-rating-label thumbsupdown-rating-label-down']"
    pfizer_email = "//*[@id='share-mail' and contains(text(), 'Email')]"
    pfizer_print = "//*[contains(text(), 'Print')]"

