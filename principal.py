import contatos_utils
try:
    #contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')
    #contatos_utils.contatos_para_pickel(contatos, 'dados/contatos.pickel')

    #contatos = contatos_utils.pickel_para_contato('dados/contatos.pickel')
    #contatos_utils.contatos_para_json(contatos, 'dados/contatos.json')

    contato =contatos_utils.json_para_contatos('dados/contatos.json')

    for contato in contato:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado')
finally:
    print('Sem permissão de escrita')
