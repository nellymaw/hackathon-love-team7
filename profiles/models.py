from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    """
    A user profile model 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_about_me = models.CharField(max_length=100,
                                            null=True, blank=True)
    default_comment = models.CharField(max_length=80,
                                               null=True, blank=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

class Profile(models.Model):

    """
    A user Profile model for maintaining default
    information and history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     Profile.objects.create(user=instance)

#     """
#     Create or update user profiles
#     """
#     if created:
#         #Exisiting users: just save profile
#         instance.userprofile.save()
 