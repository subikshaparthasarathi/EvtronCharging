from django.db import models

# Create your models here.
class Usermaster_table(models.Model):
    
    username = models.CharField(null=True, max_length=50)
    email = models.EmailField(max_length=255, primary_key=True, null=False)
    pass1 = models.CharField(null=True, max_length=20)
    status =  models.CharField(null=True, max_length=20)
    verified =  models.CharField(null=True, max_length=20)
    

    def register(self):
        self.save()

    def usernameisExist(self):
        if Usermaster_table.objects.filter(username=self.username):
            print('true')
            return True
        else:
            print('false')
            return False

    def mailisExist(self):
        if Usermaster_table.objects.filter(email=self.email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Usermaster_table.objects.get(email=email)
        except:
            return False

class Useractivity_table(models.Model):
     email = models.ForeignKey(Usermaster_table, on_delete=models.CASCADE)
     login_time =  models.DateTimeField(null=True)
     logout_time = models.DateTimeField(null=True)

     @staticmethod
     def get_loginlogout_by_email(email):
        try:
            return Useractivity_table.objects.get(email=email)
        except:
            return False






