from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path("lgn/", ad.LoginView.as_view(template_name="html/login.html"), name="lg"),
	path('lgot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
	path('usrlst/',views.userlist,name="usrl"),
	 path('usrup/<int:h>/',views.userupdate,name="usp"),
    path('usrdel/<int:d>/',views.userdelete,name="usd"),
	path('chge/',views.chgepwd,name="cge"),
	path('pfle/',views.profile,name="pf"),
	path('upfle/',views.updprofile,name="upf"),
	path('propadd/',views.addprop,name="aprop"),
	path('propupd/<int:w>/',views.updprop,name="uprop"),
	path('propdel/<int:p>/',views.deleprop,name="dp"),
	path('propsell/<int:k>/',views.sellprop,name="sp"),
	path('proplista/',views.proplist,name="lprop"),
	path('allprop_a/',views.allprops,name="allprops"),
	path('allpropadet/<int:a>/',views.allpropsadet,name="apropdet"),
	path('myprop/',views.propmy,name="mp"),
	path('buyprop/',views.propbuy,name="bp"),
	path('buypropdet/<int:q>/',views.detbuyprop,name="bpdet"),
	path('mypropforb/',views.mypropbuy,name="mpb"),
	path('approval/',views.adapprov,name="appr"),
	path('approvdet/<int:k>/',views.detaofapp,name="appd"),
	path('approvesell/<int:h>/',views.updatesell,name="appupdsell"),
	path('buymail/<int:h1>/<int:h2>/',views.mailtosell,name="mts"),
	path('soldd/<int:k1>/',views.solddetails,name="soldet"),
]