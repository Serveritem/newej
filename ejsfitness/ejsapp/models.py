from django.db import models

# Create your models here.
class MainPhotos(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main', blank=True, null=True)
    def __str__(self):
        return self.name

class Head(models.Model):
    name1 = models.CharField(max_length=250)
    description1 = models.TextField(max_length=250)
    name2 = models.CharField(max_length=250)
    description2 = models.TextField(max_length=250)
    name3 = models.CharField(max_length=250)
    description3 = models.TextField(max_length=250)
    name4 = models.CharField(max_length=250)
    description4 = models.TextField(max_length=250)
    name5 = models.CharField(max_length=250)
    description5 = models.TextField(max_length=250)
    name6 = models.CharField(max_length=250)
    description6 = models.TextField(max_length=250)


class TrainersGroup(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='trainersgroup', blank=True, null=True)
    def __str__(self):
        return self.name


class Part(models.Model):
    name1 = models.CharField(max_length=250)
    description1 = models.TextField(max_length=250)
    name2 = models.CharField(max_length=250)
    description2 = models.TextField(max_length=250)
    name3 = models.CharField(max_length=250)
    description3 = models.TextField(max_length=250)


class Benefits(models.Model):
    name1 = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description1 = models.TextField(max_length=1000)
    name2 = models.CharField(max_length=250)
    image2 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description2 = models.TextField(max_length=1000)
    name3 = models.CharField(max_length=250)
    image3 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description3 = models.TextField(max_length=1000)
    name4 = models.CharField(max_length=250)
    image4 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description4 = models.TextField(max_length=1000)
    name5 = models.CharField(max_length=250)
    image5 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description5 = models.TextField(max_length=1000)
    name6 = models.CharField(max_length=250)
    image6 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description6 = models.TextField(max_length=1000)
    name7 = models.CharField(max_length=250)
    image7 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description7 = models.TextField(max_length=1000)
    name8 = models.CharField(max_length=250)
    image8 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description8 = models.TextField(max_length=1000)
    name9 = models.CharField(max_length=250)
    image9 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description9 = models.TextField(max_length=1000)
    name10 = models.CharField(max_length=250)
    image10 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description10 = models.TextField(max_length=1000)

class Trainer(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='trainer', blank=True, null=True)
    description=models.TextField(max_length=250)
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='testimonial', blank=True, null=True)
    profession=models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    date = models.DateField()
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name
class GalleryPhotos(models.Model):
    name1 = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='blog', blank=True, null=True)
    image2 = models.ImageField(upload_to='blog', blank=True, null=True)
    image3 = models.ImageField(upload_to='blog', blank=True, null=True)
    image4 = models.ImageField(upload_to='blog', blank=True, null=True)
    image5 = models.ImageField(upload_to='blog', blank=True, null=True)
    image6 = models.ImageField(upload_to='blog', blank=True, null=True)
    image7 = models.ImageField(upload_to='blog', blank=True, null=True)
    image8 = models.ImageField(upload_to='blog', blank=True, null=True)

    name2 = models.CharField(max_length=250)
    image01 = models.ImageField(upload_to='blog', blank=True, null=True)
    image02 = models.ImageField(upload_to='blog', blank=True, null=True)
    image03 = models.ImageField(upload_to='blog', blank=True, null=True)
    image04 = models.ImageField(upload_to='blog', blank=True, null=True)
    image05 = models.ImageField(upload_to='blog', blank=True, null=True)
    image06 = models.ImageField(upload_to='blog', blank=True, null=True)
    image07 = models.ImageField(upload_to='blog', blank=True, null=True)
    image08 = models.ImageField(upload_to='blog', blank=True, null=True)

    name3 = models.CharField(max_length=250)
    image001 = models.ImageField(upload_to='blog', blank=True, null=True)
    image002 = models.ImageField(upload_to='blog', blank=True, null=True)
    image003 = models.ImageField(upload_to='blog', blank=True, null=True)
    image004 = models.ImageField(upload_to='blog', blank=True, null=True)
    image005 = models.ImageField(upload_to='blog', blank=True, null=True)
    image006 = models.ImageField(upload_to='blog', blank=True, null=True)
    image007 = models.ImageField(upload_to='blog', blank=True, null=True)
    image008 = models.ImageField(upload_to='blog', blank=True, null=True)

    name4 = models.CharField(max_length=250)
    image0001 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0002 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0003 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0004 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0005 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0006 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0007 = models.ImageField(upload_to='blog', blank=True, null=True)
    image0008 = models.ImageField(upload_to='blog', blank=True, null=True)

    name5 = models.CharField(max_length=250)
    image00001 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00002 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00003 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00004 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00005 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00006 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00007 = models.ImageField(upload_to='blog', blank=True, null=True)
    image00008 = models.ImageField(upload_to='blog', blank=True, null=True)

    name6 = models.CharField(max_length=250)
    image000001 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000002 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000003 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000004 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000005 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000006 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000007 = models.ImageField(upload_to='blog', blank=True, null=True)
    image000008 = models.ImageField(upload_to='blog', blank=True, null=True)

