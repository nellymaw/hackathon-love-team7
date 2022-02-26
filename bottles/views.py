from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Letter
from .forms import ReplyForm


class LetterList(generic.ListView):
    """
    docstring
    """
    model = Letter
    queryset = Letter.objects.order_by("-created_on")
    template_name = "home/landing.html"


class LetterDetail(View):
    """
    A view to show 5 lastest letters ordered by created
    Args:
        ListView: class based view
    Returns:
        Render of home page with context
    """
    def get(self, request, slug):
        """
        doc string
        """
        queryset = Letter.objects
        letter = get_object_or_404(queryset, slug=slug)
        replys = letter.replys.order_by("-created_on")  # oldest first
        return render(
            request,
            "home/landing_detail.html",
            {
                "letter": letter,
                "replys": replys,
                "reply_form": ReplyForm(),

            },
        )

    def post(self, request, slug):
        """
        doc string
        """
        queryset = Letter.objects
        letter = get_object_or_404(queryset, slug=slug)
        replys = letter.replys.order_by("-created_on")  # oldest first
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            reply_form.instance.name = request.user.username
            reply = reply_form.save(commit=False)
            reply.letter = letter
            reply.save()
        else:
            reply_form = ReplyForm()
        return render(
            request, "home/landing_detail.html",
            {
                "letter": letter,
                "replys": replys,
                "reply_form": ReplyForm(),
                },
        )
