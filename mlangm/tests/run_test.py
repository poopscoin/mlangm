if __name__ == '__main__':
    from sys import path
    from os import getcwd
    path.append(getcwd())

import unittest
from mlangm import configure, translate, get_config, _extra


class TestLocalizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configure(default_lang='en', translations_path='locale', strict_mode=True)

    def test_greeting_en(self):
        self.assertEqual(translate('greeting', 'en'), 'Hello')

    def test_greeting_ru(self):
        self.assertEqual(translate('greeting', 'ru'), 'Привет')

    def test_farewell_with_name_ru(self):
        self.assertEqual(translate('farewell', 'ru', name='Alice'), 'Пока, Alice')

    def test_farewell_with_name_en(self):
        self.assertEqual(translate('farewell', 'en', name='Bob'), 'Bye, Bob')

    def test_missing_translation_key(self):
        if not get_config("mode"):
            self.assertEqual(translate('not.existing.key', 'ru'), 'not.existing.key')
        else:
            self.assertEqual(translate('menu.settings.test', 'en'), 'menu.settings.test')

    def test_fallback_to_default_lang(self):
        self.assertEqual(translate('greeting', 'jp'), 'Hello')

    def test_none_key_to_default_lang(self):
        self.assertEqual(translate('only_ua', 'ru'), 'only_ua')

    def test_key_only_one_lang(self):
        self.assertEqual(translate('only_ua', 'ua'), 'Тільки українською')

    def test_nested_key(self):
        self.assertEqual(translate('menu.settings.title', 'ru'), 'Настройки')

    def test_nested_key2(self):
        self.assertEqual(translate('menu.settings.title', 'en'), 'Settings')

    def test_nested_key_in_multi_row_nested_key(self):
        self.assertEqual(translate('menu.back', 'ua'), 'Повернутися')

    def test_nested_key_in_multi_row_nested_key2(self):
        self.assertEqual(translate('menu.settings.buttons.next', 'ua'), 'Наступна')

    def test_nested_key_in_multi_row_nested_key3(self):
        self.assertEqual(translate('menu.settings.buttons.back', 'ua'), 'Попередня')

    def test_nested_key_in_multi_row_nested_key4(self):
        self.assertEqual(translate('menu.settings.descr', 'ua'), 'Налаштуй свої повідомлення')

    def test_another_nested_key(self):
        self.assertEqual(translate('menu.settings.button', 'ru'), 'Кнопка')

    def test_another_nested_key2(self):
        self.assertEqual(translate('menu.contacts.title', 'ru'), 'Контакты')
    
    def test_another_nested_key_theepl_names(self):
        self.assertEqual(translate('menu.settings.test', 'ru', one='первых', two='вторых', thee='третих'), 'Много первых, вторых и третих')
    
    def test_another_nested_key_theepl_names_wrong(self):
        self.assertEqual(translate('menu.settings.test', 'ru', one='первых'), 'Много {one}, {two} и {thee}')
    
    def test_test(self):
        print(_extra().config)
        self.assertEqual(0, 0)

class TestAnotherLocalizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configure(default_lang='ua', translations_path='locale/another_locale')
    
    def test_change_lang_file(self):
        self.assertEqual(translate('new_locale'), 'Ви обрали інший файл мови')

    def test_change_lang_file_with_name(self):
        self.assertEqual(translate('another_bye', 'en', new_name='Petr'), 'Goodbye, good day, Petr')
    
    def test_test(self):
        print(_extra().config)
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
