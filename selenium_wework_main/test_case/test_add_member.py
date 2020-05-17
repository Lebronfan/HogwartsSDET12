from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        assert self.main.goto_add_member().add_member()
