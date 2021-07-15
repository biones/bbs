from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .form import WriteForm
from .models import Posts

class IndexView(View):
    def get(self, request, *args, **kwargs):
        queryset = Posts.objects.all().order_by('-created_at')
        return render(request, 'post.html', {'posts': queryset})


index = IndexView.as_view()


class WriteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'write.html', {'form': WriteForm})

    def post(self, request, *args, **kwargs):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # indexのviewに移動
        return redirect(to='bbs:index')


write = WriteView.as_view()