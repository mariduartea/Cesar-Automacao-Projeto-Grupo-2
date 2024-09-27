class Test2:

    def test_edit_post_buzz(self, new_post_buzz_with_delete):

        login_p, menu_p, buzz_p = new_post_buzz_with_delete

        edit_description = "Edição da postagem. Time 2"
        
        buzz_p.edit_post(edit_description)
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz_p.has_description_post(edit_description), "Elemento não encontrado"

        # No final de teste a postagem será apagada