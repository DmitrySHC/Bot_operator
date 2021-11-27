import unittest
from Bot_operator.dialogs import answer_to, initial_phrase


class TestDialog(unittest.TestCase):

    # manual and readable standard dialog
    def test_valid_dialog1(self):
        self.assertEqual(initial_phrase(), 'Какую вы хотите пиццу? Большую или маленькую?')
        self.assertEqual(answer_to('Большую'), 'Как вы будете платить? Картой или наличными?')
        self.assertEqual(answer_to('Наличкой'), 'Вы хотите большую пиццу, оплата - наличкой?')
        self.assertEqual(answer_to('Да'), 'Спасибо за заказ!')

    # dialog with 'NO' in confirmation
    def test_valid_dialog2(self):
        self.assertEqual(initial_phrase(), 'Какую вы хотите пиццу? Большую или маленькую?')
        self.assertEqual(answer_to('маленькую'), 'Как вы будете платить? Картой или наличными?')
        self.assertEqual(answer_to('картой'), 'Вы хотите маленькую пиццу, оплата - картой?')
        self.assertEqual(answer_to('нет'), 'Что вы хотите изменить? Размер пиццы или способ оплаты?')
        self.assertEqual(answer_to('оплату'), 'Как вы будете платить? Картой или наличными?')
        self.assertEqual(answer_to('наличными'), 'Вы хотите маленькую пиццу, оплата - наличными?')
        self.assertEqual(answer_to('да'), 'Спасибо за заказ!')

    # standard dialog step by step
    def test_valid_A(self):
        self.assertEqual(initial_phrase(), 'Какую вы хотите пиццу? Большую или маленькую?')

    def test_valid_B(self):
        self.assertEqual(answer_to('Большую'), 'Как вы будете платить? Картой или наличными?')

    def test_valid_C(self):
        self.assertEqual(answer_to('Наличкой'), 'Вы хотите большую пиццу, оплата - наличкой?')

    def test_valid_D(self):
        self.assertEqual(answer_to('Да'), 'Спасибо за заказ!')

    # dialog with wrong answer from client on each step
    def test_valid_dialog_with_wrong_answer(self):
        self.assertEqual(initial_phrase(), 'Какую вы хотите пиццу? Большую или маленькую?')
        self.assertEqual(answer_to('круглую!!!'), 'Возможно вы ошиблись при вводе, повторите попытку.')
        self.assertEqual(answer_to('маленькую'), 'Как вы будете платить? Картой или наличными?')
        self.assertEqual(answer_to('НИКАК'), 'Возможно вы ошиблись при вводе, повторите попытку.')
        self.assertEqual(answer_to('по карте'), 'Вы хотите маленькую пиццу, оплата - по карте?')
        self.assertEqual(answer_to('Я?'), 'Возможно вы ошиблись при вводе, повторите попытку.')
        self.assertEqual(answer_to('ДА'), 'Спасибо за заказ!')


if __name__ == '__main__':
    unittest.main()
