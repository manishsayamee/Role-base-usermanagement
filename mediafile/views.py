from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import FileCreateForm, commentForm
from .models import UploadFile, Comment
from accounts.decorators import maker_required, checker_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
# @maker_required
class uploadfile_createView(CreateView):
  template_name = 'mediafile/create.html'
  form_class = FileCreateForm
  success_url = '/files/list/'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.author = self.request.user
    self.object.save()
    return super().form_valid(form)


class uploadfile_listView(ListView):
  template_name = 'mediafile/list.html'
  model = UploadFile
  context_object_name = 'data'
  queryset = UploadFile.objects.all()



@method_decorator(login_required, name='dispatch')
class updateview(UpdateView):
  form_class = FileCreateForm
  success_url = '/files/list/'
  model = UploadFile
  template_name = 'mediafile/update.html'


@method_decorator(login_required, name='dispatch')
class deleteview(DeleteView):
  model = UploadFile
  success_url = '/files/list'

  def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)

  


def commentview(request, pk):
  template_name = 'comment.html'
  post = get_object_or_404(UploadFile, id=pk)
  comments = post.comments.filter(active=True)
  new_comment = None
  if request.method == 'POST':
  
    comment_form = commentForm(data=request.POST)
    if comment_form.is_valid():

      new_comment = comment_form.save(commit=False)
      new_comment.post = post
      new_comment.save()
  else:
    comment_form = commentForm()

  return render(request, template_name, {'post': post,
                                          'comments': comments,
                                          'new_comment': new_comment,
                                          'comment_form': comment_form})

