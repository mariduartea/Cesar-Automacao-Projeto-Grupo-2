from interaction_type import InteractionType

class Test6:

    def test_to_share_post_buzz(self, new_post_buzz_with_delete):

        login_p, menu_p, buzz_p = new_post_buzz_with_delete

        buzz_p.share_post()
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz_p.has_interactions(InteractionType.Share, '1 Share', 1), "Sem compartilhamento na postagem"

        # No final de teste a postagem será apagada
        # Devido o compartilhamento, será apagado apenas UMA postagem e outra vai ficar