from django.shortcuts import render
from testapp.forms import QRCodeForm
import qrcode
import os
from django.conf import settings

# pip install qrcode
# pip install pillow



# HOME PAGE
def index(request):
    return render(request,'testapp/index.html')


# QR SCREEN
def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) #../media/rathan_rest_menu.png
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            qr.save(file_path)

            # Create Image URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request, 'testapp/qr_result.html', context)
    
    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'testapp/generate_qr_code.html', context)