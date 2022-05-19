import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserAccountManager(BaseUserManager):

    def create_user(self,email,name,password = None):
         if not email:
             raise ValueError('users must have an email address')
         email = self.normalize_email(email)
         user = self.model(email=email, name = name)
         user.set_password(password)
         user.save()

         return user
    

class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_seller= models.BooleanField(default=False)
    is_buyer= models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)




    objects = UserAccountManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['name'] 
    def get_full_name(self):
      return self.name
    # def get_short_name(self):
    #   return self.name
    def __str__(self) -> str:
        return self.email

  
class SellerProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    seller = models.OneToOneField(UserAccount, on_delete=models.CASCADE,
                                              related_name='seller_profile')
    RegistrationNo = models.CharField(max_length=100, null=True, blank = True)
    RegistrationDate = models.DateField(auto_now_add = True)
    firstName = models.CharField(max_length = 100 , null = True, blank = True)
    LastName = models.CharField(max_length = 100  , null = True, blank = True)
    # contactDept = models.CharField(max_length=100, null=True, blank = True)
    contactPhone = models.CharField(max_length=100, null=True, blank = True)
    sellerPhone = models.CharField(max_length=100, null=True, blank = True)
    sellerEmail = models.EmailField(max_length = 200,null=True, blank = True)
    country = models.CharField(max_length=100, null=True, blank = True)
    state = models.CharField(max_length=100, null=True, blank = True)
    city = models.CharField(max_length=100, null=True, blank = True)
    companyWeb = models.CharField(max_length=100, null=True, blank = True)
    streetAddress = models.CharField(max_length=200, null=True, blank = True)