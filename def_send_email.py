from calendar import monthrange
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


def enviar_email(gmail_user, gmail_pass, gmail_to, lista_departamento_sem_id, lista_colaborador_sem_projeto, lista_colaborador_sem_cadastro, lista_colaboradores_sem_conta_a_pagar, lista_conta_atualizada_sucesso, conta_omie, msg="", texto=""):
    try:

        subject = 'ATENÇÃO: Resultado do Serviço de Distribuição dos Custos'+ msg
        mail_content = "ERRO GERAL"
        if not msg:
            mail_content = f"""
                <HTML><BODY>
                Segue lista de usuários <b>no processo de separação dos custos da<br/> 
                <br/>Lista dos Colaboradores com Conta Atualizada com Sucesso: <table border=1>"""
            tabela = ""
            for item in lista_conta_atualizada_sucesso:
                tabela= tabela+"<tr><td> "+item+"</td></tr>"
            mail_content = mail_content +tabela
            mail_content= mail_content +f"""</table><br/>
                <br/>Lista Error Id Departamento: <table border=1>"""
            tabela_2 = ""
            for item in lista_departamento_sem_id:
                tabela_2= tabela_2+"<tr><td> "+item+"</td></tr>"
            mail_content = mail_content +tabela_2
            mail_content= mail_content +f"""</table><br/>
                <br/>Lista Error Colaborador Sem Projeto: <table border=1>"""
            tabela_3 = ""
            for item in lista_colaborador_sem_projeto:
                tabela_3= tabela_3+"<tr><td> "+item+"</td></tr>"
            mail_content = mail_content +tabela_3
            mail_content= mail_content +f"""</table><br/>
                <br/>Lista Error Colaborador Sem Cadastro: <table border=1>"""
            tabela_4 = ""
            for item in lista_colaborador_sem_cadastro:
                tabela_4= tabela_4+"<tr><td> "+item+"</td></tr>"
            mail_content = mail_content +tabela_4
            mail_content= mail_content +f"""</table><br/>

                <br/>Lista Error Colaborador Sem Conta a Pagar: <table border=1>"""
            tabela_5 = ""
            for item in lista_colaboradores_sem_conta_a_pagar:
                tabela_5= tabela_5+"<tr><td> "+item+"</td></tr>"
            mail_content = mail_content +tabela_5
            mail_content= mail_content +f"""</table><br/>
                </BODY></HTML>
                """
        else:
            mail_content =f"<HTML><BODY>{texto}</BODY></HTML>"
        #The mail addresses and password
        sender_address = gmail_user
        sender_pass = gmail_pass
        receiver_address = gmail_to.split(",")
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = ", ".join(receiver_address)
        message['Subject'] = subject
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html', 'utf-8'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as e:
        logging.error('Falha ao executar a def enviar_email' +str(e))
        raise Exception('Falha ao executar a def enviar_email' +str(e))
