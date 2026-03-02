from django.contrib import admin
from .models import Order

admin.site.register(Order)



from .models import ContactMessage

admin.site.register(ContactMessage)

from .models import Feedback

admin.site.register(Feedback)
