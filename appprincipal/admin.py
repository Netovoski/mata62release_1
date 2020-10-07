from django.contrib import admin
from projpad.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Hist_voo2015, Hist_voo2015_2, Hist_voo2015_3, Hist_voo2015_4, Hist_voo2015_5, Hist_voo2015_6, Hist_voo2015_7, Hist_voo2015_8, Hist_voo2015_9, Hist_voo2015_10, Hist_voo2015_11, Hist_voo2015_12, Hist_voo2016, Hist_voo2016_2, Hist_voo2016_3, Hist_voo2017)
#admin.site.register(Hist_voo2015)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
