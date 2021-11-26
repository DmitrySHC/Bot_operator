class Operator:

    def __init__(self):
        self.current_phrase = 'Какую вы хотите пиццу? Большую или маленькую?'
        self.current_order = {'new_order': '', 'payment': ''}
        self.operator_phrases = {
            'new_order': 'Какую вы хотите пиццу? Большую или маленькую?',
            'payment': 'Как вы будете платить? Картой или наличными?',
            'edit': 'Что вы хотите изменить? Размер пиццы или способ оплаты?',
            'complete': 'Спасибо за заказ!'
        }

    def change_phrase(self, state):
        if state == 'confirmation':
            self.current_phrase = 'Вы хотите {} пиццу, оплата - {}?'.format(
                self.current_order['new_order'],
                self.current_order['payment']
            )
        else:
            self.current_phrase = self.operator_phrases[state]

    def change_order(self, state, content):
        self.current_order[state] = content.lower()
