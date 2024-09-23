import time

class Test2:

    def test_edit_post_buzz(self, new_post_buzz):

        edit_description = "Edição da postagem. Time 2"
        login_p, menu_p, buzz_p = new_post_buzz
        buzz_p.edit_post(edit_description)
        assert login_p.alerts(), "Alert não encontrado"
        time.sleep(2)
        assert buzz_p.has_description_post() == edit_description, "Elemento não encontrado"