class Test8:

    def test_validation_of_mandatory_fields(self, navigate_qualification):
        
        login_p, menu_p, myinfo_p, qualification_p = navigate_qualification

        #Salvando sem preencher os campos
        qualification_p.save_values()

        #Verificar se as mensagens de Required são exibidas para os campos Company e Job Title
        company_error = qualification_p.error_message_for_required_fields('Company')
        assert company_error, 'Mensagem de de erro no campo Company não foi exibida'

        job_title_error = qualification_p.error_message_for_required_fields('Job Title')
        assert job_title_error, 'Mensagem de erro no campo Job Title não foi exibida'