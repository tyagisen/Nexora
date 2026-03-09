from django.utils.text import slugify

def generate_unique_slug(model, name):
    slug = slugify(name)
    unique_slug = slug
    counter = 1

    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{counter}"
        counter+=1
    return unique_slug
