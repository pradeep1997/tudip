from django.db import models

# Create your models here.

status = (("Active","Active"), ("Inactive","Inactive"), ("Delete","Delete"))

class Country(models.Model):
	name = models.CharField(max_length=50)
	local = models.CharField(max_length=50)
	code = models.IntegerField()
	code2 = models.CharField(max_length=2, null=True, blank=True)
	code3 = models.CharField(max_length=3, null=True, blank=True)
	capital = models.CharField(max_length=50)
	gdp = models.BigIntegerField()
	area = models.BigIntegerField()
	population = models.BigIntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "1.Countries"

	def __str__(self):
		return self.name

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.PROTECT)
	name = models.CharField(max_length=50)
	local = models.CharField(max_length=50)
	capital = models.CharField(max_length=50)
	area = models.BigIntegerField()
	population = models.BigIntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "2.States"

	def __str__(self):
		return str(self.country.name)+" | "+str(self.name)

class City(models.Model):
	state = models.ForeignKey(State, on_delete=models.PROTECT)
	name = models.CharField(max_length=50)
	local = models.CharField(max_length=50)
	area = models.BigIntegerField()
	population = models.BigIntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "3.Cities"

	def __str__(self):
		return str(self.state.name)+" | "+str(self.name)

		
