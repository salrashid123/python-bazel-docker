workspace(name = "qs")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "a644da969b6824cc87f8fe7b18101a8a6c57da5db39caa6566ec6109f37d2141",
    strip_prefix = "rules_python-0.20.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.20.0/rules_python-0.20.0.tar.gz",
)


load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")
py_repositories()


load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
   name = "my_deps",
   requirements_lock = "//:requirements.txt",
)
load("@my_deps//:requirements.bzl", "install_deps", "requirement")
install_deps()


# ---------------------------------

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()


load("@io_bazel_rules_docker//python3:image.bzl", _py_image_repos = "repositories")
_py_image_repos()


load("@io_bazel_rules_docker//container:pull.bzl", "container_pull")

container_pull(
    name = "distroless_base",
    digest = "sha256:75f63d4edd703030d4312dc7528a349ca34d48bec7bd754652b2d47e5a0b7873",
    registry = "gcr.io",
    repository = "distroless/base",
)


container_pull(
    name = "distroless_python3-debian11",
    digest = "sha256:57dbab565d405ce5ae9c7a8c781c95fa229655cb8381d0e5db4ece28661fa687",
    registry = "gcr.io",
    repository = "distroless/python3-debian11",
)
