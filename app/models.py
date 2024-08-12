from django.db import models


class Infos(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=200)
    company_location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=255)
    company_twitter = models.URLField(null=True, max_length=100, blank=True, default=any)
    company_facebook = models.URLField(null=True, max_length=100, blank=True, default=any)
    company_instagram = models.URLField(null=True, max_length=100, blank=True, default=any)
    company_linkedin = models.URLField(null=True, max_length=100, blank=True, default=any)

    class Meta:
        db_table = 'infos'
        managed = True
        verbose_name = 'infos'
        verbose_name_plural = 'infos'


    def __str__(self) -> str:
        return self.company_name
