from transitions import Machine, State
from Bot_operator.operations import Operator


TRANSITIONS = [
    {'trigger': 'size', 'source': 'new_order', 'dest': 'payment'},
    {'trigger': 'pay', 'source': 'payment', 'dest': 'confirmation'},
    {'trigger': 'N_conf', 'source': 'confirmation', 'dest': 'edit'},
    {'trigger': 'edit_pay', 'source': 'edit', 'dest': 'payment'},
    {'trigger': 'edit_size', 'source': 'edit', 'dest': 'new_order'},
    {'trigger': 'Y_conf', 'source': 'confirmation', 'dest': 'complete'},
]

VALID_TRIGGERS = {
    'size': ['большую', 'маленькую'],
    'pay': ['наличкой', 'наличными', 'картой', 'по карте'],
    'Y_conf': ['да', '+'],
    'N_conf': ['нет', '-'],
    'edit_size': ['размер', 'размер пиццы', 'пиццу'],
    'edit_pay': ['способ оплаты', 'способ', 'оплату'],
}


class StateOrder(State):
    def say(self):
        return 'Какую вы хотите пиццу? Большую или маленькую?'


class StatePay(State):
    def say(self):
        return 'Как вы будете платить? Картой или наличными?'


class StateConfirm(State):
    def say(self):
        current_phrase = 'Вы хотите {} пиццу, оплата - {}?'.format(
            operator.current_order['new_order'],
            operator.current_order['payment']
        )
        return current_phrase


class StateEdit(State):
    def say(self):
        return 'Что вы хотите изменить? Размер пиццы или способ оплаты?'


class StateComplete(State):
    def say(self):
        return 'Спасибо за заказ!'


STATES = [
    StateOrder(name='new_order'),
    StatePay(name='payment'),
    StateConfirm(name='confirmation'),
    StateEdit(name='edit'),
    StateComplete(name='complete'),
]


operator = Operator()
machine = Machine(model=operator, states=STATES, transitions=TRANSITIONS, initial='new_order')


def valid_trigger(word):
    for trigger, words in VALID_TRIGGERS.items():
        if word.lower() in words:
            operator.trigger(trigger)
            break
    else:
        raise ValueError()
