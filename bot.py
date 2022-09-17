import os
import uuid
import random
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from faker import Faker

from chave import chave_api
from options_vpn import optionsCitiesToConect

linkWebsite = 'https://nlw.rocketseat.com.br/invite/arthur-79600'

def main():
  fake = Faker('pt_BR')

  while True:
      browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
      browser.get(linkWebsite)

      # fill input name
      nameToFillInput = fake.name()
      inputName = browser.find_element(By.XPATH, '//*[@id="name-5"]')
      inputName.send_keys(nameToFillInput)

      # fill input phone number
      numberToFillInput = fake.phone_number()
      inputNumber = browser.find_element(By.XPATH, '//*[@id="field"]')
      inputNumber.send_keys(numberToFillInput)

      # fill email name
      emailToFillInput = fake.email()
      inputEmail = browser.find_element(By.XPATH, '//*[@id="email-6"]')
      inputEmail.send_keys(emailToFillInput)

      # select option experience
      optionToSelect = browser.find_element(By.XPATH, '//*[@id="Mais-de-2-anos"]')
      optionToSelect.click()

      # starting resolving captcha
      key_captcha = browser.find_element(By.XPATH, '//*[@id="gtm-inscricao-section_six-form-subscribe-embarcar-na-missao"]/div[3]').get_attribute('data-sitekey')

      solver = recaptchaV2Proxyless()
      solver.set_verbose(1)
      solver.set_key(chave_api)
      solver.set_website_url(linkWebsite)
      solver.set_website_key(key_captcha)

      response = solver.solve_and_return_solution()

      if response != 0:
          print(response)

          # to fill captcha input
          browser.execute_script(f"document.getElementById('g-recaptcha-response-1').innerHTML = '{response}'")

          optionToSelect = browser.find_element(By.XPATH, '//*[@id="gtm-inscricao-section_six-form-subscribe-embarcar-na-missao"]/input[4]')
          optionToSelect.click()

          sleep(10)

          if browser.title == 'Next Level Week - eSports | Rocketseat':
            browser.quit()
            main()
          else:
            browser.quit()
            main()
      else:
        print(solver.err_string)

      sleep(100)
