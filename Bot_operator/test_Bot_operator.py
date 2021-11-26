import unittest
from itertools import cycle
import Bot_operator.states_machine as states_machine

# phrases to function 'test_valid_dialog0'
operator = [
    'Какую вы хотите пиццу? Большую или маленькую?',
    'Как вы будете платить? Картой или наличными?',
    'Вы хотите большую пиццу, оплата - наличкой?',
    'Спасибо за заказ!'
]
client = ['Большую', 'Наличкой', 'Да']


class TestDialog(unittest.TestCase):
    def test_valid_dialog0(self):
        operator_phrase_index = 0
        client_phrase_index = 0
        states_machine.operator.to_new_order()
        states_machine.operator.change_phrase(states_machine.operator.state)
        for speaker in cycle([operator, client]):
            if speaker == operator:
                self.assertEqual(
                    states_machine.operator.current_phrase,
                    speaker[operator_phrase_index]
                )
                operator_phrase_index += 1
            else:
                if states_machine.operator.state in ('new_order', 'payment'):
                    states_machine.operator.change_order(
                        states_machine.operator.state,
                        speaker[client_phrase_index]
                    )
                states_machine.valid_trigger(speaker[client_phrase_index])
                states_machine.operator.change_phrase(states_machine.operator.state)
                client_phrase_index += 1
            if client_phrase_index == len(client) - 1 and operator_phrase_index == len(operator) - 1:
                break

# ====================================================================================================

    def test_valid_dialog1(self):
        states_machine.operator.to_new_order()
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Какую вы хотите пиццу? Большую или маленькую?')
        states_machine.operator.change_order(states_machine.operator.state, 'Большую')
        states_machine.valid_trigger('Большую')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Как вы будете платить? Картой или наличными?')
        states_machine.operator.change_order(states_machine.operator.state, 'Наличкой')
        states_machine.valid_trigger('Наличкой')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Вы хотите большую пиццу, оплата - наличкой?')
        states_machine.valid_trigger('Да')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Спасибо за заказ!')

    # ====================================================================================================

    def test_valid_dialog2(self):
        states_machine.operator.to_new_order()
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Какую вы хотите пиццу? Большую или маленькую?')
        states_machine.operator.change_order(states_machine.operator.state, 'маленькую')
        states_machine.valid_trigger('маленькую')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Как вы будете платить? Картой или наличными?')
        states_machine.operator.change_order(states_machine.operator.state, 'картой')
        states_machine.valid_trigger('картой')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Вы хотите маленькую пиццу, оплата - картой?')
        states_machine.valid_trigger('нет')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Что вы хотите изменить? Размер пиццы или способ оплаты?')
        states_machine.valid_trigger('оплату')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Как вы будете платить? Картой или наличными?')
        states_machine.operator.change_order(states_machine.operator.state, 'наличными')
        states_machine.valid_trigger('наличными')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Вы хотите маленькую пиццу, оплата - наличными?')
        states_machine.valid_trigger('да')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Спасибо за заказ!')

    # ====================================================================================================

    def test_valid_A(self):
        states_machine.operator.to_new_order()
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Какую вы хотите пиццу? Большую или маленькую?')

    def test_valid_B(self):
        states_machine.operator.change_order(states_machine.operator.state, 'Большую')
        states_machine.valid_trigger('Большую')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Как вы будете платить? Картой или наличными?')

    def test_valid_C(self):
        states_machine.operator.change_order(states_machine.operator.state, 'Наличкой')
        states_machine.valid_trigger('Наличкой')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Вы хотите большую пиццу, оплата - наличкой?')

    def test_valid_D(self):
        states_machine.valid_trigger('Да')
        states_machine.operator.change_phrase(states_machine.operator.state)
        self.assertEqual(states_machine.operator.current_phrase, 'Спасибо за заказ!')


if __name__ == '__main__':
    unittest.main()
