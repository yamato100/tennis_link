from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル

    usernameを使わず、emailアドレスをユーザー名として使うようにしています。

    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    user_name = models.CharField(_('ユーザ名'), max_length=150, blank=True)
    user_introduction = models.TextField(_('自己紹介'), blank=True)
    SEX_CHOICES = (
        (10, '男性'),
        (20, '女性'),
    )
    user_sex = models.IntegerField(_('性別'),choices=SEX_CHOICES, blank=True, null=True)
    AGE_CHOICES = (
        (10, '10代'),
        (20, '20代'),
        (30, '30代'),
        (40, '40代'),
        (30, '50代'),
        (60, '60代～'),
    )
    user_age = models.IntegerField(_('年齢'), choices=AGE_CHOICES, blank=True, null=True)
    LEVEL_CHOICES = (
        (10, '1.0'),
        (20, '1.5'),
        (30, '2.0'),
        (40, '2.5'),
        (50, '3.0'),
        (60, '3.5'),
        (70, '4.0'),
        (80, '4.5'),
        (90, '5.0'),
        (100, '5.5'),
        (100, '6.0'),
    )
    user_level = models.IntegerField(_('レベル(NTRP)'), choices=LEVEL_CHOICES, blank=True, null=True)    

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email
