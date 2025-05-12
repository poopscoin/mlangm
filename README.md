# Mini language Manager

**Mini localization manager for Python using JSON/YAML files**

Mini language Manager is a lightweight and developer-friendly localization (i18n) tool for Python. It allows you to organize translations in plain JSON or YAML files and access them with nested keys. Supports fallback mechanisms and formatted string substitution.

---

## 📦 Installation

```bash
pip install m-lang-m
```

---

## ✨ Features

- ✅ Supports both `.json` and `.yaml`/`.yml` translation files  
- ✅ Automatic directory resolution relative to the caller  
- ✅ Nested key support (e.g., `menu.settings.language`)  
- ✅ Optional strict mode (fallbacks or not)  
- ✅ String formatting with `{placeholders}`  
- ✅ Simple and minimal public API  
- ✅ Returns the current config if needed  

---

## 📁 Translation File Example

**locale/en.json**
```json
{
    "title": "Main",
    "menu": {
        "settings": {
            "language": "Language",
            "placeholders": "Many {one}, {two} and {thee}"
        },
        "back" : "Go back"
    }
}
```

**locale/ua.yml**
```yml
title: "Головна"
menu:
  settings:
    language: "Мова"
    placeholders: "Багато {one}, {two} і {thee}"
  back: "Повернутися"
```

---

## 🚀 Usage

### 1. Configure the localizer

```python
from mlangm import configure, translate, get_config

config_info = configure(default_lang='en', translations_path='locale')
# config_info = {
#     'default_lang': 'en',
#     'path': 'locale',
#     'mode': False
# }

print(translate('menu.settings.language'))  # Output: "Language"
print(translate('menu.back')) # Output: "Go back"
print(translate('menu.settings.language', 'ua'))  # Output: "Мова"
print(translate('title', 'ua')) # Output: "Головна"

print(translate('menu.settings.placeholders', one='first', two='second', thee='third'))
# Output: "Many first, second and third"
```

---

## 🔧 API

### `configure(default_lang = 'en', translations_path = 'translations', strict_mode = False) -> dict`

Initializes the localizer and loads translations.

- `default_lang`(str): The default language code.
- `translations_path`(str): Directory with `.json` / `.yaml` files.
- `strict_mode`(bool): If True, disables fallbacks.

Returns the configuration dictionary.

---

### `translate(key: str, lang: str = None, **kwargs) -> str`

Retrieves a translated string.  
Supports fallback and string formatting.

---

### `get_config(key: str = None) -> str | bool | dict`

Returns the current configuration or a single setting.

---

### `_extra() -> Localizer`

Technical action, under normal conditions, not to be used.

Access the internal `Localizer` instance directly.

## 🧪 Example _extra()

```python
from mlangm import configure, _extra

configure(default_lang='en', translations_path='locale')

print(_extra().config) # Output: {'default_lang': 'en', 'path': 'locale', 'mode': False}
print(_extra().default_lang) # Output: 'en'
print(_extra().translations) # Output: Dictionary with translations from the 'locale' folder

```


---

## 📄 License

MIT License