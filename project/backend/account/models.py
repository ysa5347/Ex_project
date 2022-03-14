
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, userID, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not userID:
            raise ValueError('The given ID must be set')
        email = self.normalize_email(email)
        user = self.model(
            userID=userID,
            email=email,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, userID, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(userID, email, password, **extra_fields)

    def create_superuser(self, userID, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(userID, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin): #AbstractBaseUser에 password columm이 이미 있음
    userID = models.CharField(
        max_length=15,
        unique=True,
        help_text='user ID'
        )
    phone = models.CharField( #휴대폰 인증 서비스 등록 필
        max_length=11,
        help_text='phone number'
        )
    email = models.CharField( #이메일 인증 서비스 등록 필
        max_length=100,
        unique=True,
        help_text='Email'
        )
    birth = models.PositiveSmallIntegerField(null=True, blank=True) 
    penalty = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=40) 
    lab = models.CharField(max_length=40, blank=True) #추가정보
    
    isExp = models.BooleanField(
        _('post permition request status'),
        default=False,
        help_text=_('Designates whether this user should be registrated on post permition waiting list.')
        )
    isPermit = models.BooleanField(
        _('post permition status'),
        default=False,
        help_text=_('Designates whether this user should be treated as post writer')
        )
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    dateJoined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'userID'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.userID}'

    def get_short_name(self):
        return self.userID
# Create your models here.
