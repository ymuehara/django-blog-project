from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # pillow library


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# image resizing. With our profile picture we set up so the pillow library resizes the images by opening them in the file system
# and resizing and resaving them. This worked when they were in the local file system,
# but now they are in s3bucket. And using pillow would give us some issues.
#    def save(self, *args, **kwargs):
        """
        overrides the save method. Method that gets run after model is saved.
        Exists in parent class, but we are creating our own so we can add functionality
        """
#        super().save(*args, **kwargs)  # runs the save method of parent class

        # will open the image of the current instance
#        img = Image.open(self.image.path)

#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)  # tuple of max sizes
#            img.thumbnail(output_size)
#            img.save(self.image.path)
