class Operator:

    def __init__(self):
        self.current_order = {'new_order': '', 'payment': ''}

    def change_order(self, state, content):
        self.current_order[state] = content.lower()
