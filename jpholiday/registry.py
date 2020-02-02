# -*- coding: utf-8 -*-

class RegistryHolder(type):
    _REGISTRY = []

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)

        instance = new_cls()

        cls._REGISTRY.append(instance)

        return new_cls

    @classmethod
    def get_registry(cls):
        return list(cls._REGISTRY)


class BaseHoliday(metaclass=RegistryHolder):

    def is_holiday(self, date):
        if self._is_holiday(date):
            return True
        else:
            return False

    def is_holiday_name(self, date):
        if self._is_holiday(date):
            return self._is_holiday_name(date)
        else:
            return None

    def _is_holiday(self, date):
        pass

    def _is_holiday_name(self, date):
        pass
