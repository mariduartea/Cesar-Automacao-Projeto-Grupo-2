import time

class Test6:

    def test_to_share_post_buzz(self, new_post_buzz):

        login_p, menu_p, buzz_p = new_post_buzz
        buzz_p.share_post()
        assert login_p.alerts(), "Alert não encontrado"
        time.sleep(2)
        assert buzz_p.has_share() == '1 Share', "Sem compartilhamento na postagem"