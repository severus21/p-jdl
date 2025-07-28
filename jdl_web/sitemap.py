from django.urls import reverse

from django.contrib import sitemaps

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    namespace = 'projects'

    def items(self):
        return list( map( lambda x : "%s:%s" % (self.namespace, x), 
            ['index', 'TIPE_3/2', 'TIPE_5/2_c', 'TIPE_5/2_python'] 
        ))

    def location(self, item):
        return reverse(item)
