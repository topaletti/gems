from django.core.mail import send_mail

def send_test_mail(request):
    send_mail("It works!", "This will get sent through Mailgun",
              "Anymail Sender <from@example.com>", ["antonio.bruletti@gmail.com"])