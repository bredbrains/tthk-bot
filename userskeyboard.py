from vkbottle import Keyboard, KeyboardButtonColor, Text


class UsersKeyboard:

    def __init__(self):
        self.keyboard = None

    def get_main(self):
        self.keyboard = Keyboard(one_time=False) \
            .add(Text("TARpv19"), color=KeyboardButtonColor.POSITIVE) \
            .row() \
            .add(Text("Baum, Eduard"), color=KeyboardButtonColor.POSITIVE) \
            .get_json()
        return self.keyboard
