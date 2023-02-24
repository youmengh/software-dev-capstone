from django.db import models

class Test(models.Model):  # new
    text = models.TextField()

# returns name of data in admin list instead of test_object
def __str__(self):  # new
        return self.text[:50]

