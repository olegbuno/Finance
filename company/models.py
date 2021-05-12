from django.db import models

# Create your models here.
class Cldr(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLDR'
        verbose_name_plural = "CLDR"


class Docu(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DOCU'
        verbose_name_plural = "DOCU"


class Pd(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PD'
        verbose_name_plural = "PD"


class Pins(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PINS'
        verbose_name_plural = "PINS"


class Run(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'RUN'
        verbose_name_plural = "RUN"


class Zm(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ZM'
        verbose_name_plural = "ZM"


class Zuo(models.Model):
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    open = models.TextField(db_column='Open', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high = models.TextField(db_column='High', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low = models.TextField(db_column='Low', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    close = models.TextField(db_column='Close', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adjclose = models.TextField(db_column='AdjClose', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ZUO'
        verbose_name_plural = "ZUO"
