from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Model to handle the uploaded files
class UploadedFiles(models.Model):
    # To get Unique URLs of the 
    # To be done in views, when inserting the data into this table.
    # TODO: Make a unique url as the ID of this table, should not already be present in the table
    unique_url = models.CharField(max_length=256, primary_key=True)
    # Foreign key to reference the user who uploaded the file, i.e. a user can upload multiple files
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=256)
    file_path = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

# Model to handle the sharing of files among different users
class SharedFiels(models.Model):
    # For every time a user shares a file, i.e. for every entry in this Model, 
    # TODO: an email should be sent to the added user
    # the file_id[unique_url] and user_id should be updated here
    shared_to_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    shared_file = models.ForeignKey(to=UploadedFiles, on_delete=models.CASCADE)
    shared_at = models.DateTimeField()

    def __str__(self):
        return str(self.shared_file) + ':' + str(self.shared_to_user)

# Model to handle the comments
class Comments(models.Model):

    file = models.ForeignKey(to=UploadedFiles, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # TODO: users can update their previously added comments
    # TODO: users should receive emails if some other user comments on their PDFs

    def __str__(self) -> str:
        return self.comment[:10] + '...:' + str(self.user)+':'+str(self.file)