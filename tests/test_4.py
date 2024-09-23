import time

class Test4:

    def test_comment_post_buzz(self, new_post_buzz):

        comment_text = "Teste Comentario. Time 2"
        login_p, menu_p, buzz_p = new_post_buzz
        buzz_p.comment_post(comment_text)
        assert login_p.alerts(), "Alert não encontrado"
        time.sleep(2)
        assert buzz_p.has_interactions() == '1 Comment', "Sem comentarios na postagem"