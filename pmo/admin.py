from django.contrib import admin
from easy_select2 import select2_modelform
from .models import Os
from .models import Projeto
from .models import Sistema
from .models import Status
from .models import Atividade

ProjetoForm = select2_modelform(Projeto, attrs={'width': '250px'})
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'Sistemas', 'responsavel', 'horas_saldo')
    form = ProjetoForm
    def Sistemas(self, obj):
        return "\n".join([s.nome+' /' for s in obj.sistemas.all()])

admin.site.register(Os)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Sistema)
admin.site.register(Atividade)
admin.site.register(Status)



# Register your models here.
