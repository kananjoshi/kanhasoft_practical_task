from django.db import models
from django.utils.translation import ugettext as _

class Category(models.Model):
    CATEGORY_TYPES = (
        ("e", "Electronic"),
        ("s", "Sculpture"),
        ("t", "Toys"),
        ("f", "Furniture"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(_("Category Name"), max_length=50, blank=True, null=True)
    type = models.CharField(_("Category Type"), max_length = 20,
                            choices = CATEGORY_TYPES, default = '1')
    image = models.ImageField(upload_to='images/',blank=True, null=True)

    def __str__(self):
        return "[CATEGORY] {} [TYPE]".format(self.name,self.type)

class Subcategory(models.Model):
    class Meta:
        verbose_name = _("Sub - Category")
        verbose_name_plural = _("Sub - Categories")

    category = models.ForeignKey(Category, related_name=_("subcategory"), on_delete=models.CASCADE)
    name = models.CharField(_("Sub-Category Name"), max_length=50, blank=True, null=True)
    desc = models.CharField(_("Description"), max_length=255, blank=True, null=True)

    def __str__(self):
        return "[SUBCATEGORY]".format(self.name)