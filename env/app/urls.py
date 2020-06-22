from django.contrib import admin
from django.urls import include, path
 
from .models import Item,F_Item
from .views import C_View,f_index,CustomerView,ItemCreateView, ItemDetailView, ItemCreateView, ItemUpdateView, F_ItemDeleteView

# アプリケーションのルーティング設定


urlpatterns = [
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
#    path('accounts/', include('django.contrib.auth.urls'),name='accounts'), #  追加
    path('create/', ItemCreateView.as_view(), name='create'),
    path('C_View/',C_View,name = 'C_View'),
    path('F_View/',F_View,name = 'F_View'),
    path('f_create/', ItemCreateView.as_view(template_name='app/item_form.html'), name='F_create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', F_ItemDeleteView.as_view(), name='delete'),
    path('', CustomerView.as_view(), name='index'),
#    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # [追加]

]

