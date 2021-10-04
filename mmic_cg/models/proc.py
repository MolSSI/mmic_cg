""" Populate this file if your component requires its own models """

from cmselemental.models import InputProc, OutputProc
from mmelemental.models import Molecule
from pydantic import Field
from typing import Union, Optional, Dict, List, Any

__all__ = ["InputCoarse", "OutputCoarse"]


class InputCoarse(InputProc):
    """An input model for coarse-graining."""

    molecule: Union[Molecule, List[Molecule]] = Field(
        ..., description="A single or list of molecule objects to coarse-grain."
    )
    method: str = Field(..., description="The name of the coarse-graining method.")
    method_keywords: Optional[Dict[str, Any]] = Field(
        None, description="Additional keyword arguments used for the cg method."
    )


class OutputCoarse(OutputProc):
    """An output model for coarse-graining."""

    proc_input: InputCoarse = Field(
        ...,
        description=InputCoarse.__doc__,
    )
    molecule: Union[Molecule, List[Molecule]] = Field(
        None, description="A single or list of coarse-grained molecule objects."
    )
