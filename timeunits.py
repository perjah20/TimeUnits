from __future__ import annotations

from abc import ABC
from typing import TypeVar, Generic, Union, Type

T = TypeVar("T", bound="TimeUnit")


class TimeUnit(ABC, Generic[T]):
    """
    Represents a unit of time with conversions between different orders of
    magnitude. This class is inspired by the concept of time units as
    described in 'Orders of Magnitude (Time)'
    (https://en.wikipedia.org/wiki/Orders_of_magnitude_(time)).
    The purpose is to provide a clear and straightforward way for developers to
    work with time units without needing to write comments to specify the units.

    The class includes methods to convert between various time units like
    seconds, milliseconds, microseconds, etc., providing a versatile tool for
    time-related calculations.

    Example usage with doctests:
    >>> time_unit = Sec(1)  # 1 second
    >>> time_unit.to_milli()
    MilliSec(1000.0)
    >>> time_unit.to_micro()
    MicroSec(1000000.0)
    >>> time_unit.to_nano()
    NanoSec(1000000000.0)
    >>> time.sleep(time_unit.v)  # sleep for 1 second
    >>> time.sleep((float)time_unit)  # sleep for 1 second
    >>> time.sleep(int(time_unit))  # sleep for 1 second

    :param value: The numerical value of the time unit.
    """

    def __init__(self, value: float):
        self.__verify_value(value)
        self.__value: float = float(value)

    def to_quecto(self) -> QuectoSec:
        """Convert to  Quectoseconds"""
        return QuectoSec(self.__convert(target_class=QuectoSec))

    def to_ronto(self) -> RontoSec:
        """Convert to Rontoseconds"""
        return RontoSec(self.__convert(target_class=RontoSec))

    def to_yocto(self) -> YoctoSec:
        """Convert to Yoctoseconds"""
        return YoctoSec(self.__convert(target_class=YoctoSec))

    def to_zepto(self) -> ZeptoSec:
        """Convert to Zeptoseconds"""
        return ZeptoSec(self.__convert(target_class=ZeptoSec))

    def to_atto(self) -> AttoSec:
        """Convert to ttoseconds"""
        return AttoSec(self.__convert(target_class=AttoSec))

    def to_femto(self) -> FemtoSec:
        """Convert to Femtoseconds"""
        return FemtoSec(self.__convert(target_class=FemtoSec))

    def to_pico(self) -> PicoSec:
        """Convert to icoseconds"""
        return PicoSec(self.__convert(target_class=PicoSec))

    def to_nano(self) -> NanoSec:
        """Convert to anoseconds"""
        return NanoSec(self.__convert(target_class=NanoSec))

    def to_micro(self) -> MicroSec:
        """Convert to Microseconds"""
        return MicroSec(self.__convert(target_class=MicroSec))

    def to_milli(self) -> MilliSec:
        """Convert to Milliseconds"""
        return MilliSec(self.__convert(target_class=MilliSec))

    def to_sec(self) -> Sec:
        return Sec(self.__convert(target_class=Sec))

    def to_centi(self) -> CentiSec:
        """Convert to Centiseconds"""
        return CentiSec(self.__convert(target_class=CentiSec))

    def to_deci(self) -> DeciSec:
        """Convert to eciseconds"""
        return DeciSec(self.__convert(target_class=DeciSec))

    def to_deca(self) -> DecaSec:
        """Convert to ecaseconds"""
        return DecaSec(self.__convert(target_class=DecaSec))

    def to_hecto(self) -> HectoSec:
        """Convert to Hectoseconds"""
        return HectoSec(self.__convert(target_class=HectoSec))

    def to_kilo(self) -> KiloSec:
        """Convert to iloseconds"""
        return KiloSec(self.__convert(target_class=KiloSec))

    def to_mega(self) -> MegaSec:
        """Convert to egaseconds"""
        return MegaSec(self.__convert(target_class=MegaSec))

    def to_giga(self) -> GigaSec:
        """Convert to igaseconds"""
        return GigaSec(self.__convert(target_class=GigaSec))

    def to_tera(self) -> TeraSec:
        """Convert to eraseconds"""
        return TeraSec(self.__convert(target_class=TeraSec))

    def to_peta(self) -> PetaSec:
        """Convert to etaseconds"""
        return PetaSec(self.__convert(target_class=PetaSec))

    def to_exa(self) -> ExaSec:
        """Convert to aseconds"""
        return ExaSec(self.__convert(target_class=ExaSec))

    def to_zetta(self) -> ZettaSec:
        """Convert to Zettaseconds"""
        return ZettaSec(self.__convert(target_class=ZettaSec))

    def to_yotta(self) -> YottaSec:
        """Convert to Yottaseconds"""
        return YottaSec(self.__convert(target_class=YottaSec))

    def to_ronna(self) -> RonnaSec:
        """Convert to Ronnaseconds"""
        return RonnaSec(self.__convert(target_class=RonnaSec))

    def to_quetta(self) -> QuettaSec:
        """Convert to  Quettaseconds"""
        return QuettaSec(self.__convert(target_class=QuettaSec))

    @property
    def v(self) -> float:
        return self.__value

    @v.setter
    def v(self, value: float) -> None:
        self.__verify_value(value)
        self.__value = float(value)

    @property
    def unit(self) -> str:
        """ Subclasses should define their own unit as a string
        I.e Sec class = 's' """
        raise NotImplementedError

    @staticmethod
    def multiple_of_a_second() -> int:
        """Subclasses should define their own multiple of a second."""
        raise NotImplementedError

    def __convert(self, target_class: Type[TimeUnit]) -> float:
        offset_difference = (
            self.multiple_of_a_second() - target_class.multiple_of_a_second()
        )
        conversion_factor = 10 ** offset_difference
        converted_value = self.v * conversion_factor
        return converted_value

    def __str__(self):
        return f"{self.v} {self.unit}"

    def __repr__(self):
        return self.v

    def __int__(self):
        return int(self.v)

    def __float__(self):
        return float(self.v)

    def __add__(self, value: Union[int, float, T]) -> T:
        self.__verify_value_for_math(value)
        return type(self)(self.v + float(value))

    def __mul__(self, value: Union[int, float, T]) -> T:
        self.__verify_value(value)
        return type(self)(self.v * float(value))

    def __sub__(self, value: Union[int, float, T]) -> T:
        self.__verify_value_for_math(value)
        temp_value = self.v - float(value)
        if temp_value < 0:
            raise ValueError("Time value cannot be negative")
        return type(self)(temp_value)

    def __truediv__(self, value: Union[int, float, T]) -> T:
        self.__verify_value(value)
        if value == 0:
            raise ZeroDivisionError("Time cannot be divided by zero")
        return type(self)(self.v / value)

    def __copy__(self) -> T:
        return type(self)(self.v)

    def __verify_value(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Unsupported operand type for Time")
        if value < 0:
            raise ValueError("Time value cannot be negative")

    def __verify_value_for_math(self, value: Union[int, float, T]) -> None:
        if not isinstance(value, type(self)):
            raise TypeError(f"Cant perform operation between {type(self)} "
                            f"and {type(value)}")
        self.__verify_value(value.v)


class Sec(TimeUnit["Sec"]):
    @staticmethod
    def multiple_of_a_second() -> float:
        return 0

    @property
    def unit(self) -> str:
        return "s"


class QuectoSec(TimeUnit["QuectoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -30

    @property
    def unit(self) -> str:
        return "qs"


class RontoSec(TimeUnit["RontoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -27

    @property
    def unit(self) -> str:
        return "rs"


class YoctoSec(TimeUnit["YoctoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -24

    @property
    def unit(self) -> str:
        return "ys"


class ZeptoSec(TimeUnit["ZeptoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -21

    @property
    def unit(self) -> str:
        return "zs"


class AttoSec(TimeUnit["AttoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -18

    @property
    def unit(self) -> str:
        return "as"


class FemtoSec(TimeUnit["FemtoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -15

    @property
    def unit(self) -> str:
        return "fs"


class PicoSec(TimeUnit["PicoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -12

    @property
    def unit(self) -> str:
        return "ps"


class NanoSec(TimeUnit["NanoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -9

    @property
    def unit(self) -> str:
        return "ns"


class MicroSec(TimeUnit["MicroSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -6

    @property
    def unit(self) -> str:
        return "µs"


class MilliSec(TimeUnit["MilliSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -3

    @property
    def unit(self) -> str:
        return "ms"


class CentiSec(TimeUnit["CentiSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -2

    @property
    def unit(self) -> str:
        return "cs"


class DeciSec(TimeUnit["DeciSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return -1

    @property
    def unit(self) -> str:
        return "ds"


class DecaSec(TimeUnit["DecaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 1

    @property
    def unit(self) -> str:
        return "das"


class HectoSec(TimeUnit["HectoSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 2

    @property
    def unit(self) -> str:
        return "hs"


class KiloSec(TimeUnit["KiloSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 3

    @property
    def unit(self) -> str:
        return "ks"


class MegaSec(TimeUnit["MegaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 6

    @property
    def unit(self) -> str:
        return "Ms"


class GigaSec(TimeUnit["GigaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 9

    @property
    def unit(self) -> str:
        return "Gs"


class TeraSec(TimeUnit["TeraSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 12

    @property
    def unit(self) -> str:
        return "Ts"


class PetaSec(TimeUnit["PetaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 15

    @property
    def unit(self) -> str:
        return "Ps"


class ExaSec(TimeUnit["ExaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 18

    @property
    def unit(self) -> str:
        return "Es"


class ZettaSec(TimeUnit["ZettaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 21

    @property
    def unit(self) -> str:
        return "Zs"


class YottaSec(TimeUnit["YottaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 24

    @property
    def unit(self) -> str:
        return "Ys"


class RonnaSec(TimeUnit["RonnaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 27


class QuettaSec(TimeUnit["QuettaSec"]):
    @staticmethod
    def multiple_of_a_second() -> int:
        return 30

    @property
    def unit(self) -> str:
        return "Qs"
