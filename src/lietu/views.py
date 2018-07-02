from importlib import import_module
from django.views.generic import DetailView, ListView
from .models import DogInfo, DogGroup
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class DogInfoViews(DetailView):
    """
    业务查询接口，可为API请求。
    :pk 模块名称
    :order_id 业务订单号
    :return 根据自定义脚本返回的信息返回。
    """
    model = DogInfo

    def get(self, request, *args, **kwargs):
        context = {'errmsg': None, 'rabbits': None}
        try:
            queryset = self.model.objects.filter(pk=request.GET.get('pk'))
            self.obj = queryset.first()
            context.update(self.get_context_data(order_id=request.GET.get('order_id')))
            self.obj.increase_use_times()
        except Exception as e:
            context['errmsg'] = '%s' % e
        return JsonResponse(context)

    def get_context_data(self, **kwargs):
        model_name = 'scriptfile.' + self.obj.script_file.name.split('.')[0]
        cage = import_module(model_name, package='src')
        dog = cage.Dog(self.obj)
        rabbits = dog.trace(kwargs['order_id'])
        context = {'rabbits': rabbits}
        return context


class DogListView(ListView):
    model = DogInfo
    template_name = 'lietu/dogs.html'
    context_object_name = 'dog_list'
    # paginate_by = 10


class DogGroupView(DogListView):
    def get_queryset(self):
        group = get_object_or_404(DogGroup, pk=self.kwargs.get('pk'))
        return super(DogGroupView, self).get_queryset().filter(dog_group=group)
