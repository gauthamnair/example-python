# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs")

python_tests(
  name="tests",
  environment=parametrize(d="docker", l="local")
)

python_sources()

local_environment(
  name="local_env",
)

docker_environment(
  name="docker_env",
  platform="linux_x86_64",
  image="python:3.11.6-bullseye",
  python_bootstrap_search_path=["<PATH>"],
  pass_through_env_vars=["CFG"],
)