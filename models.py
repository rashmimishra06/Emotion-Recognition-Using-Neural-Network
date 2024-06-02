from django.db import models

# Create your models here.
class Inputemo(models.Model):
    emo_id = models.AutoField(primary_key=True)
    emo_name = models.CharField(default="emotion fining", max_length=150)
    date_when_upload = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to="my_data/", null=True, blank=True)

    def __str__(self):
        return self.emo_name

    def delete(self, using=None, keep_parents=False):
        self.Inputemo.storage.delete(self.Inputemo.emo_id)
        self.file.storage.delete(self.Inputemo.name)
        super().delete()