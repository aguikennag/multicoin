
from django.shortcuts import render
from django.views.generic import ListView,View,RedirectView,TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.forms.models import model_to_dict
from wallet.models import Investment, Wallet,WithdrawalApplication as WA,Transaction as TR
from django.db.models import Sum

from .forms import KycForm
from .models import KYC
from django.http import JsonResponse,HttpResponse


class Dashboard(LoginRequiredMixin,TemplateView) :
    template_name = 'dashboard.html'

    def get_context_data(self,*args,**kwargs) :
     
        ctx = super(Dashboard,self).get_context_data(*args,**kwargs)  
        try : ctx['pending_deposit'] = self.request.user.user_pending_deposit.all().aggregate(
            total = Sum("amount")
        )['total']
        except : pass
        try : ctx['pending_withdrawal'] = self.request.user.pending_withdrawal.filter(
            status = "PENDING"
        ).aggregate(
            total = Sum("amount")
        )['total']
        except : pass
        ctx['recent_transactions'] = TR.objects.filter(user=self.request.user)[:6]
        init = self.request.user.username[0] 
        ctx['initial'] = init.upper()

        return ctx

    def get(self,request,*args,**kwargs)   :
        user = request.user
        user.handle_due_investments()
        #if request.user.user_wallet.plan_is_active and request.user.user_wallet.plan_is_due :
            #request.user.user_wallet.on_plan_complete()
        
        return render(request,self.template_name,self.get_context_data())    


class Transaction(LoginRequiredMixin,ListView) :
    model = TR
    template_name= 'user-transactions.html'
    context_object_name = "transactions"
    
    def get_queryset(self) :
        return self.model.objects.filter(user = self.request.user)



class KYC(LoginRequiredMixin,View) :
    template_name = "kyc.html"
    form_class = KycForm
    model = KYC

    def get(self,request,*args,**kwargs) :
        """if self.model.objects.filter(user = request.user,is_accepted = False).exists() :
            return HttpResponse("You already have a pending kyc request, and it's been processed.")"""
        data = model_to_dict(request.user)
        name = data.get("name")
        if name and name != "" : 
            data['first_name'] = name.split()[0]
            data['last_name'] = name.split()[1]
        return render(request,self.template_name,locals())
        

    def post(self,request,*args,**kwargs)    :
        """if self.model.objects.filter(user = request.user,is_accepted = False).exists() :
            return HttpResponse("You already have a pending kyc request, and it's been processed.")"""
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid() :
            form.instance.user = request.user
            form.save()
            return JsonResponse(
                {"success" : True,
                "success_url" : reverse("dashboard") 
                }
             )

        else :
            return JsonResponse(
                {"error" : True,
                "error_response" : form.errors.as_json()
                }
            )    


    

class Referral (LoginRequiredMixin,TemplateView) :

    template_name= 'referral.html'

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        try : 
            ctx['pending_withdrawal'] = WA.objects.filter(user=self.request.user,balance_type = "Referral",status="PENDING")[0].amount
        except : pass
        prepend = "https://" if self.request.is_secure() else "http://"
        host = prepend + self.request.get_host()
        ctx['referral_link'] = "{}{}?ref_id={}".format(host,reverse("register"),self.request.user.referral_id)
        return ctx



