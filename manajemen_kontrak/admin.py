from django.contrib import admin
from .models import *

admin.site.register(UserAdmin)
admin.site.register(Barang)
admin.site.register(Penyedia)
admin.site.register(Kontrak)
admin.site.register(LampiranKontrak)
admin.site.register(FotoItemPekerjaan)
admin.site.register(TandaTerimaDistribusi)
admin.site.register(LampiranTandaTerima)
