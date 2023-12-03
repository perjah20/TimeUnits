from __future__ import annotations

from typing import TypeVar, Generic, Union

T = TypeVar('T', bound='BaseClass')


class TimeUnit(Generic[T]):
    def __init__(self, value: float):
        self.__verify_value(value)
        self.__value = value

    @property
    def value(self) -> float:
        return self.__value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __add__(self, value: Union[int, float]) -> T:
        self.__verify_value(value)
        return type(self)(self.value + value)

    def __mul__(self, value: Union[int, float]) -> T:
        self.__verify_value(value)
        return type(self)(self.value * value)

    def __sub__(self, value: Union[int, float]) -> T:
        self.__verify_value(value)
        temp_value = self.value - value
        if temp_value < 0:
            raise ValueError("Time value cannot be negative")
        return type(self)(temp_value)

    def __truediv__(self, value: Union[int, float]) -> T:
        self.__verify_value(value)
        if value == 0:
            raise ZeroDivisionError("Time cannot be divided by zero")
        return type(self)(self.value / value)

    def __copy__(self) -> T:
        return type(self)(self.value)

    def __verify_value(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Unsupported operand type for Time")
        if value < 0:
            raise ValueError("Time value cannot be negative")


class s(TimeUnit['S']):
    def to_qs(self) -> QS:
        """ Convert to quasiseconds """
        return QS(self.value * 1e30)

    def to_rs(self) -> RS:
        """ Convert to rontoseconds """
        return RS(self.value * 1e27)

    def to_ys(self) -> YS:
        """ Convert to yoctoseconds """
        return YS(self.value * 1e24)

    def to_zs(self) -> ZS:
        """ Convert to zeptoseconds """
        return ZS(self.value * 1e21)

    def to_as(self) -> AS:
        """ Convert to attoseconds """
        return AS(self.value * 1e18)

    def to_fs(self) -> FS:
        """ Convert to femtoseconds """
        return FS(self.value * 1e15)

    def to_ps(self) -> PS:
        """ Convert to picoseconds """
        return PS(self.value * 1e12)

    def to_ns(self) -> NS:
        """ Convert to nanoseconds """
        return NS(self.value * 1e9)

    def to_us(self) -> US:
        """ Convert to microseconds """
        return US(self.value * 1e6)

    def to_ms(self) -> MS:
        """ Convert to milliseconds """
        return MS(self.value * 1e3)

    def to_ds(self) -> DS:
        """ Convert to deciseconds """
        return DS(self.value * 1e2)

    def to_cs(self) -> CS:
        """ Convert to centiseconds """
        return CS(self.value * 1e1)

    def to_das(self) -> DAS:
        """ Convert to decaseconds """
        return DAS(self.value * 1e-1)

    def to_hs(self) -> HS:
        """ Convert to hectoseconds """
        return HS(self.value * 1e-2)

    def to_ks(self) -> KS:
        """ Convert to kiloseconds """
        return KS(self.value * 1e-3)

    def to_Ms(self) -> MS:
        """ Convert to megaseconds """
        return MS(self.value * 1e-6)



class DS(TimeUnit['DS']):
    pass


class CS(TimeUnit['CS']):
    pass


class MS(TimeUnit['MS']):
    pass


class US(TimeUnit['US']):
    pass


class NS(TimeUnit['NS']):
    pass


class PS(TimeUnit['PS']):
    pass


class FS(TimeUnit['FS']):
    pass


class AS(TimeUnit['AS']):
    pass


class ZS(TimeUnit['ZS']):
    pass


class YS(TimeUnit['YS']):
    pass


class RS(TimeUnit['RS']):
    pass


class QS(TimeUnit['QS']):
    pass
