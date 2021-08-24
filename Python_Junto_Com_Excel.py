import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC764cd78c57185d298beeab478d12d622"
# Your Auth Token from twilio.com/console
auth_token = "7812cc3fbc0e0becf2fbaab21dd07620"
client = Client(account_sid, auth_token)

#Projeto de vendas, onde quando um vendedor bater a meta de venda ele recebe um sms com o valor da venda total

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguêm bateu a META. Vendedor: {vendedor}, Vendas:R${vendas}')
        message = client.messages.create(
            to="+5517991969256",
            from_="+19709646587",
            body=f'No mês {mes} alguêm bateu a META. Vendedor: {vendedor}, Vendas:R${vendas}')
        print(message.sid)

