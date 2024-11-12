from django.db import models
from .validators import iranian_phone_number_validator

# Create your models here.

class Profile(models.Model):
    name = models.CharField(verbose_name="نام کاربری", max_length=50)
    field = models.CharField(verbose_name="زمینه کاری", max_length=50)
    email = models.EmailField(verbose_name="ایمیل", null=True, blank=True)
    intro = models.TextField(verbose_name="معرفی نامه")
    phone_number = models.CharField(verbose_name="شماره تماس", max_length=12, null=True, blank=True)
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    
    instagram_link = models.URLField(blank=True, null=True, verbose_name="لینک اینستاگرام")
    twitter_link = models.URLField(blank=True, null=True, verbose_name="لینک توییتر")
    linkdien_link = models.URLField(blank=True, null=True, verbose_name="لینک لینکدین")
    github_link = models.URLField(blank=True, null=True, verbose_name="لینک گیتهاب")
    
    intro_image = models.ImageField(verbose_name="عکس بک گراند", upload_to="intro_image")
    
    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    SERVICE_CHOICES = [
        ('branding', 'طراحی برندینگ'),
        ('web', 'طراحی سایت'),
        ('uxui', 'طراحی UX/UI'),
        ('app', 'طراحی اپلیکیشن'),
    ]

    fname = models.CharField(max_length=50, verbose_name="نام")
    lname = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس", validators=[iranian_phone_number_validator])
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES, verbose_name="نوع خدمات", default="web")
    message = models.TextField(verbose_name="پیام")

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    
from django.utils.translation import gettext_lazy as _
class Category(models.TextChoices):
    UXUI = 'uxui', _('UX/UI')
    BRANDING = 'branding', _('برندینگ')
    MOBILE_APP = 'mobile-app', _('اپلیکیشن موبایل')

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("عنوان"))
    description = models.TextField(verbose_name=_("توضیحات"))
    image = models.ImageField(upload_to='portfolio/', verbose_name=_("تصویر"))
    category = models.CharField(max_length=50, choices=Category.choices, verbose_name=_("دسته‌بندی"), default="uiux")
    client = models.CharField(max_length=100, verbose_name=_("مشتری"), default="ناشناس")
    start_date = models.DateField(verbose_name=_("تاریخ شروع"))
    start_date = models.DateField(verbose_name="تاریخ شروع", default="1400-01-01")
    designer = models.CharField(max_length=100, verbose_name=_("طراح"), default="نام پیش‌فرض طراح")


    class Meta:
        verbose_name = _("پروژه")
        verbose_name_plural = _("پروژه‌ها")

    def __str__(self):
        return self.title
