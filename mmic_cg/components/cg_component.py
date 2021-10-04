"""
Components in mmic_cg.
"""

from typing import List, Tuple, Optional, Set
from cmselemental.util.decorators import classproperty
from mmic.components.blueprints import StrategyComponent

# from mmic.components.blueprints import StrategyComponent
from ..models import InputCoarse, OutputCoarse

__all__ = ["CoarseComponent"]


class CoarseComponent(StrategyComponent):
    """A sample component that defines the 3 required methods."""

    @classproperty
    def input(cls):
        return InputCoarse

    @classproperty
    def output(cls):
        return OutputCoarse

    @classproperty
    def tactic_comps(cls) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return {"mmic_md_protomd"}
