from django.db import models

# Create your models here.
class layanan(models.Model):
    idlayanan = models.AutoField(primary_key=True)
    jenislayanan = models.CharField(max_length=30)
    harga = models.IntegerField()
    
    def __str__(self):
        return str(self.jenislayanan)

class pelanggan(models.Model):
    idpelanggan = models.AutoField(primary_key=True)
    idlayanan = models.ForeignKey(layanan,on_delete=models.CASCADE)
    statuscuci = models.CharField(max_length=50)
    statushelm = models.CharField(max_length=50)
    namapelanggan = models.CharField(max_length=50)
    nohp = models.IntegerField()
    alamat = models.CharField(max_length=50)
    tanggalpesan = models.DateField()


    def __str__(self):
        return str(self.idpelanggan)

class pemesanan(models.Model):
    idpemesanan = models.AutoField(primary_key=True)
    metodeambil = models.CharField(max_length=35)
    namadelivery = models.CharField(max_length=50)
    harga = models.IntegerField()

    def __str__(self):
        return str(self.metodeambil)

class detaillayanan(models.Model):
    iddetaillayanan = models.AutoField(primary_key=True)
    idpemesanan = models.ForeignKey(pemesanan, on_delete=models.CASCADE)
    idpelanggan = models.ForeignKey(pelanggan, on_delete=models.CASCADE)