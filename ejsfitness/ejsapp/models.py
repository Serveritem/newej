from django.db import models

# Create your models here.
class MainPhotos(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main', blank=True, null=True)
    def __str__(self):
        return self.name

class Head(models.Model):
    name1 = models.CharField(max_length=250)
    description1 = models.TextField(max_length=2000)
    name2 = models.CharField(max_length=250)
    description2 = models.TextField(max_length=2000)
    name3 = models.CharField(max_length=250)
    description3 = models.TextField(max_length=2000)
    name4 = models.CharField(max_length=250)
    description4 = models.TextField(max_length=2000)
    name5 = models.CharField(max_length=250)
    description5 = models.TextField(max_length=2000)
    name6 = models.CharField(max_length=250)
    description6 = models.TextField(max_length=2000)


class TrainersGroup(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='trainersgroup', blank=True, null=True)
    def __str__(self):
        return self.name


class Part(models.Model):
    name1 = models.CharField(max_length=250)
    description1 = models.TextField(max_length=2000)
    name2 = models.CharField(max_length=205)
    description2 = models.TextField(max_length=2000)
    name3 = models.CharField(max_length=250)
    description3 = models.TextField(max_length=2000)


class Benefits(models.Model):
    name1 = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description1 = models.TextField(max_length=2000)
    name2 = models.CharField(max_length=250)
    image2 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description2 = models.TextField(max_length=2000)
    name3 = models.CharField(max_length=250)
    image3 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description3 = models.TextField(max_length=2000)
    name4 = models.CharField(max_length=250)
    image4 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description4 = models.TextField(max_length=2000)
    name5 = models.CharField(max_length=250)
    image5 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description5 = models.TextField(max_length=2000)
    name6 = models.CharField(max_length=250)
    image6 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description6 = models.TextField(max_length=2000)
    name7 = models.CharField(max_length=250)
    image7 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description7 = models.TextField(max_length=2000)
    name8 = models.CharField(max_length=250)
    image8 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description8 = models.TextField(max_length=2000)
    name9 = models.CharField(max_length=250)
    image9 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description9 = models.TextField(max_length=2000)
    name10 = models.CharField(max_length=250)
    image10 = models.ImageField(upload_to='benefits', blank=True, null=True)
    description10 = models.TextField(max_length=2000)

class Trainer(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='trainer', blank=True, null=True)
    description=models.TextField(max_length=250)
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='testimonial', blank=True, null=True)
    profession=models.TextField(max_length=250)
    description = models.TextField(max_length=2000)
    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    date = models.DateField()
    description = models.TextField(max_length=2000)
    def __str__(self):
        return self.name

class Gallery(models.Model):
    name1 = models.CharField(max_length=250)
    image101 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image102 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image103 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image104 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image105 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image106 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image107 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image108 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image109 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image110 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image111 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image112 = models.ImageField(upload_to='gallery', blank=True, null=True)
    description101 = models.TextField(max_length=500)
    description102 = models.TextField(max_length=500)
    description103 = models.TextField(max_length=500)
    description104 = models.TextField(max_length=500)
    description105 = models.TextField(max_length=500)
    description106 = models.TextField(max_length=500)
    description107 = models.TextField(max_length=500)
    description108 = models.TextField(max_length=500)
    description109 = models.TextField(max_length=500)
    description110 = models.TextField(max_length=500)
    description111 = models.TextField(max_length=500)
    description112 = models.TextField(max_length=500)

    name2 = models.CharField(max_length=250)
    image201 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image202 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image203 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image204 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image205 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image206 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image207 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image208 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image209 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image210 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image211 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image212 = models.ImageField(upload_to='gallery', blank=True, null=True)
    description201 = models.TextField(max_length=500)
    description202 = models.TextField(max_length=500)
    description203 = models.TextField(max_length=500)
    description204 = models.TextField(max_length=500)
    description205 = models.TextField(max_length=500)
    description206 = models.TextField(max_length=500)
    description207 = models.TextField(max_length=500)
    description208 = models.TextField(max_length=500)
    description209 = models.TextField(max_length=500)
    description210 = models.TextField(max_length=500)
    description211 = models.TextField(max_length=500)
    description212 = models.TextField(max_length=500)

    name3 = models.CharField(max_length=250)
    image301 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image302 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image303 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image304 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image305 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image306 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image307 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image308 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image309 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image310 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image311 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image312 = models.ImageField(upload_to='gallery', blank=True, null=True)
    description301 = models.TextField(max_length=500)
    description302 = models.TextField(max_length=500)
    description303 = models.TextField(max_length=500)
    description304 = models.TextField(max_length=500)
    description305 = models.TextField(max_length=500)
    description306 = models.TextField(max_length=500)
    description307 = models.TextField(max_length=500)
    description308 = models.TextField(max_length=500)
    description309 = models.TextField(max_length=500)
    description310 = models.TextField(max_length=500)
    description311 = models.TextField(max_length=500)
    description312 = models.TextField(max_length=500)

    name4 = models.CharField(max_length=250)
    image401 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image402 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image403 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image404 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image405 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image406 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image407 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image408 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image409 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image410 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image411 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image412 = models.ImageField(upload_to='gallery', blank=True, null=True)
    description401 = models.TextField(max_length=500)
    description402 = models.TextField(max_length=500)
    description403 = models.TextField(max_length=500)
    description404 = models.TextField(max_length=500)
    description405 = models.TextField(max_length=500)
    description406 = models.TextField(max_length=500)
    description407 = models.TextField(max_length=500)
    description408 = models.TextField(max_length=500)
    description409 = models.TextField(max_length=500)
    description410 = models.TextField(max_length=500)
    description411 = models.TextField(max_length=500)
    description412 = models.TextField(max_length=500)

    name5 = models.CharField(max_length=250)
    image501 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image502 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image503 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image504 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image505 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image506 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image507 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image508 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image509 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image510 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image511 = models.ImageField(upload_to='gallery', blank=True, null=True)
    image512 = models.ImageField(upload_to='gallery', blank=True, null=True)
    description501 = models.TextField(max_length=500)
    description502 = models.TextField(max_length=500)
    description503 = models.TextField(max_length=500)
    description504 = models.TextField(max_length=500)
    description505 = models.TextField(max_length=500)
    description506 = models.TextField(max_length=500)
    description507 = models.TextField(max_length=500)
    description508 = models.TextField(max_length=500)
    description509 = models.TextField(max_length=500)
    description510 = models.TextField(max_length=500)
    description511 = models.TextField(max_length=500)
    description512 = models.TextField(max_length=500)




class LastPhotos(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='last')
    def __str__(self):
        return self.name

class Programs(models.Model):
    name = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='last')
    image2 = models.ImageField(upload_to='last')
    description = models.TextField(max_length=2000)
    def __str__(self):
        return self.name

