from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)    # input cannot exeed 100 characters
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)   # gives a textbox area to type
    
    def send_email(self):
        print(f"Sending email from {self.cleaned_data ['email']} with message: {self.cleaned_data ['message']}")

    