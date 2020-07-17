from django import forms
from myapp.models import Order


class OrderForm(forms.Form):
    """ based on the Order model to create the form """
    class Meta:
        model = Order
        fields = ('student', 'course', 'levels', 'order_date')
        widgets = {
            'student': forms.RadioSelect(attrs={'class': 'radio'}),
            'order_date': forms.SelectDateWidget(attrs={'class': 'years=date.today()'}),
        }
        Labels = {
            'student': 'Student Name',
            'order_date': 'Order Date',
        }


class InterestForm(forms.Form):
    CHOICES = (
        ('1', 'Yes'),
        ('0', 'No'),
    )

    interested = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
    levels = forms.IntegerField(initial=1)
    comments = forms.CharField(widget=forms.Textarea(), required=False, label="Additional Comments")