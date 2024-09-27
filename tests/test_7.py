class Test7:

    def test_new_work_experience(self, navigate_qualification):

        login_p, menu_p, myinfo_p, qualification_p = navigate_qualification

        #Preenchendo os campos Company, Job, Title, From e To e garantindo que foram preenchidos
        labels = ['Company', 'Job Title', 'From', 'To']
        values = ['Cesar School', 'Quality Assurance','2023-01-09', '2024-01-09']

        for label, value in zip(labels, values):
            qualification_p.enter_value(label, value)

        #Salvando os valores preenchidos
        qualification_p.save_values()
        assert login_p.alerts(), "Alert não encontrado"
        qualification_p.wait_spinner()

        #Garantindo que os valores enviados então corretos
        assert qualification_p.was_saved(values), 'Os campos não foram salvos'