from django.db import models
import uuid

# To Understand the Relation Check the image.jpeg file in the Root + docs Directory of the project
# sterven4/docs/image.jpeg


class type_of_server(models.Model):
    type_server_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    server_type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    class Meta:
        ordering = ["type_server_id"]
        verbose_name_plural = "types_of_server"

    def __str__(self):
        return self.server_type

class server(models.Model):
    server_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=45)
    type_of_server = models.ForeignKey(type_of_server, on_delete=models.CASCADE)
    processor_number = models.CharField(max_length=45, blank=False)
    memory_capacity = models.CharField(max_length=45)
    storage_capacity = models.CharField(max_length=45)
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Servers"

    def __str__(self):
        return self.name

class application(models.Model):
    app_id = models.UUIDField(default=uuid.uuid4, unique=True, blank=False, primary_key=False, editable=False)
    name_app = models.CharField(max_length=45)
    logo_app = models.ImageField(null = True, blank = True)
    server = models.ForeignKey(server, on_delete=models.CASCADE)
    user = models.ForeignKey("user", on_delete=models.CASCADE)
    class Meta:
        ordering = ["name_app"]
        verbose_name_plural = "Apps"

    def __str__(self):
        return self.name_app

class user(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_name = models.CharField(max_length=45)
    sur_name = models.CharField(max_length=45)
    email = models.EmailField()
    class Meta:
        ordering = ["user_id"]
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_name

class services(models.Model):
    service_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name_of_service = models.CharField(max_length=45)
    date_of_launch = models.DateField()
    memory_used = models.CharField(max_length=45)
    ram_memory = models.CharField(max_length=45)
    service_launched_onto = models.ForeignKey(server, on_delete=models.CASCADE)
    class Meta:
        ordering = ["service_id"]
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name_of_service

class applicaitonshasservices(models.Model):
    app_id = models.ForeignKey(application, blank = False, on_delete=models.CASCADE)
    services_id = models.ForeignKey(services, blank = False, on_delete=models.CASCADE)
    class Meta:
        ordering = ["app_id"]
        verbose_name_plural = "AppsHasService"
    def __int__(self):
        return self.app_id

class overall(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    number_of_server_used = models.IntegerField()
    total_storage_used = models.IntegerField()
    class Meta:
        ordering = ["number_of_server_used"]
        verbose_name_plural = "Overall"
    
