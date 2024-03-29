from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin
from django.contrib.auth import login, logout

# from django.contrib.auth.forms import UserCreationForm - форма переопределена в forms.py в UserRegisterForm

from django.contrib import messages
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # используется подменная форма
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()  # используется подменная форма
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


# def test(request):
#     objects = ['aaaa1', 'aaaa2', 'aaaa3', 'aaaa4', 'aaaa5', 'aaaa6', 'aaaa7']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_obects = paginator.get_page(page_num)
#     return render(request, 'news/test.html', {'page_obj': page_obects})

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # используется подменная форма
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'faforpython@gmail.com', ['eur@yandex.ru'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()  # используется подменная форма

    return render(request, 'news/test.html', {'form': form})



class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'
    paginate_by = 2

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_publishes=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


# def index(request):
#     news = News.objects.all()
#
#     context = {'news': news,
#                'title': 'Список новостей',
#                }
#     return render(request, 'news/index.html', context)


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_publishes=True).select_related(
            'category')  # Загрузить данные сразу для связанной модели select_related('category')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home') # Будет работать get_absolute_url
    login_url = '/admin/'  # если не авторизован на страницу авторизации
    # raise_exception = True  # - в этом случае ошибка доступа

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # News.objects.create(**form.cleaned_data) // Для несвязанных форм
#             news = form.save()  # Для связанных с моделью
#             return redirect('home')
#     else:
#
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
