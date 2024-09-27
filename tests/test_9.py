class Test9:

    def test_delete_record_on_the_qualification_screen(self, navigate_qualification):
        
        login_p, menu_p, myinfo_p, qualification_p = navigate_qualification

        #Preenchendo os campos Company, Job, Title, From e To e garantindo que foram preenchidos
        labels = ['Company', 'Job Title', 'From', 'To']
        values = ['Cesar Delete', 'QA - Delete','2023-01-09', '2024-01-09']

        for label, value in zip(labels, values):
            qualification_p.enter_value(label, value)

        #Salvando os valores preenchidos
        qualification_p.save_values()
        assert login_p.alerts(), "Alert não encontrado"
        qualification_p.wait_spinner()

        #Garantindo que os valores enviados então corretos
        assert qualification_p.was_saved(values), 'Os campos não foram salvos'

        #Excluindo a linha que acabamos de adicionar
        qualification_p.delete_item(0)
        assert login_p.alerts(), "Alert não encontrado"
        qualification_p.wait_spinner()