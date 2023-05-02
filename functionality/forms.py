from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime

from functionality.models import Activity


class ActivityForm(forms.Form):
    activity_name = forms.CharField(max_length = 200)
    # user_id = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    date_time_start = forms.DateTimeField(widget=AdminDateWidget())
    # date_time_finish = forms.DateTimeField(widget=AdminDateWidget())
    # date_time_added = models.DateTimeField()
    record_description = forms.CharField(max_length=2000)
    date_time_start = forms.SplitDateTimeField(widget = AdminSplitDateTime())
    duration = forms.IntegerField()
    # completion = forms.DecimalField(decimal_places=3)
    # date_time_finish = forms.SplitDateTimeField(widget = AdminSplitDateTime())

# class ActivityForm(forms.ModelForm):
#     date_time_start = forms.SplitDateTimeField(widget = AdminSplitDateTime())
#     date_time_finish = forms.SplitDateTimeField(widget = AdminSplitDateTime())
#     class Meta:
#         model = Activity
#         fields = ["activity_name", "date_time_start", "date_time_finish", "record_description"]
