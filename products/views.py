from django.shortcuts import render

def productsDetails(request):
    return render(request, 'products_detail_page.html')  