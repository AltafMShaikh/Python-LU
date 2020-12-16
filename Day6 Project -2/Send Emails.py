 def sendMail(email, name):
        
       html_text = '''<p><span style=\"font-family: Arial;\"><span style=\"background-color: rgb(247, 218, 100);\">HEY Sam,'''+ name+'''</span>&nbsp;</span></p>
                   <p><span style=\"font-family:Arial ;\"><br></span></p>
                   <p><span style=\"font-family:Arial ;\">How are you ,&nbsp;</span></p>
                   <p><span style=\"font-family:Arial ;\">King of Empire  !!</span></p>
                   <p><span style=\"font-family: Arial;\">Love u all,&nbsp;</span></p>
                   <p><span style=\"font-family: Arial;\"><br></span></p>
                   <p><span style=\"font-family: Arial;\">Regards,&nbsp;</span></p>
                   <p><strong><span style=\"font-family:Arial;\">King of Empire,</span></strong></p>
                   <p><span style=\"font-family: Arial;\"><strong>Altaf Shaikh</strong></span></p>'''
   
       subject = Hey sam + name + you have EMAIL FROM Empire
       message = emails.html(html=html_text,
                            subject=subject,
                              mail_from=('King Empire', 'sam@abc.com')),
    
    
        mail_via_python = message.send(to=email,
                                  smtp={'host': 'smtp.gmail.com',
                                         'timeout': 5,
                                       'port':587,
                                      'user':'YOUREMAIL@REQUIRED>COM',
                                        'password':'YourPassWordREquired',
                                        'tls':True})
      return mail_via_python.status_code"
