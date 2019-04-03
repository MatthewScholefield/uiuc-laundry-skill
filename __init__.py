from mycroft import MycroftSkill, intent_file_handler


class UiucLaundry(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('laundry.uiuc.intent')
    def handle_laundry_uiuc(self, message):
        number = ''

        self.speak_dialog('laundry.uiuc', data={
            'number': number
        })


def create_skill():
    return UiucLaundry()

