from django.db import models


# general infos model
class Infos(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=200)
    company_location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=255, null=True)
    company_twitter = models.URLField(null=True, max_length=100, blank=True)
    company_facebook = models.URLField(null=True, max_length=100, blank=True)
    company_instagram = models.URLField(null=True, max_length=100, blank=True)
    company_linkedin = models.URLField(null=True, max_length=100, blank=True)

    class Meta:
        db_table = 'infos'
        managed = True
        verbose_name = 'infos'
        verbose_name_plural = 'infos'

    def __str__(self) -> str:
        return self.company_name
    

# servcies model
class ServicesModel(models.Model):
    service_picture = models.ImageField(upload_to='uploads')
    service_title = models.CharField(max_length=50)
    service_description = models.CharField(max_length=100)

    class Meta:
        db_table = 'services'
        managed = True
        verbose_name = 'services'
        verbose_name_plural = 'services'

    def __str__(self) -> str:
        return self.service_title
    


# about model
class AboutModel(models.Model):
    about_title = models.CharField(max_length=50)
    about_content = models.TextField()
    about_image = models.ImageField(upload_to='uploads')

    class Meta:
        db_table = 'about'
        managed = True
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self) -> str:
        return self.about_title