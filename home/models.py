from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

from geolocation.models import *

# Create your models here.
status = (("Draft", "Draft"),("Schedule", "Schedule"),("Active", "Active"),("Inactive", "Inactive"),("Delete", "Delete"))
gender = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),)

class User(AbstractUser):
	email = models.EmailField(blank=False, unique=True)
	mobile = models.PositiveIntegerField(unique=True)
	phone = models.CharField(verbose_name="Alternate mobile", max_length=10, blank=True)
	gender = models.CharField(max_length=6, choices=gender, default='Male')
	dob = models.DateField(null=True, blank=True)
	about = models.TextField(blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	@property
	def full_name(self):
		"Returns the person's full name."
		if self.first_name and self.last_name:
			return '%s %s' % (self.first_name, self.last_name)
		return self.username

	REQUIRED_FIELDS = ['email', 'mobile']

	class Meta:
		verbose_name_plural = "01. Users"

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' (' + str(self.username) + ')'

class Skill(models.Model):
	title = models.CharField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "02. Skills"

	def __str__(self):
		return str(self.title)

class Tag(models.Model):
	title = models.CharField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "03. Tags"

	def __str__(self):
		return str(self.title)

class Job(models.Model):
	designations = (
			('backend developer', 'backend developer'),
			('frontend developer', 'frontend developer'),
			('devops engineer', 'devops engineer'),
			('content writer', 'content writer'),
			('back office', 'back office'),
			('chartered accountant', 'chartered accountant'),
			('other', 'other'),
		)
	types = (
			('onsite', 'onsite'),
			('remote', 'remote'),
			('hybrid', 'hybrid'),
		)
	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='auhtor_job')
	city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True, related_name='location')
	skills = models.ManyToManyField(Skill)
	tags = models.ManyToManyField(Tag, blank=True)
	title = models.CharField(max_length=160)
	designation = models.CharField(max_length=20, choices=designations)
	type = models.CharField(max_length=20, choices=types)
	min_experiance = models.FloatField()
	max_experiance = models.FloatField()
	min_salary = models.FloatField()
	max_salary = models.FloatField()
	desc = RichTextUploadingField()
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "04. Job"

	def save(self, *args, **kwargs):
		if self.type == 'onsite' or self.type == 'hybrid':
			if not self.city:
				raise ValidationError({"ValidationError":"City is mandatory field for this type of job"})
		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.title)

class Applicant(models.Model):
	job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='job_applicant')
	city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city_of_applicant')
	fname = models.CharField('First Name', max_length=160)
	lname = models.CharField('Last Name', max_length=160, null=True, blank=True)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	designation = models.CharField('Current Designation', max_length=160)
	experiance = models.FloatField('Relavant experiance')
	experiance2 = models.FloatField('Total experiance')
	resume = models.FileField(upload_to='applicant/resume/')
	about = models.TextField()
	cctc = models.FloatField('Current CTC')
	ectc = models.FloatField('Expected CTC')
	ccompany = models.CharField('Current Company', max_length=160, null=True, blank=True)
	address = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	utimestamp = models.DateTimeField(auto_now=True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=20, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "05. Applicants"

	def __str__(self):
		return str(self.fname)

