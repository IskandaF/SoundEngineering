from django.core.mail import send_mail
from django.conf import settings
from tracks.models import Project
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

class Message:
    
    def __init__(self,formset):
        self.formset=formset
       
    def prepare_message(self,receiver):
        if receiver=="engineer":
            message="Привет, присылаю правки:\n"
            for form in self.formset:
                    
                    # form.save()
                    if form.cleaned_data["volumechange"]!=0:
                        message+="Громкость - "+str(form.cleaned_data["volumechange"])+"\n"
                    if form.cleaned_data["panningposition"]!=0:
                        if form.cleaned_data["panningposition"]>int(0):
                            message+="На "+str(form.cleaned_data["volumechange"])+"% направо \n"
                        if form.cleaned_data["panningposition"]<int(0):
                            message+="На "+str(form.cleaned_data["volumechange"])+"% налево \n"
                    if form.cleaned_data["eq_high"]!=0:
                        if form.cleaned_data["eq_high"]>0:
                            message+="Высокие на "+str(form.cleaned_data["eq_high"])+"% повыше \n"
                        if form.cleaned_data["eq_high"]<0:
                            message+="Высокие на "+str(form.cleaned_data["volumechange"])+"% пониже\n"
                    message=message+("Для {0}".format(form.cleaned_data["track"]))
        if receiver=="admin":
            message=""
        if receiver=="user":
            context_submitter={"form":form,"username":form.User.username}
            message= 

        return message
        
    def notify(self):
        # message_user=prepare_message("user")
        # message_admin=prepare_message("admin")
        # message_engineer=prepare_message("engineer")
        return send_mail(
        'Revisions',
        "The revisions are done, come an check",
        'soulist96@yandex.ru',
        ['ifakhritdinov@gmail.com'],
        fail_silently=False,
    )
    def notifysubmitter(self):
        submitter=User.objects.filter(project=form.cleaned_data["project"])
        message=prepare_message(receiver="submitter")
        
    def notifyengineer(self):
        message=prepare_message(receiver="engineer")
    def notifyadmin(self):
        message=prepare_message(receiver="admin")
    # def CookMessage(revisions):
    #     message=revisions

