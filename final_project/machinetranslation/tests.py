import unittest
 
from translator import english_to_french, french_to_english
 
class TestEnglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('None'),'') #test for null input for english to french
        self.assertNotEqual(english_to_french(0),0) #test for empty string
 
 
class TestFrenchtoEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(french_to_english('None'),'') #test for null input for french to english
        self.assertNotEqual(french_to_english(0),0) #test for empty string
 
class TestHelloBonjour(unittest.TestCase):
    def test3(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #hello returns bonjour
        self.assertNotEqual(english_to_french('Hello'), 'Hello') #hello does not return hello
 
class TestBonjourHello(unittest.TestCase):
    def test4(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #bonjour returns hello
        self.assertNotEqual(french_to_english('Hello'), 'Hello') #hello does not return hello
 
unittest.main()
