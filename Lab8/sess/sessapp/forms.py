from django import forms

class FirstPage(forms.Form):
    name = forms.CharField(max_length=100,label='Name')
    roll = forms.CharField(max_length=100,label='Roll')
    
    subjects = [
        ('math', 'Mathematics'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('history', 'History'),
        ('geography', 'Geography'),
        ('english', 'English'),
    ]
    
    subject = forms.ChoiceField(choices=subjects,label="Select Subjects")