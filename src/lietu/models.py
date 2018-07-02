from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class DogGroup(models.Model):
    name = models.CharField('分类', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组管理'


class DogInfo(models.Model):
    dog_group = models.ForeignKey(DogGroup, on_delete=models.CASCADE, related_name='doginfo', verbose_name='分组')
    dog_trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dogtrainer', verbose_name='上传者')
    dog_name = models.CharField('名称', max_length=32)
    # dog_tid = models.CharField('唯一ID', max_length=32, unique=True, db_index=True)
    dog_info = models.TextField('描述', max_length=255)
    script_file = models.FileField('执行脚本', upload_to='')
    condition = models.SmallIntegerField('必要条件', default=1)  # 0：无需条件，1：1个order_id（默认查单），
    use_times = models.PositiveIntegerField('引用次数', default=0)
    work_zan = models.PositiveIntegerField('赞', default=0)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def increase_use_times(self):
        self.use_times += 1
        self.save(update_fields=['use_times'])

    def increase_zan(self):
        self.work_zan += 1
        self.save(update_fields=['work_zan'])

    def get_absolute_url(self):
        return reverse('lietu:trace', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-use_times', '-create_time']
        verbose_name = '小狗'
        verbose_name_plural = '小狗管理'

    def __str__(self):
        return self.dog_name


class Mountain(models.Model):
    DB_TYPE = {
        'mysql': 'mysql',
        'oracle': 'oracle',
        'other': 'other',
    }
    dogs = models.ForeignKey(DogInfo, on_delete=models.CASCADE, related_name='databases')
    db_type = models.CharField('数据库类型', max_length=32, choices=DB_TYPE.items())
    db_name = models.CharField('数据库名称', max_length=64)
    db_host = models.CharField('主机', max_length=64)
    db_port = models.CharField('端口', max_length=16)
    db_user = models.CharField('用户', max_length=64)
    db_pwd = models.CharField('密码', max_length=64)

    def __str__(self):
        return self.db_name

    class Meta:
        verbose_name = '关联DB'
        verbose_name_plural = '关联DB管理'
