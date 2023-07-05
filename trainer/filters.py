import django_filters
from trainer.models import Trainer


class TrainerFilters(django_filters.FilterSet):
    get_trainers = [(trainer.first_name, trainer.first_name.upper()) for trainer in Trainer.objects.filter(active=True)]
    first_name = django_filters.ChoiceFilter(choices=list(set(get_trainers)))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    course = django_filters.CharFilter(lookup_expr='exact', label='Course')
#    department =
    
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.filters['course'].field.widget.attrs.update({'class': 'form-control',
                                                          'placeholder': 'Please enter course'})
