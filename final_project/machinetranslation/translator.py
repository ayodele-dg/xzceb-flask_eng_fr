import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('2kTYncjsq2C1aFa8liauUNAbjDhwzeCHIcQ7ke11k24Z')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    #write the code here
    """
    This function translates English to French and returns French text
    """
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    #write the code here
    """
    This function translates English to French and returns French text
    """
    english_text = language_translator.translate(
    text='Hello, how are you today?',
    model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text
