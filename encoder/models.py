
from django.db import models





class Url(models.Model):
    def converter(self):
        base62tuple=tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        prevdata=Url.objects.all()
        N=len(prevdata)
        num=prevdata[N-1].id
        temp=oct(num)
        temp=temp[::-1]
        num=int(temp[:-2])

        self.shorturls=''
        while num>0:
            self.shorturls+=base62tuple[num%62]
            num=num//62

        return self.shorturls

    id=models.AutoField(primary_key=True)
    longurl=models.CharField()
    shorturl=models.CharField(blank=True)

    def save(self, *args, **kwargs):
        if not self.shorturl:
            self.shorturl = self.converter()  # Generate shortened URL if it is not already set
        super().save(*args, **kwargs)  # Call the parent class's save method



    def __str__(self):
        return f"ID: {self.id} ,, Longurl: {self.longurl} ,, Shorturl: {self.shorturl}"

