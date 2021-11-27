from Bot_operator.states_machine import operator, machine, valid_trigger


def answer_to(text: str):
    try:
        if operator.state in ('new_order', 'payment'):
            operator.change_order(operator.state, text)
        valid_trigger(text)
    except:
        if operator.state in ('new_order', 'payment'):
            operator.change_order(operator.state, '')
        return 'Возможно вы ошиблись при вводе, повторите попытку.'
    else:
        return machine.get_model_state(operator).say()


def initial_phrase():
    operator.to_new_order()
    return machine.get_model_state(operator).say()
