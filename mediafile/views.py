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



@login_required
@checker_required
def updateview(request, pk):
  user_object = get_object_or_404(UploadFile, author_id=pk)
  if request.method == 'POST':
      form = FileCreateForm(
          request.POST, instance=user_object
      )
      if form.is_valid():
          print("form is valid")
          print(form.cleaned_data)
          form.save()
          return redirect(f'/files/update/{pk}')
      else:
          print("form is invalid")
  else:
      form = FileCreateForm(instance=user_object)

  return render(request, 'accounts/update.html', {
      'form': form
  })
@login_required
@checker_required
def deleteview(request,pk):
  obj = get_object_or_404(UploadFile,author_id=pk)
  obj.delete()
  return redirect(request, '/files/list/')

  


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

