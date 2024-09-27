from interaction_type import InteractionType

class Test4:

    def test_comment_post_buzz(self, new_post_buzz_with_delete):

        login_p, menu_p, buzz_p = new_post_buzz_with_delete

        comment_text = "Teste Comentario. Time 2"

        buzz_p.comment_post(comment_text)
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz_p.has_interactions(InteractionType.Comment, '1 Comment'), "Sem comentarios na postagem"

        # No final de teste a postagem será apagada