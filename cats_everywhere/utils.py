from django.utils.text import slugify

def unique_slug_generator(instance, instance_attribute, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        string = getattr(instance, instance_attribute)
        slug = slugify(string)
    Klass = instance.__class__
    queryset = Klass.objects.filter(type = slug).exclude(id = instance.id)
     
    if queryset.exists():
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size = 4))
             
        return unique_slug_generator(instance, instance_attribute, new_slug = new_slug)
    return slug