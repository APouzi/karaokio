from django.db import models
from django.conf import settings

# upload_to field allows for a callable and thats how it's getting the name. Note, you can't save userID because this is being applied before the save. This can be achieved with updating the model after a save, which is a whole seperate thing. 
def upload_to(instance, name):
    #since model returns __str__ method is returning "self.name", it returns a string of name. Unlike behavior within views that usually get their id passed in. Makes sense, 
    return f'venue/{instance.created_by}/{name}'


# Create your models here.
class Venue(models.Model):#Wondering if it's requiring me to allow the null stuff because of the foriegnKey
    name = models.CharField(max_length=300)
    description = models.TextField(null = True)
    state = models.CharField(max_length=2, null=True)
    zip = models.IntegerField(null = True)
    has_nft = models.BooleanField(null = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null = True)
    created_date = models.DateTimeField(auto_now_add = True)#Not editable, so wont show up in admin panel to view, must specify within code to view within it. 
    image = models.ImageField(upload_to = upload_to, default = 'venue/default.jpg')
    published = models.BooleanField(default=False)

    #Fields I believe it needs: Street Address, unit number(if needed), state
    def __str__(self):
        return self.name

