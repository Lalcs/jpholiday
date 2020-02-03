# -*- coding: utf-8 -*-

class RegistryHolder(type):
    _REGISTRY = []

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)

        cls.register(new_cls)

        return new_cls

    @classmethod
    def get_registry(cls):
        return list(cls._REGISTRY)

    @classmethod
    def register(cls, register_class):
        instance = register_class()
        cls._REGISTRY.append(instance)

    @classmethod
    def unregister(cls, register_class):
        for registered_class in cls._REGISTRY:
            if type(registered_class) != register_class:
                continue

            cls._REGISTRY.remove(registered_class)
            break

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

class OriginalHoliday(metaclass=RegistryHolder):

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