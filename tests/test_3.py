class Test3:

    def test_delete_post_buzz(self, new_post_buzz):
        
        login_p, menu_p, buzz_p = new_post_buzz

        description = "Nova postagem para realizar testes. Time 2."
        
        buzz_p.delete_post()
        assert login_p.alerts(), "Alert não encontrado"
        assert len(buzz_p.get_posts_by_text(description)) == 0

        # Como este teste é sobre o excluir de um post, eu não estou usando o new_post_buzz_with_delete do conftest
