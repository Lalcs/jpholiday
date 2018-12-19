# -*- coding: utf-8 -*-
import datetime


class RegistryHolder(type):
    _REGISTRY = []
    _REGISTRY_EXTRA = []

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)

        instance = new_cls()

        if instance._IS_REGISTER == False:
            return new_cls

        cls._REGISTRY.append(instance)

        return new_cls

    @classmethod
    def get_registry(cls):
        return list(cls._REGISTRY)

class BaseHoliday(metaclass=RegistryHolder):
    _HOLIDAY_NAME = ''
    _IS_REGISTER = False

    def __init__(self):
        if self._HOLIDAY_NAME != '':
            self._IS_REGISTER = True

    def is_holiday(self, date):
        if self._check_holiday(date):
            return True
        else:
            return False

    def is_holiday_name(self, date):
        if self._check_holiday(date):
            return self._HOLIDAY_NAME
        else:
            return None

    def _check_holiday(self, date):
        return False
