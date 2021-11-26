from transitions import Machine
from Bot_operator.operations import Operator


STATES = ['new_order', 'payment', 'confirmation', 'edit', 'complete']

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
    'edit_size': ['размер', 'размер пиццы'],
    'edit_pay': ['способ оплаты', 'способ', 'оплату'],
}

operator = Operator()
machine = Machine(model=operator, states=STATES, transitions=TRANSITIONS, initial='new_order')


def valid_trigger(word):
    for trigger, words in VALID_TRIGGERS.items():
        if word in words:
            operator.trigger(trigger)
            break
    else:
        raise ValueError()
