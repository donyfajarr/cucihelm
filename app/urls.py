from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('tambahpelanggan', views.tambahpelanggan, name ='tambahpelanggan'),
    path('indexlayanan', views.indexlayanan, name ='indexlayanan'),
    path('deletelayanan/<str:id>', views.deletelayanan, name="deletelayanan"),
    path('updatelayanan/<str:id>', views.updatelayanan, name ='updatelayanan'),
    path('createlayanan', views.createlayanan, name ='createlayanan'),
    path('metodeantar', views.metodeantar, name="metodeantar"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('updatepelanggan/<str:id>', views.updatepelanggan, name ='updatepelanggan'),
    path('detaillayanan<str:id>', views.detaillayanan, name='detaillayanan'),
    path('adddetaillayanan', views.adddetaillayanan, name='adddetaillayanan'),
    path('updatedetail<str:id>', views.updatedetail, name='updatedetail' ),
    # path('deletedetail<str:id>', views.deletedetail, name='deletedetail'),
    path('invoice/<str:id>', views.invoice, name='invoice'),
    path('profile', views.profile, name='profile'),
    path('rekap', views.generate, name='rekap'),
    path('generate', views.generate, name='generate')
]