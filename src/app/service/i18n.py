import pendulum
from babel.support import Translations

from src.app.service.references import BASE_DIR

LOCALES_LOCATION = BASE_DIR.joinpath("locales")
TRANSLATIONS = {
    "zh_CN": Translations.load(LOCALES_LOCATION, locales=["zh_CN"]),
    "en_US": Translations.load(LOCALES_LOCATION, locales=["en_US"])
}

translations = TRANSLATIONS.get("en_US")


def set_locale(locale: str):
    global translations
    if locale == "zh_CN":
        plocale = "zh"
    else:
        plocale = "en"
    pendulum.set_locale(plocale)

    translations = TRANSLATIONS.get(locale)
