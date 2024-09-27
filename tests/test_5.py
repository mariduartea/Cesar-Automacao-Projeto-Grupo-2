from interaction_type import InteractionType

class Test5:

    def test_like_post_buzz(self, new_post_buzz_with_delete):

        login_p, menu_p, buzz_p = new_post_buzz_with_delete
        
        buzz_p.like_post()
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz_p.has_like_interactions(), "O like não aconteceu"
        assert buzz_p.has_interactions(InteractionType.Like, '1 Like'), "Sem curtidas na postagem"

        # No final de teste a postagem será apagada