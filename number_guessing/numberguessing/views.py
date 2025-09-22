from django.shortcuts import render
import random

def play(request):
    number = random.randint(1, 100)
    message = None

    if request.method == "POST":
        guess = int(request.POST.get("guess"))
        if guess == number:
            message = "🎉 Correct! You guessed it!"
        elif guess < number:
            message = "Too low! Try again."
        else:
            message = "Too high! Try again."

    return render(request, "game/play.html", {"message": message})
