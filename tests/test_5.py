import time

class Test5:

    def test_like_post_buzz(self, new_post_buzz):

        login_p, menu_p, buzz_p = new_post_buzz
        buzz_p.like_post()
        assert login_p.alerts(), "Alert não encontrado"
        time.sleep(2)
        assert buzz_p.has_like_interactions(), "O like não aconteceu"
        assert buzz_p.has_interactions() == '1 Like', "Sem curtidas na postagem"