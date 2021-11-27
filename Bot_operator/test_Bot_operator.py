import unittest
from itertools import cycle
from Bot_operator.states_machine import operator, machine, valid_trigger

# phrases to function 'test_valid_dialog0'
operator_phrases = [
    'Какую вы хотите пиццу? Большую или маленькую?',
    'Как вы будете платить? Картой или наличными?',
    'Вы хотите большую пиццу, оплата - наличкой?',
    'Спасибо за заказ!'
]
client_phrases = ['Большую', 'Наличкой', 'Да']


class TestDialog(unittest.TestCase):
    def test_valid_dialog0(self):
        operator_phrase_index = 0
        client_phrase_index = 0
        operator.to_new_order()
        for speaker in cycle([operator_phrases, client_phrases]):
            if speaker == operator_phrases:
                self.assertEqual(
                    machine.get_model_state(operator).say(),
                    speaker[operator_phrase_index]
                )
                operator_phrase_index += 1
            else:
                if operator.state in ('new_order', 'payment'):
                    operator.change_order(
                        operator.state,
                        speaker[client_phrase_index]
                    )
                valid_trigger(speaker[client_phrase_index])
                client_phrase_index += 1
            if client_phrase_index == len(client_phrases) - 1 and operator_phrase_index == len(operator_phrases) - 1:
                break

    # like "test_valid_dialog0", but more manual
    def test_valid_dialog1(self):
        operator.to_new_order()
        self.assertEqual(machine.get_model_state(operator).say(), 'Какую вы хотите пиццу? Большую или маленькую?')
        operator.change_order(operator.state, 'Большую')
        valid_trigger('Большую')
        self.assertEqual(machine.get_model_state(operator).say(), 'Как вы будете платить? Картой или наличными?')
        operator.change_order(operator.state, 'Наличкой')
        valid_trigger('Наличкой')
        self.assertEqual(machine.get_model_state(operator).say(), 'Вы хотите большую пиццу, оплата - наличкой?')
        valid_trigger('Да')
        self.assertEqual(machine.get_model_state(operator).say(), 'Спасибо за заказ!')

    # dialog with 'NO' in confirmation
    def test_valid_dialog2(self):
        operator.to_new_order()
        self.assertEqual(machine.get_model_state(operator).say(), 'Какую вы хотите пиццу? Большую или маленькую?')
        operator.change_order(operator.state, 'маленькую')
        valid_trigger('маленькую')
        self.assertEqual(machine.get_model_state(operator).say(), 'Как вы будете платить? Картой или наличными?')
        operator.change_order(operator.state, 'картой')
        valid_trigger('картой')
        self.assertEqual(machine.get_model_state(operator).say(), 'Вы хотите маленькую пиццу, оплата - картой?')
        valid_trigger('нет')
        self.assertEqual(
            machine.get_model_state(operator).say(),
            'Что вы хотите изменить? Размер пиццы или способ оплаты?'
        )
        valid_trigger('оплату')
        self.assertEqual(machine.get_model_state(operator).say(), 'Как вы будете платить? Картой или наличными?')
        operator.change_order(operator.state, 'наличными')
        valid_trigger('наличными')
        self.assertEqual(machine.get_model_state(operator).say(), 'Вы хотите маленькую пиццу, оплата - наличными?')
        valid_trigger('да')
        self.assertEqual(machine.get_model_state(operator).say(), 'Спасибо за заказ!')

    # standard dialog step by step
    def test_valid_A(self):
        operator.to_new_order()
        self.assertEqual(machine.get_model_state(operator).say(), 'Какую вы хотите пиццу? Большую или маленькую?')

    def test_valid_B(self):
        operator.change_order(operator.state, 'Большую')
        valid_trigger('Большую')
        self.assertEqual(machine.get_model_state(operator).say(), 'Как вы будете платить? Картой или наличными?')

    def test_valid_C(self):
        operator.change_order(operator.state, 'Наличкой')
        valid_trigger('Наличкой')
        self.assertEqual(machine.get_model_state(operator).say(), 'Вы хотите большую пиццу, оплата - наличкой?')

    def test_valid_D(self):
        valid_trigger('Да')
        self.assertEqual(machine.get_model_state(operator).say(), 'Спасибо за заказ!')


if __name__ == '__main__':
    unittest.main()
