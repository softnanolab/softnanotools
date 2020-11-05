import argparse
from .merge import main as _main
from .merge import _description, _parser
args = _parser().parse_args()
_main(**vars(args))