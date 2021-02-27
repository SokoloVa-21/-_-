from typing import Dict, Union
from unittest import TestCase

from telegram.ext import Updater

from main import get_address_from_coords


class Test(TestCase):
    def test_get_address_from_coords1(self):
        coords = f"{2.2945111},{48.8582573}"
        self.assertEqual(get_address_from_coords(
            coords), "Франция, Иль-де-Франс, Париж, VII округ Парижа, авеню Анатоль Франс, 5")

    def test_get_address_from_coords2(self):
        coords = f"{2.2945111},{48.8582573}"
        self.assertNotEqual(get_address_from_coords(coords), "Россия, Ханты-Мансийский автономный округ, "
                                                             "Нижневартовск, улица " \
                                                             "Менделеева, 8А ")

    def test_get_adress_from_location(self):
        loc: Dict[str, Union[Dict[str, float], str]] = {'location': {'longitude': 30.397852, 'latitude': 60.039635},
                                                        'title': 'Магазин Колхоз',
                                                        'address': 'проспект Просвещения 69',
                                                        'foursquare_id': '4ef6fd76b8f72ebea7fb2995',
                                                        'foursquare_type': 'shops/foodanddrink'}
        current_position1 = loc["location"]["longitude"]
        current_position2 = loc["location"]["latitude"]
        coords = f"{current_position1},{current_position2}"
        address_str = get_address_from_coords(coords)
        self.assertEqual(address_str, "Россия, Санкт-Петербург, проспект Просвещения, 69")

    def test_making_bot(self):
        updater = Updater("1587628778:AAED4G-hYFpf5u3pH2cIV8LYCltvPwFrvn8", use_context=True)
        self.assertEqual(updater.bot.id, 1587628778)
        self.assertEqual(updater.bot.first_name, 'Kurs21')
        self.assertTrue(updater.bot.bot.is_bot)

    def test_integr1(self):
        updater = Updater("1587628778:AAED4G-hYFpf5u3pH2cIV8LYCltvPwFrvn8", use_context=True)
        self.assertEqual(updater.bot.id, 1587628778)
        self.assertEqual(updater.bot.first_name, 'Kurs21')
        self.assertTrue(updater.bot.bot.is_bot)
        loc: Dict[str, Union[Dict[str, float], str]] = {'location': {'longitude': 30.397852, 'latitude': 60.039635},
                                                        'title': 'Магазин Колхоз',
                                                        'address': 'проспект Просвещения 69',
                                                        'foursquare_id': '4ef6fd76b8f72ebea7fb2995',
                                                        'foursquare_type': 'shops/foodanddrink'}
        current_position1 = loc["location"]["longitude"]
        current_position2 = loc["location"]["latitude"]
        coords = f"{current_position1},{current_position2}"
        address_str = get_address_from_coords(coords)
        self.assertEqual(address_str, "Россия, Санкт-Петербург, проспект Просвещения, 69")

    def test_integr2(self):
        updater = Updater("1587628778:AAED4G-hYFpf5u3pH2cIV8LYCltvPwFrvn8", use_context=True)
        self.assertEqual(updater.bot.id, 1587628778)
        self.assertEqual(updater.bot.first_name, 'Kurs21')
        self.assertTrue(updater.bot.bot.is_bot)
        coords = f"{2.2945111},{48.8582573}"
        self.assertEqual(get_address_from_coords(
            coords), "Франция, Иль-де-Франс, Париж, VII округ Парижа, авеню Анатоль Франс, 5")

