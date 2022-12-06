from django.shortcuts import render, redirect
from . import models
from datetime import  timedelta
from django.db.models.functions import Length
# Create your views here.


def index (request):
    pemesanan = models.pelanggan.objects.all()
    index = []
    for item in pemesanan :
        dummy = []
        idpemesanan = item.idpelanggan
        detail = models.detaillayanan.objects.filter(idpelanggan = idpemesanan)
        dummy.append(item)
        dummy.append(detail)
        index.append(dummy)
    return render(request, 'index.html', {
        'index' : index,
    })

def delete (request, id):
    pelanggan = models.pelanggan.objects.get(idpelanggan = id)
    pelanggan.delete()
    return redirect ('index')

def updatepelanggan (request, id):
    pelanggan = models.pelanggan.objects.get(idpelanggan = id)
    layanan = models.layanan.objects.all()
    pemesanan = models.pemesanan.objects.all()
    

    if request.method == "GET":
        return render (request, 'updatepelanggan.html', {
            'pelanggan' : pelanggan,
            'layanan' : layanan,
            'pemesanan' : pemesanan
          
        })
    else:
        # metode = request.POST['metode']
        id_layanan = request.POST['idlayanan']
        pelanggan.namapelanggan = request.POST['namapelanggan']
        pelanggan.nohp = request.POST['nohp']
        pelanggan.alamat = request.POST['alamat']
        pelanggan.tanggalpesan = request.POST['tanggalpesan']
        pelanggan.statuscuci = request.POST['status']
        pelanggan.statushelm = request.POST['helm']
        
        getlayanan = models.layanan.objects.get(idlayanan = id_layanan)
        pelanggan.idlayanan = getlayanan
        # getmetode = models.pemesanan.objects.get(idlayanan = metode)
        # pemesanan.save()
        pelanggan.save()
        # pemesanan.idlayanan = getmetode
        # pemesanan.save()
        return redirect ('index')

def metodeantar(request):
    layanan = models.pemesanan.objects.all()
    #layanan = models.layanan.objects.exclude(jenislayanan__exact='-')
    pelanggan = models.pelanggan.objects.all()
    if request.method == "GET":
        return render(request, 'metodeantar.html', {
            'detail' : layanan,  
            'pelanggan' : pelanggan
        })
    else:
        idpelanggan = request.POST['idpelanggan']
        metodeambil = request.POST['metodeambil']
        getlayanan = models.pemesanan.objects.get(idpemesanan = metodeambil)
        getpelanggan = models.pelanggan.objects.get(idpelanggan = idpelanggan)
        # getid = models.detaillayanan.objects.get(idlayanan = idlayanan)
        # pemesanan_obj =  models.pemesanan.objects.all().last()
        newdetail = models.detaillayanan(
            idpelanggan = getpelanggan,
            idpemesanan = getlayanan
        ).save()
        # newdetail2 = models.pemesanan(
        #     idpelanggan = getpelanggan,
        # ).save()
            
        return redirect ('index')
def tambahpelanggan (request):
    # layanan = models.layanan.objects.exclude(metodeambil__exact='-')
    layananall = models.layanan.objects.exclude(jenislayanan__exact='‎')
    if request.method == "GET":
        return render (request, 'tambahpelanggan.html', {
            'layananall' : layananall,

        })
    else:
        namapelanggan = request.POST['namapelanggan']
        nohp = request.POST['nohp']
        alamat = request.POST['alamat']
        id_layanan = request.POST['idlayanan']
        tanggalpesan = request.POST['tanggalpesan']
        getlayanan = models.layanan.objects.get(idlayanan = id_layanan)
    
    newpelanggan = models.pelanggan(
        namapelanggan = namapelanggan,
        idlayanan = getlayanan,
        nohp = nohp,
        alamat = alamat,
        tanggalpesan = tanggalpesan,
        statuscuci = 'Belum tercuci',
        statushelm = 'Belum diambil',
        ).save()

    pelanggan = models.pelanggan.objects.all().last()
  
    # index = models.detaillayanan(
    #     idpelanggan = pelanggan,
    # ).save()
    return redirect ('metodeantar')

def detaillayanan(request, id):
    detailpemesanan = models.detaillayanan.objects.filter(idpelanggan = id)
    # pemesanan = models.pemesanan.objects.all()
    return render(request, 'detaillayanan.html', {
        'detailpemesanan' : detailpemesanan,
       
    })

def updatedetail (request, id):
    getpemesanan = models.detaillayanan.objects.get(iddetaillayanan=id)
    pemesanan = models.pemesanan.objects.all()
    if request.method == "GET":

        return render(request, 'updatedetail.html', {
            'pemesanan' : pemesanan,
            'getpemesanan' : getpemesanan,
        
        } )
    else:
        getpemesanan.idpemesanan.namadelivery = request.POST['namadelivery']
        # namadelivery = request.POST['namadelivery']
        metodeambil = request.POST['metodeambil']
        getmetode = models.pemesanan.objects.get(idpemesanan = metodeambil)
    
        getpemesanan.idpemesanan = getmetode
      
        # getpemesanan.idpemesanan.namadelivery = namadelivery
        getpemesanan.save()
        return redirect ('index')

def generate(request):
    if request.method =='GET':
        return render(request, 'generate.html')
    elif request.method =='POST':
        pemesanan = []
        total = []
        mulai = request.POST['mulai']
        akhir = request.POST['akhir']
        tampil = models.pelanggan.objects.filter(tanggalpesan__range=(mulai,akhir))
        for item in tampil:
            total2 = []
            dummy = []
            # print(item,'woy')
            id_pemesanan = item.idpelanggan
            specificdetail = models.detaillayanan.objects.filter(idpelanggan= id_pemesanan)
            dummy.append(item)
            dummy.append(specificdetail)
            pemesanan.append(dummy)
            for i in specificdetail:
                tes = models.pelanggan.objects.get(idpelanggan = i.idpelanggan.idpelanggan)
                tes2 = models.pemesanan.objects.get(idpemesanan = i.idpemesanan.idpemesanan)
                total.append(tes.idlayanan.harga)
                total.append(tes2.harga)
                #total.append(i.idpemesanan.harga)
                #total.append(i.idpelanggan.idlayanan.harga)
        
        jumlah = (total)
        totale = sum(total)
        
        return render(request, 'rekap.html',{
            'pemesanan' : pemesanan,
            'mulai' : mulai,
            'akhir' : akhir,
            'jumlah' : jumlah,
            'total' : totale
            
    })
    
def invoice(request, id):
    idinvoice = models.detaillayanan.objects.filter(idpelanggan = id)
    idinvoiceobj = models.detaillayanan.objects.all()
    tes = models.pelanggan.objects.get(idpelanggan=id)
    # totale = 0
    for x in idinvoice:
    #     total1 = x.idpemesanan.idpaketpelanggan.harga
    #     # total1.append(tes1)
    #     total2 = x.idlayanan.harga
    #     totale += total2
        total1 = x.idpelanggan.idlayanan.harga
        total2 = x.idpemesanan.harga
    total = total1+total2

   # total = idinvoice.idpemesanan.idpaketpelanggan.harga + idinvoice.idlayanan.harga
    if request.method == 'GET':
        return render(request, 'invoice.html',{
            'idinvoice' : idinvoice,
            'idinvoiceojb' : idinvoiceobj,
             'total' : total,
             
            
    })

def home(request):
    pemesanan = []
    total = []
    tampil = models.pelanggan.objects.all()
    for item in tampil:
        dummy = []
        # print(item,'woy')
        id_pemesanan = item.idpelanggan
        specificdetail = models.detaillayanan.objects.filter(idpelanggan= id_pemesanan)
        dummy.append(item)
        dummy.append(specificdetail)
        pemesanan.append(dummy)
        for i in specificdetail:
            tes = models.pelanggan.objects.get(idpelanggan = i.idpelanggan.idpelanggan)
            tes2 = models.pemesanan.objects.get(idpemesanan = i.idpemesanan.idpemesanan)
            total.append(i.idpemesanan.harga)
            total.append(i.idpelanggan.idlayanan.harga)
    totale = sum(total)
    totalpelanggan = models.pelanggan.objects.all().count()
    layanan = models.layanan.objects.all().count()
    layanan = int(layanan) 
    tes = models.detaillayanan.objects.all().count()
    # total = models.detaillayanan.objects.filter(iddetaillayanan = True)
    # # totale = 0
    # for x in total:
    #     total1 = x.idpelanggan.idlayanan.harga
    #     total2 = x.idpemesanan.harga
    #     totale += total1
    #     totale += total2

    return render(request, 'home.html', {
        'jumlah' : totalpelanggan,
        'layanan' : layanan,
        'tes' : tes,
        'total' : totale
    })
    
def indexlayanan(request):
    layanan = models.layanan.objects.all()

    return render(request, 'indexlayanan.html', {
        'layanan' : layanan
    })

def updatelayanan(request, id):
    layananobj = models.layanan.objects.get(idlayanan = id)
    layanan_obj = models.layanan.objects.all()
    if request.method == "GET":
        return render(request, 'updatelayanan.html', {
            'alllayananobj' : layananobj,
            'layananobj' : layanan_obj
        })
    else:

        layananobj.jenislayanan = request.POST['jenislayanan']
        layananobj.harga = request.POST['harga']
        layananobj.save()
        return redirect ('indexlayanan')

def deletelayanan(request, id):

    layanan = models.layanan.objects.get(idlayanan = id)
    layanan.delete()   
    return redirect('indexlayanan') 

def createlayanan(request):
    layanan = models.layanan.objects.all()
    if request.method == "GET":
        return render(request, 'createlayanan.html', {
        })
    else:
        jenislayanan = request.POST['jenislayanan']
        harga = request.POST['harga']

        newlayanan = models.layanan(
            jenislayanan = jenislayanan,
            harga = harga
        ).save()
        return redirect('indexlayanan')

def profile(request):
    return render(request, 'profile.html')

def adddetaillayanan(request):
    pemesanan = models.pemesanan.objects.all()
    pelanggan = models.pelanggan.objects.all()
    if request.method == "GET":
        return render(request, 'adddetaillayanan.html', {
            'pemesanan' : pemesanan,  
            'pelanggan' : pelanggan
        })
    else:
        idpelanggan = request.POST['idpelanggan']
        jenislayanan = request.POST['metode']
        getpemesanan = models.pemesanan.objects.get(idpemesanan = jenislayanan)
        getpelanggan = models.pelanggan.objects.get(idpelanggan = idpelanggan)
        # getid = models.detaillayanan.objects.get(idlayanan = idlayanan)
        # pemesanan_obj =  models.pemesanan.objects.all().last()
        newdetail = models.detaillayanan(
            idpelanggan = getpelanggan,
            idpemesanan = getpemesanan
        ).save()
        # newdetail2 = models.pemesanan(
        #     idpelanggan = getpelanggan,
        # ).save()
            
        return redirect ('index')