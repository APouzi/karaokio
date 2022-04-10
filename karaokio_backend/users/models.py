from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator
from venues.models import Venue
from event.models import Event

def upload_to(instance, filename):
    return f"userprofile/{filename}"

class UserProfile(models.Model):
    image = models.ImageField(upload_to = upload_to, default = "userprofile/default.jpg")
    endUser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)#Not entirely sure about "on_delete", to be 100%.
    state = models.CharField(max_length=2, null = True)
    zip = models.IntegerField(default = 11111, validators=[MaxValueValidator(99999)])

class EndUserVenueFavoriteList(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete= models.CASCADE, null = True)#endUser or maybe UserProfile? 
    venues = models.ManyToManyField(Venue) 
    def __str__(self) -> str:
        return f"{self.userProfile} list"


class EndUserEventsFavoriteList(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete= models.CASCADE)
    events = models.ManyToManyField(Event)
    def __str__(self) -> str:
        return f"{self.userProfile}"

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
 
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name,last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        profile = UserProfile.objects.create(
            endUser = user,
            state = "CA",
            zip = 91942
        )
        EndUserVenueFavoriteList.objects.create(
            userProfile = profile,

        )
        EndUserEventsFavoriteList.objects.create(userProfile = profile)
        return user

class EndUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(auto_now_add = True, null = True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name',  'last_name']

    def __str__(self):
        return self.user_name