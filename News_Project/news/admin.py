from django.contrib import admin

from .models import *

#Home Admin
admin.site.register(Post)
admin.site.register(Latest_Post)
admin.site.register(Recent_Post)

# It Admin

admin.site.register(It_Post)
admin.site.register(It_Latest_Post)
admin.site.register(It_Recent_Post)
admin.site.register(It_Trending_Post)

# Business Admin

admin.site.register(Business_Post)
admin.site.register(Business_Latest_Post)
admin.site.register(Business_Recent_Post)
admin.site.register(Business_Trending_Post)

# Sport Admin

admin.site.register(Sport_Post)
admin.site.register(Sport_Latest_Post)
admin.site.register(Sport_Recent_Post)
admin.site.register(Sport_Trending_Post)

# Travel Admin

admin.site.register(Travel_Post)
admin.site.register(Travel_Latest_Post)
admin.site.register(Travel_Recent_Post)
admin.site.register(Travel_Trending_Post)


# Comment Admin
admin.site.register(Comment)

admin.site.register(TravelComment)

admin.site.register(BusinessComment)

admin.site.register(SportComment)

admin.site.register(ItComment)


# Tags
admin.site.register(Tag)