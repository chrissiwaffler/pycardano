"""Transaction witness."""

from dataclasses import dataclass, field
from typing import Any, List

from pycardano.key import VerificationKey
from pycardano.nativescript import NativeScript
from pycardano.plutus import PlutusData, Redeemer
from pycardano.serialization import (
    ArrayCBORSerializable,
    MapCBORSerializable,
    list_hook,
)

__all__ = ["VerificationKeyWitness", "TransactionWitnessSet"]


@dataclass(repr=False)
class VerificationKeyWitness(ArrayCBORSerializable):
    vkey: VerificationKey
    signature: bytes


@dataclass(repr=False)
class TransactionWitnessSet(MapCBORSerializable):
    vkey_witnesses: List[VerificationKeyWitness] = field(
        default=None,
        metadata={
            "optional": True,
            "key": 0,
            "object_hook": list_hook(VerificationKeyWitness),
        },
    )

    native_scripts: List[NativeScript] = field(
        default=None,
        metadata={"optional": True, "key": 1, "object_hook": list_hook(NativeScript)},
    )

    # TODO: Add bootstrap witness (byron) support
    bootstrap_witness: List[Any] = field(
        default=None, metadata={"optional": True, "key": 2}
    )

    plutus_script: List[bytes] = field(
        default=None, metadata={"optional": True, "key": 3}
    )

    plutus_data: List[PlutusData] = field(
        default=None,
        metadata={"optional": True, "key": 4, "object_hook": list_hook(PlutusData)},
    )

    redeemer: List[Redeemer] = field(
        default=None,
        metadata={"optional": True, "key": 5, "object_hook": list_hook(Redeemer)},
    )
