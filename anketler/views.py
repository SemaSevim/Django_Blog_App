from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .common import insert_soru,select_soru,update_soru
from datetime import datetime
from .models import Soru,Secim
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic




def index(request):
    son_sorular_listesi = Soru.objects.order_by('-yayim_tarihi')[:5]
    template = loader.get_template('index.html')
    cikti = {
        'son_sorular_listesi': son_sorular_listesi,
    }
    return HttpResponse(template.render(cikti, request))

# class IndexView(generic.ListView):
#     tema_adi = 'anketler/index.html'
#     baglam_nesnesinin_adi = 'son_sorular_listesi'

#     def get_queryset(self):
#         """En son yayınlanan 5 soruyu getir."""
#         return Soru.objects.order_by('-yayim_tarihi')[:5]


class AyrintiView(generic.DetailView):
    model = Soru
    tema_adi = 'anketler/ayrinti.html'


class SonuclarView(generic.DetailView):
    model = Soru
    tema_adi = 'anketler/sonuclar.html'

def oy(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    try:
        secim_secildi = soru.secim_set.get(pk=request.POST['secim'])
    except (KeyError, Secim.DoesNotExist):
          # Soruyu oylama biçimini yeniden görüntüleme.
        return render(request, 'anketler/ayrinti.html', {
            'soru': soru,
            'hata_mesaji': "Herhangi bir seçim yapmadınız.",
        })
    else:
        secim_secildi.oylar += 1
        secim_secildi.save()
        # POST verileri her zmaan bir HttpResponseRedirect döndürür. Bu, bir kullanıcı "geri" düğmesine basarsa verilerin iki kez gönderilmesini önler.
        return HttpResponseRedirect(reverse('anketler:sonuclar', args=(soru.id,)))
          

# def index(request):
#     son_sorular_listesi = Soru.objects.order_by('-yayim_tarihi')[:5]
#     cikti = {'son_sorular_listesi': son_sorular_listesi}
#     return render(request, 'anketler/index.html', cikti)

# def ayrinti(request, soru_id):
#     soru = get_object_or_404(Soru, pk=soru_id)
#     return render(request, 'anketler/ayrinti.html', {'soru': soru})       
    


# def sonuclar(request, question_id):
#     soru = get_object_or_404(Soru, pk=question_id)
#     return render(request, 'anketler/sonuclar.html', {'soru': soru})    
