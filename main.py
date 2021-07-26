from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog


class Test(MDApp):
    dialog = None
    def submit(self):
        f = open("demofile.txt", "w")
        f.write(self.root.ids.test.text)
        f.close()
    def show(self):
        f = open("demofile.txt", "r")
        text = f.read()
        if not self.dialog:
            self.dialog = MDDialog(text=text)
        self.dialog.open()

Test().run()
