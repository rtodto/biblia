from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    ENABLED_DISABLED_CHOICE = [
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
    ]
    VALUE_CHOICES = [(i, i) for i in range(1, 11)] 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_books', on_delete=models.CASCADE)
    temp_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='borrowed_books', on_delete=models.SET_NULL, null=True, blank=True) 
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=30)
    is_read = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='no', verbose_name="Finished")
    summary = models.TextField(default='No summary')
    original_title = models.CharField(max_length=250)
    language = models.CharField(max_length=50)
    original_language = models.CharField(max_length=50)
    published_year = models.DateField
    rating = models.IntegerField(
        choices=VALUE_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default='5')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    wish_list = models.CharField(max_length=9, 
                                 choices=ENABLED_DISABLED_CHOICE, 
                                 default='disabled',
                                 help_text="If enabled, it puts the book in wish list i.e book isn't purchased yet") 
    
    entry_created_date = models.DateTimeField(default=timezone.now)
    entry_published_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author','title'], name='unique_book_author')
        ]


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title