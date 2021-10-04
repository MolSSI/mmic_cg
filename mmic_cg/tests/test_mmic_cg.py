# Import package, test suite, and other packages as needed
import mmic_cg
import pytest
from mmic.components.blueprints import TacticComponent
from cmselemental.util.decorators import classproperty
import mm_data
from typing import Tuple
import sys
import json


molfiles = [filep for filen, filep in mm_data.mols.items() if filep.endswith(".json")]


def test_mmic_cg_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_cg" in sys.modules


@pytest.mark.parametrize("molfile", molfiles)
def test_mmic_cg_models(molfile):
    with open(molfile, "r") as fp:
        mol = json.load(fp)

    inputs = mmic_cg.InputCoarse(
        molecule=mol,
        schema_name="test",
        schema_version=1.0,
        method="some_method",
    )

    class CoarseDummyComponent(TacticComponent):
        @classproperty
        def input(cls):
            return mmic_cg.InputCoarse

        @classproperty
        def output(cls):
            return mmic_cg.OutputCoarse

        @classmethod
        def strategy_comps(cls):
            return mmic_cg.CoarseComponent

        @classproperty
        def version(cls):
            return None

        def execute(
            self,
            inputs: mmic_cg.InputCoarse,
        ) -> Tuple[bool, mmic_cg.OutputCoarse]:

            return True, mmic_cg.OutputCoarse(
                proc_input=inputs,
                molecule=inputs.molecule,
                schema_name=inputs.schema_name,
                schema_version=inputs.schema_version,
                success=True,
            )

    outputs = CoarseDummyComponent.compute(inputs)
