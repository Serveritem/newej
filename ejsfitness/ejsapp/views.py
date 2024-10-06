from django.shortcuts import render
from . models import MainPhotos
from . models import TrainersGroup
from . models import Trainer
from . models import Testimonial
from . models import Blog
from . models import Head
from . models import Part
from . models import Benefits
from . models import Gallery
from . models import LastPhotos
from . models import Programs

# Create your views here.
def index(request):
    mainphotos=MainPhotos.objects.all()
    trainersgroup=TrainersGroup.objects.all()
    programs=Programs.objects.all()
    trainr=Trainer.objects.all()
    testimonial=Testimonial.objects.all()
    blog=Blog.objects.all()
    head=Head.objects.all()
    part = Part.objects.all()
    benefits=Benefits.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request,'index.html',{'result':trainr,'tes':testimonial,'blo':blog,
                                        'main':mainphotos,'trainers':trainersgroup,'hea':head,'par':part,'ben':benefits,"last":lastphotos,"pro":programs})

def about(request):
    trainr = Trainer.objects.all()
    trainersgroup = TrainersGroup.objects.all()
    part = Part.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request,'about.html',{'result':trainr,'trainers':trainersgroup,'par':part,"last":lastphotos})


def feature(request):
    benefits = Benefits.objects.all()
    testimonial = Testimonial.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request,'feature.html',{'tes':testimonial,'ben':benefits,"last":lastphotos})


def blog(request):
    blog = Blog.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request,'blog.html',{'blo':blog,"last":lastphotos})

def training(request):
    head = Head.objects.all()
    programs=Programs.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request,'training.html',{'hea':head,"last":lastphotos,"pro":programs})

def contact(request):
    lastphotos = LastPhotos.objects.all()
    return render(request,'contact.html',{"last":lastphotos})

def gallery(request):
    gallery = Gallery.objects.all()
    lastphotos = LastPhotos.objects.all()
    return render(request, 'gallery.html', {'gal': gallery,"last":lastphotos})



def footer(request):

    return render(request,'footer.html')

