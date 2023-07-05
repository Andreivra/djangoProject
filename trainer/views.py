from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from trainer.filters import TrainerFilters
from trainer.models import Trainer
from trainer.forms import TrainerForm, TrainerUpdateForm


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')
    success_message = "Student {first_name} {last_name} was created successfully"
    permission_required = 'trainer.add_trainer'

    def form_valid(self, form):
        if form.is_valid():
            new_trainer = form.save(commit=False)
            new_trainer.first_name = new_trainer.first_name.title()
            new_trainer.last_name = new_trainer.last_name.title()
            new_trainer.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(first_name=self.object.first_name, last_name=self.object.last_name)


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data1 = super().get_context_data(**kwargs)
        students = Trainer.objects.all()
        data1['get_all_trainers'] = students
        trainers = Trainer.objects.filter(active=True)
        my_filter = TrainerFilters(self.request.GET, queryset=trainers)
        trainers = my_filter.qs
        data1['all_trainers'] = trainers
        data1['form_filters'] = my_filter.form
        return data1


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-of-trainers')
    success_message = "Student %(first_name_field)s  %(last_name_field)s was updated successfully  "
    permission_required = 'trainer.change_trainer'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    success_message = "Student %(first_name_field)s  %(last_name_field)s was deleted successfully"
    permission_required = 'trainer.delete_trainer'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class TrainerDetailsView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/trainer_details.html'
    model = Trainer
    success_url = reverse_lazy('list-of-students')
    permission_required = 'trainer.view_trainer'
