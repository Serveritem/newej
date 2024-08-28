from django.contrib import admin
from . models import MainPhotos
from . models import Trainer
from . models import Testimonial
from . models import Blog
from . models import TrainersGroup
from . models import Head
from . models import Part
from . models import Benefits
from . models import GalleryPhotos

admin.site.register(MainPhotos)
admin.site.register(TrainersGroup)
admin.site.register(Trainer)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Head)
admin.site.register(Part)
admin.site.register(Benefits)
admin.site.register(GalleryPhotos)
