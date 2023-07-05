from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from student.filters import StudentFilters
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from trainer.models import Trainer


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    success_message = "Student {first_name} {last_name} was created successfully"
    permission_required = 'student.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.last_name = new_student.last_name.title()
            new_student.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(first_name=self.object.first_name, last_name=self.object.last_name)


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_student_list'

    def get_queryset(self):
        return Student.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.now()
        data['current_date_time'] = now
        trainers = Trainer.objects.all()
        data['get_all_trainers'] = trainers
        students = Student.objects.filter(active=True)
        my_filter = StudentFilters(self.request.GET, queryset=students)
        students = my_filter.qs
        data['all_students'] = students
        data['form_filters'] = my_filter.form
        return data


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')
    success_message = "Student %(first_name_field)s  %(last_name_field)s was updated successfully  "
    permission_required = 'student.change_student'
    permission_denied_message = 'Permission denied today'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    success_message = "Student %(first_name_field)s  %(last_name_field)s was deleted successfully"
    permission_required = 'student.delete_student'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class StudentDetailsView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/student_details.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.view_student'
