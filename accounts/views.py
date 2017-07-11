
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, MypageForm
from accounts.models import Profile

from django.contrib import messages

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import login as default_login_view
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def user_list(request):
    qs = Profile.objects.all().prefetch_related()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(server__icontains=q)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page',1)
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profile = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profile = paginator.page(paginator.num_pages)


    return render(request, 'accounts/user_list.html',{
        'user_list' : qs,
        'profile' : profile,
    })

@login_required
def mypage(request):
	message='get method'
	if request.method == "POST":
		test='post'
		mypageform=MypageForm(request.POST)
		if mypageform.is_valid():
			profile = Profile.objects.get(user=request.user)
			profile.userid = mypageform.cleaned_data['userid']
			profile.skill = mypageform.cleaned_data['skill']
			profile.context = mypageform.cleaned_data['context']
			profile.server = mypageform.cleaned_data['server']
			profile.race = mypageform.cleaned_data['race']
			profile.save()
			user=request.user
			user.save()
			messages.success(request, '마이페이지가 작성됐습니다. 유저 목록을 확인해주세요.')
		else:
			message = mypageform.errors
	user=User.objects.get(id=request.user.id)
	#프로필 있는지 확인 없으면생성
	try:
		profile=Profile.objects.get(user=request.user)
	except:
		new_profile=Profile(user=request.user)
		new_profile.save()
	mypageform = MypageForm({'userid':user.profile.userid,'skill':user.profile.skill,
							'context':user.profile.context,'server':user.profile.server,
							'race':user.profile.race})
	return render(request,"accounts/mypage.html", {
			'message':message, 'mypageform':mypageform
	})


def signup(request):
    if request.method=="POST":
        userform = SignupForm(request.POST)
        if userform.is_valid():
            user=userform.save(commit=False)
            user.username = userform.cleaned_data['username']
            user.save()
            profile = Profile(user=user)
            profile.save()
            messages.success(request, '회원가입을 완료했습니다.\n 로그인 해주세요.')
            return HttpResponseRedirect(reverse("signup_ok"))
        return render(request, "accounts/signup_form.html", {
            'userform': userform,
            'message':'입력정보를 정확히 확인해주세요.',
		})
    elif request.method=="GET":
        userform = SignupForm()
        return render(request, "accounts/signup_form.html", {
            'userform':userform,
            'message':'회원가입 후 마이페이지에 정보 입력시 자동으로 유저리스트에 올라갑니다.',
		})

# @login_required
# def profile(request):
#     return render(request, 'accounts/mypage.html')
#특정 뷰가 호출될때 로그아웃 상황이 아닌
#로그인상황에서만 호출이 되도록 강제시킬려면 장식자를 사용 @login_required
