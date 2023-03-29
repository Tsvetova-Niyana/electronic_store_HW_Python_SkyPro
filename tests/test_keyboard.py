from electronics_store.keyboard import Keyboard
import pytest

class TestKeyboard:
    def test_init_keyboard(self):
        """Проверка инициализации экземпляра класса Keyboard"""
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard is not None

    def test_check_name_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard.name_product == 'Dark Project KD87A'

    def test_check_amount_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard.amount_product == 9600

    def test_check_count_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard.count_product == 5

    def test_check_lang_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard.language == 'EN'

    def test_check_pay_rate_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert keyboard.pay_rate == 0.85

    def test_check_str_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(keyboard) == 'Dark Project KD87A'

    def test_check_repr_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        assert repr(keyboard) == f'Keyboard ({keyboard.name_product}, {keyboard.amount_product}, ' \
                                 f'{keyboard.count_product})'

    def test_check_change_lang_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        keyboard.change_lang()
        assert keyboard.language == 'RU'

    def test_check_many_change_lang_keyboard(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        keyboard.change_lang()
        keyboard.change_lang()
        assert keyboard.language == 'EN'

    def test_check_change_lang_keyboard_with_setter(self):
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        with pytest.raises(AttributeError):
            keyboard.language = 'CH'
