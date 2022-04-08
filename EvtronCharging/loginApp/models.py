from django.db import models

# Create your models here.
class Userbase_table(models.Model):
    
    username = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True, max_length=255)
    pass1 = models.CharField(null=True, max_length=20)
    status =  models.CharField(null=True, max_length=20)
    verified =  models.CharField(null=True, max_length=20)
    

    def register(self):
        self.save()

    def usernameisExist(self):
        if Customer.objects.filter(username=self.username):
            print('true')
            return True
        else:
            print('false')
            return False

    def mailisExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

class Usertransaction_table(models.Model):
     login_time =  models.DateTimeField(null=True)
     logout_time = models.DateTimeField(null=True)






