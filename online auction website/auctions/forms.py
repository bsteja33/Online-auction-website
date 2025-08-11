from django.forms import ModelForm
from django import forms
from .models import Auction, Bid, Comment

class NewListingForm(ModelForm):
    # specify the model to use
    class Meta:
        model = Auction
        fields = ["title", "description", "starting_bid", "category", "imageURL"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter the title of your auction list",
                "class": "form-control"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Enter the description...",
                "class": "form-control",
                "rows": 15
            }),
            "starting_bid": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0.01",
                "step": "0.01"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "imageURL": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the image URL"
            })
        }

class NewBidForm(ModelForm):
    # specify the model to use
    class Meta:
        model = Bid
        fields = ["bid_price"]
        widgets = {
            "bid_price": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0.01",
                "step": "0.01"
            })
        }

class NewCommentForm(ModelForm):
    # specify the model to use
    class Meta:
        model = Comment
        fields = ["headline", "message"]
        widgets = {
            "headline": forms.TextInput(attrs={
                "placeholder": "Enter headline",
                "class": "form-control"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Enter your comment...",
                "class": "form-control",
                "rows": 4
            })
        }
