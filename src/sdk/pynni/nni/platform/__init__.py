# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from ..env_vars import trial_env_vars

if trial_env_vars.NNI_PLATFORM is None:
    from .standalone import *
elif trial_env_vars.NNI_PLATFORM == 'unittest':
    from .test import *
elif trial_env_vars.NNI_PLATFORM in ('local', 'remote', 'pai', 'kubeflow', 'frameworkcontroller'):
    from .local import *
else:
    raise RuntimeError('Unknown platform %s' % trial_env_vars.NNI_PLATFORM)
