from django.db import models

ENVRONMENT_TYPES = (
    ('py',  'Python'),
    ('php', 'PHP'),
    ('rr',  'Ruby'),
)
class Infrastructure(models.Model):
	name        = models.CharField(max_length=32)
	description = models.TextField(blank=True)
	location    = models.CharField(max_length=256, blank=True)
	
class Product(models.Model):
	name        = models.CharField(max_length=32)
	service     = models.CharField(max_length=32)
	description = models.TextField(blank=True)

class ConcreteProduct(Product):
	pass

class Server(models.Model):
	name        = models.CharField(max_length=32)
	hostname    = models.CharField(max_length=32)
	ipaddress   = models.CharField(max_length=32)
	is_virt     = models.BooleanField(default=False)
	description = models.TextField(blank=True)
	
class Entity(models.Model):
	name       = models.CharField(max_length=32)
	host       = models.ForeignKey('Server')
	produces   = models.ManyToManyField(ConcreteProduct, db_table="producesa", related_name="producedby")
	consumes   = models.ManyToManyField(ConcreteProduct, db_table="consumesa", related_name="consumedby")

class Domain(models.Model):
	dns      = models.CharField(max_length=256)
	provider = models.CharField(max_length=32)
	
class EnvironmentApp(models.Model):
	application = models.CharField(max_length=32)
	version     = models.CharField(max_length=32)
	
class Environment(models.Model):
	envtype      = models.CharField(max_length=32, choices=ENVRONMENT_TYPES)
	version      = models.CharField(max_length=32)
	applications = models.ManyToManyField(EnvironmentApp)
	
class Website(models.Model):
	sitename          = models.CharField(max_length=64)
	domain            = models.ForeignKey('Domain')
	siteprovider      = models.ForeignKey('Entity',related_name="providedassiteto")
	databaseprovider  = models.ForeignKey('Entity',related_name="providedasdatabaseto")
	datastoreprovider = models.ForeignKey('Entity',related_name="providedasdatastoreto")
	environment       = models.ForeignKey('Environment')
	
	

