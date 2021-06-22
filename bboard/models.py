from django.db import models

# Create your models here.

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Rubrikalar'
        verbose_name = 'Rubrika'
        ordering = ['name']
    def __str__(self):
        return self.name
        
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='elon')
    content = models.TextField(null=True,blank=True,verbose_name='mazmuni')
    price = models.FloatField(null=True,blank=True,verbose_name='narx')
    published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='chop qilingan sana')
    rubric = models.ForeignKey(Rubric,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "E'lonlar"
        verbose_name = "E'lon"
        ordering = ['-published']
    
    def __str__(self):
        return self.title

    """
    CREATE TABLE "bboard_bb"(
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "title" varchar(50) NOT NULL,
        "content" text NULL,
        "price" real NULL,
        "published" datetime NOT NULL,
    );
    CREATE INDEX "bboard_bb_published_58fde1db5" ON "bboar_bb"("published");
    COMMIT;
    
    """

