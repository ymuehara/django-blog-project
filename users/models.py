from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # pillow library


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        """
        overrides the save method. Method that gets run after model is saved.
        Exists in parent class, but we are creating our own so we can add functionality
        """
        super().save()  # runs the save method of parent class

        # will open the image of the current instance
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  # tuple of max sizes
            img.thumbnail(output_size)
            img.save(self.image.path)
