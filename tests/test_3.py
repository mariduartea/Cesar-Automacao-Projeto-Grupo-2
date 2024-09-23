import time

class Test3:

    def test_delete_post_buzz(self, new_post_buzz):

        description = "Nova postagem para realizar testes. Time 2."
        login_p, menu_p, buzz_p = new_post_buzz
        buzz_p.delete_post()
        assert login_p.alerts(), "Alert não encontrado"
        time.sleep(2)
        assert len(buzz_p.get_post_by_text(description)) == 0
