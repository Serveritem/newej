from django.shortcuts import render
from . models import MainPhotos
from . models import TrainersGroup
from . models import Trainer
from . models import Testimonial
from . models import Blog
from . models import Head
from . models import Part
from . models import Benefits
from . models import GalleryPhotos
from django.core.mail import send_mail


# Create your views here.
def index(request):
    mainphotos=MainPhotos.objects.all()
    trainersgroup=TrainersGroup.objects.all()
    trainr=Trainer.objects.all()
    testimonial=Testimonial.objects.all()
    blog=Blog.objects.all()
    head=Head.objects.all()
    part = Part.objects.all()
    benefits=Benefits.objects.all()

    return render(request,'index.html',{'result':trainr,'tes':testimonial,'blo':blog,
                                        'main':mainphotos,'trainers':trainersgroup,'hea':head,'par':part,'ben':benefits})

def about(request):
    trainr = Trainer.objects.all()
    trainersgroup = TrainersGroup.objects.all()
    part = Part.objects.all()
    return render(request,'about.html',{'result':trainr,'trainers':trainersgroup,'par':part})


def feature(request):
    benefits = Benefits.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request,'feature.html',{'tes':testimonial,'ben':benefits })


def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog.html',{'blo':blog})

def training(request):
    head = Head.objects.all()
    return render(request,'training.html',{'hea':head})

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    gallery = GalleryPhotos.objects.all()
    return render(request,'gallery.html',{'gala':gallery})







