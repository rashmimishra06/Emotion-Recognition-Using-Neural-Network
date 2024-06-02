from .models import Inputemo

def delete_info():
    Inputemo.objects.all().delete()