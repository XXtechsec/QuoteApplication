from django import forms


class QuoteForm(forms.Form):

    Length = forms.IntegerField()
    Breadth = forms.IntegerField()
    Height= forms.IntegerField()
